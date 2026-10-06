---
name: launch-teaser-countdown
description: Render a 9-second product launch teaser video (3-2-1 countdown, flash, letter-by-letter product reveal, tagline, launch-date pill) from a short brief, using HyperFrames (HTML → MP4). Use for launch teaser, coming-soon video, pre-launch hype clip, Product Hunt teaser, 发布预告, 新品倒计时视频.
license: MIT
metadata:
  author: SkillHub
  version: 1.0.0
  engine: HyperFrames (Apache-2.0, heygen-com/hyperframes)
---

# Launch Teaser Countdown

A ready-made, brand-able video template. You fill a small JSON brief, HyperFrames renders a
deterministic MP4 locally. Output: **9 s · 1280x720 (landscape)**, 30 fps, H.264.

## Requirements

- Node.js 22+ and FFmpeg on PATH (`npx hyperframes@0.8.136 doctor` checks both; Chrome is fetched automatically if missing).
- No API key. Everything renders locally.

## Workflow

1. **Brief.** Ask for: product name (≤ 14 characters reads best), one-line tagline (≤ 45 characters), launch line (e.g. "Launching Oct 21"), URL, and 2 brand colors + a dark background color.
2. **Project.** Copy this skill's `template/` folder to `./videos/<slug>/` (keep `index.html`, `hyperframes.json`, `package.json`).
3. **Variables.** Write `./videos/<slug>/brief.json` with these keys: `product, tagline, date, url, accent, accent2, bg`.
   Start from an example in `examples/` (`orbit.json`, `pocketroast.json`).
4. **Check.** `check` validates the declared defaults, so first copy your brief values into the `default`
   fields of `data-composition-variables` in `index.html` (this also makes the project self-contained), then:
   ```bash
   cd videos/<slug> && npx hyperframes@0.8.136 check
   ```
   Fix errors (contrast, overflow) by shortening text or adjusting colors. Expected warnings are listed under Tips.
5. **Preview frames** (optional): `npx hyperframes@0.8.136 snapshot --at 2,5,8` and look at the PNGs in `snapshots/`.
6. **Render.**
   ```bash
   npx hyperframes@0.8.136 render --variables-file brief.json -o renders/<slug>.mp4 --crf 24
   ```
7. **Poster** (optional): `ffmpeg -ss 6 -i renders/<slug>.mp4 -frames:v 1 renders/<slug>.jpg`.
8. Report the output path, duration and file size to the user.

## Customising beyond variables

`template/index.html` is plain HTML + CSS + a GSAP timeline registered on `window.__timelines["main"]`.
Follow HyperFrames rules when editing: every timed element keeps `data-start`/`data-duration`, the timeline
stays `paused: true`, and no `Math.random()`, `Date.now()` or network fetches inside the script.
Use fonts HyperFrames embeds automatically (Inter, Outfit, JetBrains Mono, Playfair Display, Montserrat, Poppins…)
or add an `@font-face`.

## Tips

- Keep the product name short — every letter animates in; long names get small.
- Pick a dark `bg` and two bright accents; the blurred blobs carry the brand color.
- For 9:16, render with the composition resized (change 1280x720 → 720x1280 in `index.html`) and re-check.

## Credits

Rendering engine: [HyperFrames](https://github.com/heygen-com/hyperframes) by HeyGen, Apache-2.0 — this skill
only ships its own template and instructions and calls the published `hyperframes` CLI. See `NOTICE`.
