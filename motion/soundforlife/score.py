#!/usr/bin/env python3
"""Soundtrack for the Sound for Life film, synthesized from scratch (numpy only, no samples).

The idea follows the picture: for the first five seconds the music is heard "through hearing loss"
(a heavy low-pass); at 5.0 s, when the clear waveform sweeps across the screen, the filter opens.
In the hearing-test scene each audiogram point gets a real test tone at its frequency, panned to the
ear it belongs to. 96 bpm, so one bar is 2.5 s and every scene cut lands on a bar line.

    python3 score.py out/score.wav
"""
import sys
import wave

import numpy as np

SR = 48000
DURATION = 30.0
N = int(SR * DURATION)
t_all = np.arange(N) / SR
rng = np.random.default_rng(7)

BAR = 2.5
CLARITY = 5.0  # T.clarity in the composition


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def pan_gains(pan):
    """Equal-power pan, -1 left .. +1 right."""
    angle = (pan + 1) * np.pi / 4
    return np.cos(angle), np.sin(angle)


def place(bus, start, mono, pan=0.0, gain=1.0):
    """Mix a mono signal into a stereo bus at `start` seconds."""
    i = int(start * SR)
    if i >= N:
        return
    mono = mono[: N - i] * gain
    gl, gr = pan_gains(pan)
    bus[0, i:i + len(mono)] += mono * gl
    bus[1, i:i + len(mono)] += mono * gr


def envelope(length, attack, release, total):
    """Linear-ish attack, sustain, cosine release; all in seconds."""
    n = int(total * SR)
    env = np.ones(n)
    a, r = int(attack * SR), int(release * SR)
    if a:
        env[:a] = np.sin(np.linspace(0, np.pi / 2, a)) ** 2
    if r:
        env[-r:] *= np.cos(np.linspace(0, np.pi / 2, r)) ** 2
    return env[: int(length * SR)] if length < total else env


def onepole_lowpass(x, cutoff):
    """One-pole low-pass with a per-sample cutoff (array or scalar), run twice for 12 dB/oct."""
    cutoff = np.broadcast_to(np.asarray(cutoff, dtype=float), x.shape[-1:])
    a = 1 - np.exp(-2 * np.pi * cutoff / SR)
    out = np.empty_like(x)
    for ch in range(x.shape[0]):
        for _ in range(2):
            src = x[ch] if _ == 0 else out[ch].copy()
            y, prev = out[ch], 0.0
            for k in range(src.shape[0]):
                prev += a[k] * (src[k] - prev)
                y[k] = prev
    return out


# ---------------------------------------------------------------------------- instruments
def pad_note(freq, length):
    """Warm detuned pad voice: three slightly detuned oscillators with soft harmonics."""
    tt = np.arange(int(length * SR)) / SR
    sig = np.zeros_like(tt)
    for cents, phase in ((-6, 0.3), (0, 1.1), (6, 2.0)):
        f = freq * 2 ** (cents / 1200)
        sig += np.sin(2 * np.pi * f * tt + phase) + .28 * np.sin(4 * np.pi * f * tt + phase) + .1 * np.sin(6 * np.pi * f * tt)
    wobble = 1 + .08 * np.sin(2 * np.pi * .17 * tt + freq)
    return sig * wobble / 3


def bell(midi, decay=.9, bright=.5):
    """Mallet/bell pluck: harmonic plus one inharmonic partial, higher partials die faster."""
    f = hz(midi) if midi < 200 else midi
    length = decay * 5
    tt = np.arange(int(length * SR)) / SR
    sig = (np.sin(2 * np.pi * f * tt) * np.exp(-tt / decay)
           + .45 * bright * np.sin(2 * np.pi * 2 * f * tt) * np.exp(-tt / (decay * .5))
           + .18 * bright * np.sin(2 * np.pi * 3.01 * f * tt) * np.exp(-tt / (decay * .3))
           + .12 * np.sin(2 * np.pi * 4.2 * f * tt) * np.exp(-tt / (decay * .18)))
    attack = int(.004 * SR)
    sig[:attack] *= np.linspace(0, 1, attack)
    return sig


def test_tone(freq, length=.17):
    """An audiometry beep: a pure sine with 12 ms raised-cosine ramps."""
    tt = np.arange(int(length * SR)) / SR
    sig = np.sin(2 * np.pi * freq * tt)
    ramp = int(.012 * SR)
    window = np.ones_like(sig)
    window[:ramp] = np.sin(np.linspace(0, np.pi / 2, ramp)) ** 2
    window[-ramp:] = window[:ramp][::-1]
    return sig * window


