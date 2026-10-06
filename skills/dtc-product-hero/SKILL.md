---
name: dtc-product-hero
description: Generate premium studio "hero" product images for DTC landing pages, Shopify headers and ad creatives with GPT Image via any OpenAI-compatible API — consistent lighting recipe, brand-colored set, room for headline copy. Use for product hero shot, landing page hero image, Shopify banner, 产品主视觉, 首屏图, ad creative background.
license: MIT
metadata:
  author: SkillHub
  version: 1.0.0
---

# DTC Product Hero

Landing-page heroes need three things marketplace photos don't: a mood, a brand-colored set, and
empty space for the headline. This skill writes the photo brief like an art director, then generates.

## Inputs

1. Product: what it is, material, finish, colors, size cues (e.g. "fits in one hand").
2. Brand palette (2–3 hex) and mood words.
3. Where the copy goes: `left`, `right` or `top` (default `left`).
4. Optional reference photo of the real product. If the user has one, prefer
   `/images/edits` with that photo (same script supports any edit-capable gateway) and say so;
   otherwise generate a concept hero and label it as a concept render.

## Workflow

1. Pick a lighting recipe from `templates/lighting-recipes.md` that matches the mood.
2. Fill `templates/prompt-template.md` → `hero/<slug>.prompt.txt`.
3. Generate square for ads or landscape for web heroes:
   ```bash
   python3 scripts/generate.py --prompt-file hero/<slug>.prompt.txt --size 1536x1024 --quality medium --out hero/<slug>.png
   ```
4. Check: product shape plausible, no text or fake logos, copy-side really empty, shadows coherent.
5. Deliver crops as needed: 1920x1080 web hero, 1080x1080 ad, 1200x628 link ad
   (`python3 scripts/crop.py hero/<slug>.png hero/<slug>-1080.jpg 1080x1080 --anchor right`).

## Rules

- Never put text, prices or badges in the image — copy is added in HTML/ad tool.
- One product, one hero angle (3/4 view by default), realistic materials.
- Mark generated images of real products as concept renders until checked against the product.

## Environment

`OPENAI_API_KEY` (required), `OPENAI_BASE_URL`, `IMAGE_MODEL` (default `gpt-image-2`).
