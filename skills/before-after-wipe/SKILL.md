---
name: before-after-wipe
description: Render a 10-second before/after product demo video: a messy "before" screen is wiped away to reveal a clean "after" dashboard, then an end card with the product name and outcome — HyperFrames (HTML → MP4). Use for transformation demos, SaaS before-after, workflow improvement clips, 前后对比视频, 效果对比.
license: MIT
metadata:
  author: SkillHub
  version: 1.0.0
  engine: HyperFrames (Apache-2.0, heygen-com/hyperframes)
---

# Before / After Wipe

A ready-made, brand-able video template. You fill a small JSON brief, HyperFrames renders a
deterministic MP4 locally. Output: **10 s · 1280x720 (landscape)**, 30 fps, H.264.

## Requirements

- Node.js 22+ and FFmpeg on PATH (`npx hyperframes@0.8.136 doctor` checks both; Chrome is fetched automatically if missing).
- No API key. Everything renders locally.

## Workflow

1. **Brief.** Ask what the user's life looked like before (one label) and after (one label + three short metrics shown on the dashboard tiles), plus a ≤ 40-character outcome headline.
2. **Project.** Copy this skill's `template/` folder to `./videos/<slug>/` (keep `index.html`, `hyperframes.json`, `package.json`).
3. **Variables.** Write `./videos/<slug>/brief.json` with these keys: `product, beforeLabel, afterLabel, headline, m1, m2, m3, accent`.
   Start from an example in `examples/` (`driftboard.json`, `ledgerly.json`).
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

- The "before" sheet and "after" tiles are generic HTML mockups — replace `#before`/`#after` markup with real screenshots (`<img>`) for a true product demo.
- `text_occluded` warnings during the wipe are expected (the reveal covers text on purpose).
- Keep metrics short: "p95 182 ms", "Runway 19 mo".

## Credits

Rendering engine: [HyperFrames](https://github.com/heygen-com/hyperframes) by HeyGen, Apache-2.0 — this skill
only ships its own template and instructions and calls the published `hyperframes` CLI. See `NOTICE`.
