#!/usr/bin/env node
// Frame-accurate renderer for a HyperFrames composition.
//
// Opens the composition in headless Chromium, seeks its paused GSAP timeline to each frame's
// exact time (window.__seek), screenshots the frame and pipes it to FFmpeg. Nothing plays in real
// time, so no frame is ever dropped, whatever the machine.
//
//   node render.mjs                              # whole film -> out/video-master.mp4
//   node render.mjs --stills 0,5.5,13,28         # PNG stills at those times -> out/stills/
//   node render.mjs --from 12.5 --to 17.5 --out out/test-scene.mp4
//
// Needs Node 18+, FFmpeg on PATH and Playwright (npm i -D playwright && npx playwright install chromium).
import { createRequire } from 'node:module';
import { spawn } from 'node:child_process';
import { mkdirSync } from 'node:fs';
import { writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const args = Object.fromEntries(process.argv.slice(2).reduce((pairs, arg, i, all) => {
  if (arg.startsWith('--')) pairs.push([arg.slice(2), all[i + 1]?.startsWith('--') || all[i + 1] === undefined ? true : all[i + 1]]);
  return pairs;
}, []));

let chromium;
try { ({ chromium } = createRequire(import.meta.url)('playwright')); }
catch { console.error('Playwright is missing. Run: npm i -D playwright && npx playwright install chromium'); process.exit(1); }

const composition = path.resolve(here, args.composition || 'composition/index.html');
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
page.on('pageerror', error => { console.error('Composition error:', error.message); process.exitCode = 1; });
await page.goto(pathToFileURL(composition).href);
await page.waitForFunction(() => window.__timelines?.root && typeof window.__seek === 'function');
await page.evaluate(() => document.fonts.ready);
// The film is set in locally installed fonts. A missing one silently falls back, so measure and warn.
const missingFonts = await page.evaluate(() => ['Inter', 'Inter Display', 'JetBrains Mono'].filter(family => {
  const context = document.createElement('canvas').getContext('2d');
  const width = font => { context.font = `700 64px ${font}`; return context.measureText('Hear life again 0123').width; };
  return width(`"${family}", monospace`) === width('monospace') && width(`"${family}", serif`) === width('serif');
}));
if (missingFonts.length) console.warn(`Warning: font(s) not installed, falling back: ${missingFonts.join(', ')}. Install Inter (rsms.me/inter) and JetBrains Mono.`);

const meta = await page.evaluate(() => {
  const read = name => Number(document.querySelector(`meta[name="${name}"]`)?.content);
  return { duration: read('duration') / 1000, fps: read('fps'), width: read('width'), height: read('height') };
});
await page.setViewportSize({ width: meta.width, height: meta.height });
const fps = Number(args.fps || meta.fps);
const seek = time => page.evaluate(t => window.__seek(t), time);

if (args.stills) {
  const dir = path.resolve(here, args['stills-dir'] || 'out/stills');
  mkdirSync(dir, { recursive: true });
  for (const time of String(args.stills).split(',').map(Number)) {
    await seek(time);
    const file = path.join(dir, `t${time.toFixed(2).padStart(5, '0')}.png`);
    await writeFile(file, await page.screenshot({ type: 'png' }));
    console.log(file);
  }
  await browser.close();
  process.exit();
}

const from = Number(args.from || 0), to = Number(args.to || meta.duration);
const frames = Math.round((to - from) * fps);
const out = path.resolve(here, args.out || 'out/video-master.mp4');
mkdirSync(path.dirname(out), { recursive: true });

// A high-quality master; delivery encodes (web MP4, WebM, audio) are made from it by encode.sh.
const ffmpeg = spawn('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y',
  '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'png', '-i', '-',
  '-c:v', 'libx264', '-preset', 'slow', '-crf', '12', '-pix_fmt', 'yuv420p', '-tune', 'animation',
  '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
const finished = new Promise((resolve, reject) => ffmpeg.on('close', code => code === 0 ? resolve() : reject(new Error(`ffmpeg exited with ${code}`))));

const started = Date.now();
for (let frame = 0; frame < frames; frame++) {
  await seek(from + frame / fps);
  const png = await page.screenshot({ type: 'png' });
  if (!ffmpeg.stdin.write(png)) await new Promise(resolve => ffmpeg.stdin.once('drain', resolve));
  if (frame % fps === 0) process.stdout.write(`\r${frame}/${frames} frames · ${((Date.now() - started) / 1000).toFixed(0)}s`);
}
ffmpeg.stdin.end();
await finished;
await browser.close();
console.log(`\r${frames}/${frames} frames · ${((Date.now() - started) / 1000).toFixed(0)}s → ${out}`);
