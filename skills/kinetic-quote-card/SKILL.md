---
name: kinetic-quote-card
description: Render a vertical (9:16) kinetic-typography quote video: words pop in one by one, a key word gets an animated underline, then the attribution slides in — built with HyperFrames (HTML → MP4). Use for quote reels, testimonial clips, founder quotes, Shorts/Reels/TikTok/视频号 text videos, 金句视频.
license: MIT
metadata:
  author: SkillHub
  version: 1.0.0
  engine: HyperFrames (Apache-2.0, heygen-com/hyperframes)
---

# Kinetic Quote Card

A ready-made, brand-able video template. You fill a small JSON brief, HyperFrames renders a
deterministic MP4 locally. Output: **8 s · 720x1280 (portrait)**, 30 fps, H.264.

## Requirements

- Node.js 22+ and FFmpeg on PATH (`npx hyperframes@0.8.136 doctor` checks both; Chrome is fetched automatically if missing).
- No API key. Everything renders locally.

## Workflow

1. **Brief.** Get the exact quote (≤ 14 words works best), the one word to highlight (copy it exactly as it appears, including punctuation), and the speaker's name + role. Only use real quotes with permission; label invented examples as fictional.
2. **Project.** Copy this skill's `template/` folder to `./videos/<slug>/` (keep `index.html`, `hyperframes.json`, `package.json`).
3. **Variables.** Write `./videos/<slug>/brief.json` with these keys: `quote, highlight, author, role, accent, bg, ink`.
   Start from an example in `examples/` (`customers-remember.json`, `ship-today.json`).
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

- `highlight` must match one word of the quote exactly (case-insensitive, punctuation included).
- Light `bg` + dark `ink` or the reverse — keep contrast high for small phone screens.
- Word timing adapts to quote length automatically.

## Credits

Rendering engine: [HyperFrames](https://github.com/heygen-com/hyperframes) by HeyGen, Apache-2.0 — this skill
only ships its own template and instructions and calls the published `hyperframes` CLI. See `NOTICE`.
