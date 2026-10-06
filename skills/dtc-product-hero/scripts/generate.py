#!/usr/bin/env python3
"""SkillHub image generator — calls any OpenAI-compatible Images API (GPT Image).

Standard library only. Usage:
  python3 scripts/generate.py --prompt-file brief/prompt.txt --size 1536x1024 \
      --quality medium --out output/cover.png [--n 2] [--model gpt-image-2]

Environment (bring your own key):
  OPENAI_API_KEY   (or IMAGE_API_KEY)  API key — required
  OPENAI_BASE_URL  (or IMAGE_BASE_URL) default https://api.openai.com/v1
                   any OpenAI-compatible gateway works, e.g. https://tryallapi.com/v1
  IMAGE_MODEL      default gpt-image-2 (gpt-image-1.5 / gpt-image-1 also work)
"""
import argparse, base64, json, os, pathlib, sys, time, urllib.request, urllib.error


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--prompt', help='prompt text')
    ap.add_argument('--prompt-file', help='file containing the prompt')
    ap.add_argument('--size', default='1024x1024', help='1024x1024 | 1536x1024 | 1024x1536 | auto')
    ap.add_argument('--quality', default='medium', help='low | medium | high | auto')
    ap.add_argument('--n', type=int, default=1)
    ap.add_argument('--model', default=os.environ.get('IMAGE_MODEL', 'gpt-image-2'))
    ap.add_argument('--out', required=True, help='output path (.png); -1, -2 suffixes added when n > 1')
    a = ap.parse_args()

    prompt = a.prompt or (pathlib.Path(a.prompt_file).read_text(encoding='utf-8') if a.prompt_file else None)
    if not prompt:
        sys.exit('error: pass --prompt or --prompt-file')
    key = os.environ.get('OPENAI_API_KEY') or os.environ.get('IMAGE_API_KEY')
    if not key:
        sys.exit('error: set OPENAI_API_KEY (or IMAGE_API_KEY)')
    base = (os.environ.get('OPENAI_BASE_URL') or os.environ.get('IMAGE_BASE_URL') or 'https://api.openai.com/v1').rstrip('/')

    body = json.dumps({'model': a.model, 'prompt': prompt.strip(), 'size': a.size,
                       'quality': a.quality, 'n': a.n}).encode()
    req = urllib.request.Request(base + '/images/generations', data=body, method='POST',
                                 headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f'error: HTTP {e.code}: {e.read().decode(errors="ignore")[:500]}')

    out = pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    paths = []
    for i, item in enumerate(data.get('data', [])):
        p = out if a.n == 1 else out.with_name(f'{out.stem}-{i + 1}{out.suffix}')
        if item.get('b64_json'):
            p.write_bytes(base64.b64decode(item['b64_json']))
        elif item.get('url'):
            urllib.request.urlretrieve(item['url'], p)
        else:
            continue
        paths.append(str(p))
    if not paths:
        sys.exit('error: no image in response: ' + json.dumps(data)[:500])
    print(json.dumps({'model': a.model, 'size': a.size, 'quality': a.quality, 'files': paths,
                      'usage': data.get('usage'), 'seconds': round(time.time() - t0, 1)}))


if __name__ == '__main__':
    main()
