#!/usr/bin/env bash
# Install the video toolchain: ffmpeg, yt-dlp, Whisper (openai-whisper) and
# what Remotion needs to render. Idempotent: safe to run on every session start.
#
# Cloud sessions start from a clean container, so add this line to the
# environment's setup script (cloud environment menu -> Edit -> Setup script):
#
#   cd claude-skills && bash install-video-tools.sh
#
# Local machines: run it once; the tools persist.
set -euo pipefail

say() { printf '\n== %s\n' "$*"; }

# ffmpeg / ffprobe: usually preinstalled in Claude Code cloud images.
if ! command -v ffmpeg >/dev/null 2>&1 || ! command -v ffprobe >/dev/null 2>&1; then
  say "ffmpeg"
  if command -v apt-get >/dev/null 2>&1; then
    apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq ffmpeg
  elif command -v brew >/dev/null 2>&1; then
    brew install ffmpeg
  else
    echo "ffmpeg missing and no apt-get/brew to install it" >&2; exit 1
  fi
fi

# uv installs each Python CLI into its own isolated environment.
if ! command -v uv >/dev/null 2>&1; then
  say "uv"
  python3 -m pip install -q --user uv
  export PATH="$HOME/.local/bin:$PATH"
fi

# yt-dlp, with the EJS challenge solver YouTube now requires. Node is the
# JavaScript runtime it uses to run that solver.
say "yt-dlp"
uv tool install -q --upgrade "yt-dlp[default]"
mkdir -p "$HOME/.config/yt-dlp"
grep -qs -- '--js-runtimes' "$HOME/.config/yt-dlp/config" \
  || echo '--js-runtimes node' >> "$HOME/.config/yt-dlp/config"

# Whisper. Prefer the CPU build of PyTorch from download.pytorch.org (~200 MB);
# if the network policy blocks that host, fall back to PyPI's default build
# (~5 GB, ~6 min; most of it CUDA libraries a CPU-only container never uses).
# Models download on first use from openaipublic.azureedge.net.
if ! command -v whisper >/dev/null 2>&1; then
  say "whisper"
  UV_HTTP_RETRIES=0 uv tool install -q openai-whisper \
      --extra-index-url https://download.pytorch.org/whl/cpu \
      --index-strategy unsafe-best-match 2>/dev/null \
    || { echo "download.pytorch.org unreachable; installing the PyPI build"; uv tool install -q openai-whisper; }
fi

# Remotion is installed per project (npx create-video@latest); it only needs
# Node 18+ here. Each project downloads its own headless Chrome on first render.
if ! node -e 'process.exit(+process.versions.node.split(".")[0] >= 18 ? 0 : 1)' 2>/dev/null; then
  echo "Remotion needs Node 18 or newer; found: $(node --version 2>/dev/null || echo none)" >&2; exit 1
fi

say "versions"
echo "ffmpeg   $(ffmpeg -version | head -1 | awk '{print $3}')"
echo "yt-dlp   $(yt-dlp --version)"
echo "whisper  $(uv tool list 2>/dev/null | awk '/^openai-whisper /{print $2}')"
echo "node     $(node --version)  (Remotion: npx create-video@latest)"
