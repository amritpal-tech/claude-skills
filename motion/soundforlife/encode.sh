#!/usr/bin/env bash
# Builds the delivery files from the rendered master (render.mjs) and the score (score.py).
#
#   node render.mjs && python3 score.py out/score.wav && ./encode.sh
set -euo pipefail
cd "$(dirname "$0")"
master=out/video-master.mp4 score=out/score.wav
[[ -f $master && -f $score ]] || { echo "Run node render.mjs and python3 score.py out/score.wav first." >&2; exit 1; }
q=(-hide_banner -loglevel error -y)

# Two-pass loudness normalisation to -16 LUFS / -1.5 dBTP, the usual target for web video.
stats=$(ffmpeg -hide_banner -nostats -i "$score" -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
get() { sed -n "s/.*\"$1\" : \"\(.*\)\".*/\1/p" <<<"$stats"; }
loudnorm="loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=$(get input_i):measured_TP=$(get input_tp):measured_LRA=$(get input_lra):measured_thresh=$(get input_thresh):offset=$(get target_offset):linear=true"

# 1. Main film: H.264 + AAC, plays everywhere, starts fast (moov atom first).
ffmpeg "${q[@]}" -i "$master" -i "$score" -map 0:v -map 1:a -af "$loudnorm" -ar 48000 \
  -c:v libx264 -preset slow -crf 18 -profile:v high -pix_fmt yuv420p -tune animation -g 60 \
  -c:a aac -b:a 192k -movflags +faststart -shortest out/soundforlife-promo-1080p.mp4

# 2. Same film as VP9 + Opus, usually smaller; list it first in <video> for browsers that support it.
ffmpeg "${q[@]}" -i "$master" -i "$score" -map 0:v -map 1:a -af "$loudnorm" -ar 48000 \
  -c:v libvpx-vp9 -crf 30 -b:v 0 -row-mt 1 -deadline good -cpu-used 2 -pix_fmt yuv420p -g 60 \
  -c:a libopus -b:a 128k -shortest out/soundforlife-promo-1080p.webm

# 3. Muted 720p loop for an autoplaying hero background (browsers only autoplay muted video).
ffmpeg "${q[@]}" -i "$master" -an -vf scale=1280:720:flags=lanczos \
  -c:v libx264 -preset slow -crf 23 -profile:v high -pix_fmt yuv420p -tune animation -g 60 -movflags +faststart \
  out/soundforlife-hero-720p-muted.mp4

# 4. Poster for <video poster="…">: the "Hear life again." frame.
ffmpeg "${q[@]}" -ss 8.6 -i "$master" -frames:v 1 -q:v 2 out/poster.jpg

# 5. One still per section for the NullMotion library (nullmotion/install.mjs).
mkdir -p nullmotion/posters
for pair in 0:2.6 1:8.6 2:11.4 3:16.9 4:20.2 5:24.0 6:27.8; do
  ffmpeg "${q[@]}" -ss "${pair#*:}" -i "$master" -frames:v 1 -vf scale=640:360:flags=lanczos -q:v 3 "nullmotion/posters/soundforlife-${pair%%:*}.jpg"
done

ls -lh out/soundforlife-* out/poster.jpg