def noise_sweep(length, f0, f1, shape=2.0, curve='rise'):
    """Filtered noise whose low-pass cutoff glides from f0 to f1 (a riser or a whoosh)."""
    n = int(length * SR)
    x = rng.standard_normal((1, n))
    u = np.linspace(0, 1, n)
    cutoff = f0 * (f1 / f0) ** u
    y = onepole_lowpass(x, cutoff)[0]
    amp = u ** shape if curve == 'rise' else np.sin(np.pi * u) ** shape
    return y * amp


# ---------------------------------------------------------------------------- arrangement
# One chord per bar (pad voicing, MIDI). Bars 1-2 are heard muffled.
CHORDS = [
    [50, 57, 61, 64, 66],  # 1  Dmaj9
    [47, 54, 57, 61, 62],  # 2  Bm9
    [43, 50, 54, 57, 59],  # 3  Gmaj9  (clarity)
    [45, 52, 57, 62, 64],  # 4  Asus4
    [50, 57, 61, 64, 66],  # 5  Dmaj9  (brand)
    [47, 54, 57, 62, 66],  # 6  Bm7    (hearing test: tones sit on B)
    [52, 59, 62, 66, 67],  # 7  Em9
    [43, 50, 54, 59, 62],  # 8  Gmaj7  (care)
    [45, 52, 57, 61, 64],  # 9  A
    [42, 49, 57, 61, 64],  # 10 F#m7   (network)
    [43, 50, 54, 57, 59],  # 11 Gmaj9  (end card)
    [50, 57, 61, 64, 66],  # 12 Dmaj9
]

music = np.zeros((2, N))
sfx = np.zeros((2, N))

# Pad: chords overlap slightly so changes breathe.
for b, chord in enumerate(CHORDS):
    start = b * BAR - .2
    hold = BAR + (2.6 if b == len(CHORDS) - 1 else .2)
    length = hold + 1.1
    for k, m in enumerate(chord):
        voice = pad_note(hz(m), length) * envelope(length, .7, 1.1, length)
        place(music, max(0, start), voice[int(max(0, -start) * SR):], pan=(-.45 + .9 * k / (len(chord) - 1)), gain=.11)

# Bass: the chord root kept between 62 and 110 Hz, from the clarity moment on.
for b, chord in enumerate(CHORDS[2:], start=2):
    root = chord[0] if chord[0] <= 45 else chord[0] - 12
    length = BAR + .9
    tt = np.arange(int(length * SR)) / SR
    voice = (np.sin(2 * np.pi * hz(root) * tt) + .25 * np.sin(4 * np.pi * hz(root) * tt)) * envelope(length, .08, .9, length)
    place(music, b * BAR, voice, gain=.1)

# Arpeggio: eighth notes, an octave up, resting under the hearing test and the final bar.
EIGHTH = BAR / 8
PATTERN = [1, 2, 3, 4, 3, 2, 4, 3]
for b, chord in enumerate(CHORDS):
    if b < 2 or b in (5, 6) or b == 11:
        continue
    for k, idx in enumerate(PATTERN):
        if b == 10 and k % 2:
            continue  # quarter notes on the end card
        vel = .55 + .25 * (k % 4 == 0) + .08 * rng.random()
        place(music, b * BAR + k * EIGHTH, bell(chord[idx] + 12, decay=.45, bright=.35), pan=(-.35 if k % 2 else .35), gain=.075 * vel)

# "Through hearing loss": the music bus is low-passed until the sweep, then the filter opens.
open_end = CLARITY + 1.35
seg = int((open_end + .2) * SR)
u = np.clip((t_all[:seg] - CLARITY) / (open_end - CLARITY), 0, 1)
cutoff = 320 * (19000 / 320) ** (u ** 1.6)
muffled = onepole_lowpass(music[:, :seg], cutoff)
fade = np.clip((t_all[:seg] - open_end) / .2, 0, 1)
music[:, :seg] = muffled * (1 - fade) + music[:, :seg] * fade
music[:, :seg] *= .72 + .28 * u  # a little quieter while muffled

# Duck the music under the hearing-test tones.
duck = np.ones(N)
for a, b, lo in ((13.55, 13.8, .42), (16.4, 16.9, 1.0)):
    i0, i1 = int(a * SR), int(b * SR)
    prev = duck[i0 - 1]
    duck[i0:i1] = np.linspace(prev, lo, i1 - i0)
    duck[i1:] = lo
music *= duck

# ---------------------------------------------------------------------------- sound design (synced to the composition)
place(sfx, CLARITY - 1.1, noise_sweep(1.1, 300, 9000, shape=2.6), gain=.05)                 # riser into the sweep
for m, d in ((86, 1.6), (90, 1.4), (93, 1.2), (98, 1.0)):                                     # clarity shimmer
    place(sfx, CLARITY + .02, bell(m, decay=d, bright=.6), pan=(m - 92) / 12, gain=.05)
