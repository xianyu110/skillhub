---
name: brand-og-card
description: Create on-brand Open Graph / social share cards (1200x630) for a product, blog post or launch page with GPT Image via any OpenAI-compatible API. Locks brand colors, wordmark and headline, then crops to exact OG size. Use for og:image, Twitter/X card, LinkedIn share image, link preview, 分享卡片, OG 图.
license: MIT
metadata:
  author: SkillHub
  version: 1.0.0
---

# Brand OG Card

Produce a share card that looks like it came from the brand's own design team: one headline,
one visual idea, brand colors, wordmark — and nothing else.

## Inputs to collect (ask once, in one message)

1. **Brand**: name (as it should appear), 2–3 hex colors, mood words (e.g. "calm, premium").
2. **Page**: what the link is (home page, blog post, launch, pricing) and its headline (≤ 7 words).
3. **Visual idea** (optional): an object or metaphor. If missing, propose two and pick the simpler.
4. **Output path**: default `./og/<page-slug>.png`.

## Workflow

1. Copy `templates/prompt-template.md`, fill every `{{slot}}`, save as `og/<slug>.prompt.txt`.
   Keep the headline verbatim and in quotes — the model renders quoted text most reliably.
2. Generate (1536x1024 is the closest native landscape size):
   ```bash
   python3 scripts/generate.py --prompt-file og/<slug>.prompt.txt --size 1536x1024 --quality medium --out og/<slug>-raw.png
   ```
3. Inspect the image. Reject and regenerate (max 2 retries) if: headline is misspelled, extra
   text appeared, the wordmark is wrong, or the subject touches the edges.
4. Crop to the exact OG size, keeping text safe:
   ```bash
   python3 scripts/crop.py og/<slug>-raw.png og/<slug>.png 1200x630
   ```
5. Wire it up (if a web project is open): `<meta property="og:image" content="/og/<slug>.png">`,
   `og:image:width=1200`, `og:image:height=630`, `twitter:card=summary_large_image`.

## Rules

- One headline, one wordmark. No URLs, no buttons, no fake UI unless asked.
- Keep the left 55% for text and the right 45% for the visual (or centered for minimal brands).
- 64px+ safe margin at 1200x630 — X and LinkedIn crop edges on mobile.
- Never invent a logo for a real company; use the wordmark text only.

## Environment

`OPENAI_API_KEY` (required), `OPENAI_BASE_URL` (default OpenAI; any OpenAI-compatible gateway),
`IMAGE_MODEL` (default `gpt-image-2`). Cost: roughly $0.04 per medium 1536x1024 image.
`crop.py` needs `pip install pillow`.
