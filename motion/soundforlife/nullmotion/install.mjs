#!/usr/bin/env node
// Adds the Sound for Life film to a local NullMotion checkout as a reference, so its preview page
// shows the finished film on top and one black-and-white HyperFrames draft per section underneath.
//
//   node nullmotion/install.mjs /path/to/NullMotion
//   cd /path/to/NullMotion && npm start   ->  http://127.0.0.1:4343/?v=soundforlife
//
// Everything goes into NullMotion's ignored local library (.local-media/ and public/references/), the
// same place its own importer uses. Its showcase/ is never touched. The local JSON files replace the
// showcase ones, so the showcase entries are merged in to keep them in the library. Safe to re-run.
import { copyFile, mkdir, readFile, readdir, writeFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const target = process.argv[2];
if (!target || !existsSync(path.join(target, 'server.js')) || !existsSync(path.join(target, 'public', 'drafts.mjs'))) {
  console.error('Usage: node nullmotion/install.mjs /path/to/NullMotion');
  process.exit(1);
}
const spec = JSON.parse(await readFile(path.join(here, 'reference.json'), 'utf8'));
const id = spec.catalog.id;
const film = path.join(here, '..', 'out', 'soundforlife-promo-1080p.mp4');
if (!existsSync(film)) { console.error(`Missing ${film}. Render and encode the film first.`); process.exit(1); }

const media = path.join(target, '.local-media');
const references = path.join(target, 'public', 'references');
await mkdir(media, { recursive: true });
await mkdir(references, { recursive: true });

// The film, and its audio as ADTS AAC (what NullMotion's export reads). Without FFmpeg the server extracts it on first export.
await copyFile(film, path.join(media, `${id}.mp4`));
spawnSync('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', '-i', film, '-vn', '-c:a', 'copy', '-f', 'adts', path.join(media, `${id}.aac`)]);
for (const file of await readdir(path.join(here, 'posters'))) await copyFile(path.join(here, 'posters', file), path.join(references, file));

// Merge into the local library files, seeding them from the showcase the first time.
async function library(name, fallback) {
  for (const dir of [references, path.join(target, 'showcase', 'references')]) {
    try { return JSON.parse(await readFile(path.join(dir, name), 'utf8')); } catch {}
  }
  return fallback;
}
const catalog = await library('catalog.json', { references: [] });
const segments = spec.sections.map(({ start, end }, i) => ({ ref: id, in: start, out: end, part: i + 1, poster: `/references/${id}-${i}.jpg` }));
catalog.references = [...catalog.references.filter(reference => reference.id !== id), { ...spec.catalog, segments }];
const drafts = await library('drafts.json', { aliases: {}, drafts: {} });
drafts.drafts[id] = spec.drafts;
const sections = await library('sections.json', {});
sections[id] = spec.sections;
const cuts = await library('cuts.json', {});
cuts[id] = spec.cuts;

for (const [name, data] of Object.entries({ 'catalog.json': catalog, 'drafts.json': drafts, 'sections.json': sections, 'cuts.json': cuts })) {
  await writeFile(path.join(references, name), JSON.stringify(data, null, 2) + '\n');
}
console.log(`Added "${spec.catalog.name}" to ${target}\nRun npm start there and open http://127.0.0.1:4343/?v=${id}`);
