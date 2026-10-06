---
name: carousel-slide-kit
description: Turn a tip list, thread or article into a matching set of Instagram / LinkedIn / 小红书 carousel slides (portrait) with a locked visual system, generated with GPT Image via any OpenAI-compatible API. Use for carousel posts, swipe posts, 轮播图, 图文笔记, LinkedIn document posts, tips-list graphics.
license: MIT
metadata:
  author: SkillHub
  version: 1.0.0
---

# Carousel Slide Kit

A carousel works when every slide clearly belongs to the same set. This skill writes a short
**style lock** once and prepends it to every slide prompt, then generates slide by slide.

## Inputs

- Source: the list/thread/article, or a topic to outline.
- Handle or brand name for the footer, 2–3 brand colors, language (EN / 中文).
- Slide count (default 5: cover, 3 content, CTA). Max 10.

## Workflow

1. Outline: cover hook (≤ 6 words), one idea per content slide (title ≤ 6 words + ≤ 18-word line),
   CTA slide. Show the outline and get a quick OK.
2. Write `carousel/style-lock.txt` from `templates/style-lock.md` (palette, type, layout grid,
   recurring motif, footer text, slide-number position).
3. For each slide, write `carousel/NN.prompt.txt` = style lock + slide content from
   `templates/slide-prompt.md`, then:
   ```bash
   python3 scripts/generate.py --prompt-file carousel/01.prompt.txt --size 1024x1536 --quality medium --out carousel/01.png
   ```
4. Review all slides side by side: same palette, same type, numbering correct, text spelled right.
   Regenerate only the slides that drift.
5. Instagram wants 4:5 → `python3 scripts/crop.py carousel/01.png carousel/01-ig.jpg 1080x1350`.

## Rules

- Max ~25 words of rendered text per slide; long text belongs in the caption.
- Text in quotes in the prompt, exactly as it should appear.
- Same footer and slide-number style on every slide.

## Environment

`OPENAI_API_KEY` (required), `OPENAI_BASE_URL`, `IMAGE_MODEL` (default `gpt-image-2`).
