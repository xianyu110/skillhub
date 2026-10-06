---
name: release-notes-reel
description: Turn release notes into a 12-second "What's new" feature reel video (version badge, three feature cards, CTA end card) with HyperFrames (HTML → MP4). Use for changelog video, feature update reel, release announcement, product update clip for X/LinkedIn, 更新日志视频, 版本发布短片.
license: MIT
metadata:
  author: SkillHub
  version: 1.0.0
  engine: HyperFrames (Apache-2.0, heygen-com/hyperframes)
---

# Release Notes Reel

A ready-made, brand-able video template. You fill a small JSON brief, HyperFrames renders a
deterministic MP4 locally. Output: **12 s · 1280x720 (landscape)**, 30 fps, H.264.

## Requirements

- Node.js 22+ and FFmpeg on PATH (`npx hyperframes@0.8.136 doctor` checks both; Chrome is fetched automatically if missing).
- No API key. Everything renders locally.

## Workflow

1. **Brief.** Read the changelog / PR list / release notes and pick the 3 changes users will care about most. Write each as a 2–3 word title and a ≤ 45-character line. Ask only for anything you cannot infer (brand color, CTA).
2. **Project.** Copy this skill's `template/` folder to `./videos/<slug>/` (keep `index.html`, `hyperframes.json`, `package.json`).
3. **Variables.** Write `./videos/<slug>/brief.json` with these keys: `product, version, f1t, f1d, f2t, f2d, f3t, f3d, cta, accent, bg`.
   Start from an example in `examples/` (`driftboard-2-4.json`, `lumen-notes-3-0.json`).
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

- Titles are action nouns ("Live tail"), lines say the benefit, not the implementation.
- Three features is the limit for 12 s; for more, duplicate a `.card` and extend `data-duration`.
- Use the product's real accent color; the dark `bg` keeps text contrast safe.

## Credits

Rendering engine: [HyperFrames](https://github.com/heygen-com/hyperframes) by HeyGen, Apache-2.0 — this skill
only ships its own template and instructions and calls the published `hyperframes` CLI. See `NOTICE`.