kinetic = CLARITY + 1.85
place(sfx, kinetic - .05, noise_sweep(.55, 800, 6000, shape=1.5, curve='swell'), pan=-.4, gain=.035)  # "Hear" slides in
place(sfx, kinetic + .2, bell(81, decay=.8, bright=.7), gain=.075)                            # pill pops
place(sfx, kinetic + 1.05, noise_sweep(.8, 2500, 12000, shape=1.2, curve='swell'), pan=.3, gain=.02)  # sheen
place(sfx, 10.0, bell(74, decay=1.8, bright=.5), gain=.08)                                    # logo
for i, m in enumerate((86, 90, 93)):                                                          # the three arcs
    place(sfx, 10.18 + i * .15, bell(m, decay=.9, bright=.4), pan=.15 * i, gain=.045)

# Hearing test: right ear first (panned right), then left, one tone per audiogram point.
FREQS = [250, 500, 1000, 2000, 4000, 8000]
tone_gain = [.11, .1, .085, .07, .05, .035]  # rough equal-loudness taper
right_at, gap = 12.5 + 1.3, .2
left_at = right_at + 6 * gap + .2
for i, f in enumerate(FREQS):
    place(sfx, right_at + i * gap, test_tone(f), pan=.85, gain=tone_gain[i])
    place(sfx, left_at + i * gap, test_tone(f), pan=-.85, gain=tone_gain[i])
toast = left_at + 6 * gap + .25
place(sfx, toast, bell(88, decay=.5, bright=.5), gain=.06)                                    # report ready
place(sfx, toast + .12, bell(93, decay=.9, bright=.5), gain=.06)

for i, m in enumerate((74, 78, 81)):                                                          # care cards
    place(sfx, 17.5 + .35 + i * .35, bell(m, decay=.7, bright=.4), pan=(-.4 + .4 * i), gain=.05)

for i in range(5):                                                                            # city pings
    at = 22.5 + .15 + i * .1 + .2
    tt = np.arange(int(1.6 * SR)) / SR
    ping = np.sin(2 * np.pi * 1320 * (1 - .02 * tt) * tt) * np.exp(-tt / .35)
    place(sfx, at, ping, pan=(-.5 + .25 * i), gain=.022)

press = 25.0 + 2.3                                                                            # CTA press
click = rng.standard_normal(int(.012 * SR)) * np.exp(-np.arange(int(.012 * SR)) / (.002 * SR))
place(sfx, press, click, gain=.05)
place(sfx, press + .03, bell(86, decay=1.2, bright=.6), gain=.06)
place(sfx, press + .1, bell(93, decay=1.6, bright=.6), gain=.05)

# ---------------------------------------------------------------------------- reverb, master
mix = music + sfx


def reverb(x, seconds=2.6, mix_level=.3):
    n = int(seconds * SR)
    tt = np.arange(n) / SR
    ir = rng.standard_normal((2, n)) * np.exp(-tt * 6.9 / seconds)
    ir = onepole_lowpass(ir, 5200)
    ir[:, : int(.012 * SR)] = 0  # pre-delay
    ir /= np.sqrt((ir ** 2).sum(axis=1, keepdims=True))
    size = 1 << int(np.ceil(np.log2(x.shape[1] + n)))
    wet = np.fft.irfft(np.fft.rfft(x, size) * np.fft.rfft(ir, size), size)[:, : x.shape[1]]
    return x + mix_level * wet


mix = reverb(mix)
# Zero-phase high-pass at 45 Hz: nothing below what small speakers and earbuds can play anyway.
spectrum = np.fft.rfft(mix, axis=1)
f = np.fft.rfftfreq(mix.shape[1], 1 / SR)
spectrum *= 1 / np.sqrt(1 + (45 / np.maximum(f, 1e-3)) ** 8)
mix = np.fft.irfft(spectrum, mix.shape[1], axis=1)
fade_in = np.clip(t_all / .8, 0, 1) ** 2
fade_out = np.clip((DURATION - t_all) / 1.6, 0, 1) ** 1.5
mix *= fade_in * fade_out
mix = np.tanh(mix * 1.4) / 1.4  # gentle soft clip
mix *= .89 / np.max(np.abs(mix))  # -1 dBFS peak

out = sys.argv[1] if len(sys.argv) > 1 else 'out/score.wav'
with wave.open(out, 'wb') as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((mix.T * 32767).astype('<i2').tobytes())
print(out)
