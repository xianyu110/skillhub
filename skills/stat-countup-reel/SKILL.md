---
name: stat-countup-reel
description: Render a 10-second stats reel video where three numbers roll up like an odometer with progress bars — milestones, impact reports, metrics — using HyperFrames (HTML → MP4). Use for milestone announcements, year-in-review, investor update clips, impact numbers, 数据战报视频, 里程碑视频.
license: MIT
metadata:
  author: SkillHub
  version: 1.0.0
  engine: HyperFrames (Apache-2.0, heygen-com/hyperframes)
---

# Stat Count-up Reel

A ready-made, brand-able video template. You fill a small JSON brief, HyperFrames renders a
deterministic MP4 locally. Output: **10 s · 1280x720 (landscape)**, 30 fps, H.264.

## Requirements

- Node.js 22+ and FFmpeg on PATH (`npx hyperframes@0.8.136 doctor` checks both; Chrome is fetched automatically if missing).
- No API key. Everything renders locally.

## Workflow

1. **Brief.** Collect exactly three numbers with short labels (≤ 22 characters each) and a title. Values can include separators and units ("12,480", "99.98%", "4.9/5"). Use real, verifiable numbers only.
2. **Project.** Copy this skill's `template/` folder to `./videos/<slug>/` (keep `index.html`, `hyperframes.json`, `package.json`).
3. **Variables.** Write `./videos/<slug>/brief.json` with these keys: `title, s1, l1, s2, l2, s3, l3, footer, accent, bg, ink`.
   Start from an example in `examples/` (`fernway-impact.json`, `orbit-year-one.json`).
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

- Digits roll; separators and units stay still. Keep each value ≤ 7 characters to fit the column.
- `hyperframes check` reports hidden odometer digits as `text_occluded` — that is the rolling mask, expected.
- Swap `bg`/`ink` for dark mode.

## Credits

Rendering engine: [HyperFrames](https://github.com/heygen-com/hyperframes) by HeyGen, Apache-2.0 — this skill
only ships its own template and instructions and calls the published `hyperframes` CLI. See `NOTICE`.
