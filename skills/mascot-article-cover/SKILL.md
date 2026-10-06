---
name: mascot-article-cover
description: Generate blog / newsletter / WeChat article covers that all feature the SAME mascot character in a consistent illustration style, via GPT Image on any OpenAI-compatible API. Keeps a character bible so every cover in a series matches. Use for article cover, 公众号封面, 头图, newsletter header, series artwork, brand mascot illustrations.
license: MIT
metadata:
  author: SkillHub
  version: 1.0.0
---

# Mascot Article Cover

A series of covers is recognisable when the same character shows up every time. This skill keeps
a written **character bible** and reuses it verbatim in every prompt, so the mascot stays on-model.

## First run: create the character bible

If `covers/character.md` does not exist, create it from `templates/character-bible.md`:
species/shape, 3 fixed colors (hex), clothing/accessory, line style, rendering style, and two
"never" rules (e.g. never shows teeth, never more than one character). Show it to the user and
confirm before generating. Reuse an existing bible without asking.

## Per article

1. Read the article (file, URL text, or pasted). Extract: the core idea in ≤ 6 words, and one
   concrete scene the mascot can act out (a metaphor, not a literal screenshot).
2. Fill `templates/cover-prompt.md` → `covers/<slug>.prompt.txt`. Paste the whole bible
   section verbatim into it. Title text is optional — default to **no text** (platforms overlay titles).
3. Generate:
   ```bash
   python3 scripts/generate.py --prompt-file covers/<slug>.prompt.txt --size 1536x1024 --quality medium --out covers/<slug>.png
   ```
4. Check the mascot against the bible (colors, accessory, proportions). Regenerate once if off-model.
5. Optional crops: WeChat 900x383 (`python3 scripts/crop.py covers/<slug>.png covers/<slug>-wechat.jpg 900x383`),
   Substack/Ghost 1200x630.

## Rules

- Same bible text every time — do not paraphrase it between covers.
- One mascot, one scene, plain or softly textured background, lots of negative space.
- The scene must be readable at thumbnail size (200px wide).

## Environment

`OPENAI_API_KEY` (required), `OPENAI_BASE_URL` (optional, OpenAI-compatible), `IMAGE_MODEL`
(default `gpt-image-2`). Crops need `pip install pillow`.
