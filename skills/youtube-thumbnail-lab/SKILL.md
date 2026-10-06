---
name: youtube-thumbnail-lab
description: Design click-worthy YouTube / Bilibili thumbnails (1280x720) from a video title — writes 3 concept directions (face+reaction, object+text, before/after), generates the chosen ones with GPT Image via any OpenAI-compatible API, and checks readability at small size. Use for YouTube thumbnail, B站封面, video cover, thumbnail A/B test.
license: MIT
metadata:
  author: SkillHub
  version: 1.0.0
---

# YouTube Thumbnail Lab

## Inputs

- Video title and a one-line summary of the payoff.
- Channel look: colors, recurring elements, whether the creator's face is used (if yes, ask for a
  reference photo and use an edit-capable endpoint; never invent a real person's likeness).
- 2–4 words of thumbnail text (NOT the title).

## Workflow

1. Write three concepts with `templates/concepts.md`: **A** emotion (character/face + big reaction),
   **B** object (hero object + 2–3 word text), **C** contrast (split before/after). Recommend one.
2. Fill `templates/prompt-template.md` for the chosen concept(s) → `thumbs/<slug>-A.prompt.txt`.
3. Generate (landscape) and crop to 1280x720:
   ```bash
   python3 scripts/generate.py --prompt-file thumbs/<slug>-A.prompt.txt --size 1536x1024 --quality medium --out thumbs/<slug>-A-raw.png
   python3 scripts/crop.py thumbs/<slug>-A-raw.png thumbs/<slug>-A.jpg 1280x720
   ```
4. Readability check: downscale to 320x180 (`crop.py ... 320x180`) and look — can you read the text
   and tell the subject in one second? If not, simplify and regenerate.
5. Keep the bottom-right 20% free of important content (YouTube puts the duration there).

## Rules

- ≤ 4 words of text, ultra-bold, high contrast, with outline or shadow.
- One focal point, saturated colors, no clutter, no clickbait that the video doesn't deliver.

## Environment

`OPENAI_API_KEY` (required), `OPENAI_BASE_URL`, `IMAGE_MODEL` (default `gpt-image-2`). Crops need Pillow.
