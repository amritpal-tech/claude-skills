# Sound for Life · "Hear life again" (30 s motion film)

A 30-second motion-graphics film for [soundforlife.in](https://soundforlife.in/), built in the
HyperFrames format used by [NullMotion](https://github.com/blixvip/NullMotion): one HTML scene
driven by a paused GSAP timeline, rendered frame by frame. Its moves are adapted from NullMotion's
templates: kinetic headline (22), three-step cards (02), line-growth chart (16), notification (06),
and CTA pill/click (01, 18).

| File | Use it for |
|---|---|
| `out/soundforlife-promo-1080p.mp4` | The film. 1920×1080, 30 fps, H.264 + AAC, with sound. Plays everywhere. |
| `out/soundforlife-promo-1080p.webm` | Same film as VP9 + Opus (smaller); offer it first in `<video>`. |
| `out/soundforlife-hero-720p-muted.mp4` | Light, silent copy for an autoplaying hero background. |
| `out/poster.jpg` | `poster` image shown before playback. |

## The story (96 bpm, every cut on a bar line)

| Time | Scene | What happens |
|---|---|---|
| 0:00–0:05 | **The quiet** | Words for everyday sounds (*Conversations, Laughter, Temple bells…*) float blurred and grey; the music is heard muffled, as with hearing loss. *"Missing the sounds you love?"* |
| 0:05–0:10 | **Clarity** | A bright pulse sweeps the waveform; each word snaps into focus as it passes and the music's filter opens. *"Hear (life) again."* |
| 0:10–0:12.5 | **Brand** | The sound-wave mark draws on; *"Sound for Life · Complete hearing care, by certified audiologists"*. |
| 0:12.5–0:17.5 | **Step one** | *"Start with a precise hearing test"*. An audiogram plots right ear (O) then left ear (X); each point plays its real test tone (250 Hz–8 kHz) in that ear. *"Your hearing report is ready."* |
| 0:17.5–0:22.5 | **Care** | *"Care that stays with you"*: Expert consultation → Trial & fitting → Lifelong aftercare. |
| 0:22.5–0:25 | **Near you** | *40+ clinics, 15+ cities*, a network radiating from Delhi NCR. *"Hearing care, close to home."* |
| 0:25–0:30 | **End card** | *"Rediscover the sounds you love."* A cursor clicks **Book a hearing test**; soundforlife.in · +91 90154 01540. |

The soundtrack (`score.py`) is synthesized from scratch with numpy: no samples, no stock music, nothing to license.

## Before publishing: check these facts

The site could not be loaded from the build environment, so the copy was written from public
listings of Sound for Life / SFL Hearing Solutions. Please confirm:

- **40+ clinics** and **15+ cities**: `CONFIG.clinics` / `CONFIG.cities` in `composition/index.html`.
- **+91 90154 01540**: the `#contact` line near the end of the HTML.
- **Cities** in the ticker and on the map: `CONFIG.tickerCities` / `CONFIG.mapCities`.
- **Brand colours and logo**: the palette is a placeholder (deep teal + warm amber) set as CSS
  variables at the top of the file, and the wordmark is set in Inter. To use the official logo,
  swap the `#mark` SVG (scene 3) and `#end-logo` (end card) for it.

## Edit and re-render

All copy, colours and timing live in `composition/index.html`. Open it in a browser with `#play`
appended (e.g. `composition/index.html#play`) to watch it live.

```sh
# Needs Node 18+, Python 3 with numpy, FFmpeg, and Playwright (npm i -D playwright && npx playwright install chromium)
node render.mjs                         # frames -> out/video-master.mp4 (about 10 min for 900 frames)
node render.mjs --stills 8.6,15.8,27.5  # quick PNG checks -> out/stills/
python3 score.py out/score.wav          # soundtrack
./encode.sh                             # MP4, WebM, muted hero loop, poster
```

If you change a scene's timing, keep the matching cue times in `score.py` in step (they are listed
in its "sound design" section next to the scene they belong to).

## Put it on the website

As a promo with sound (the visitor presses play):

```html
<video controls playsinline preload="metadata" poster="/media/poster.jpg" width="1920" height="1080" style="width:100%;height:auto;border-radius:16px">
  <source src="/media/soundforlife-promo-1080p.webm" type="video/webm">
  <source src="/media/soundforlife-promo-1080p.mp4" type="video/mp4">
</video>
```

As a silent, looping hero background (browsers only autoplay muted video):

```html
<video autoplay muted loop playsinline preload="auto" poster="/media/poster.jpg" style="width:100%;height:100%;object-fit:cover">
  <source src="/media/soundforlife-hero-720p-muted.mp4" type="video/mp4">
</video>
<script>
  // Respect visitors who ask for less motion: show the poster instead of playing.
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) document.querySelectorAll('video[autoplay]').forEach(v => { v.removeAttribute('autoplay'); v.pause(); });
</script>
```

Video text isn't read by screen readers or search engines, so put the key line and the booking link
in the page's own HTML next to the video.

## See it in NullMotion's breakdown view

NullMotion's preview shows a finished film on top and one rough black-and-white HyperFrames draft per
section underneath, in sync. `nullmotion/` holds this film's sections and drafts in that format:

```sh
git clone https://github.com/blixvip/NullMotion.git
node nullmotion/install.mjs ./NullMotion      # writes only to NullMotion's ignored local library
cd NullMotion && npm start                    # open http://127.0.0.1:4343/?v=soundforlife
```

In Chrome or Edge, **Download → Whole preview** exports the film-over-drafts breakdown as an MP4.

## Credits

GSAP 3.14.2 (`composition/vendor/gsap.min.js`) is bundled from NullMotion with its license header;
terms at <https://gsap.com/standard-license>. Inter and JetBrains Mono are SIL Open Font License
fonts. Rendering expects them installed locally and falls back to system sans-serif otherwise.
