#!/usr/bin/env python3
"""Generate Open Graph share cards for quran.nurtech.dev.

Creates:
  public/og/default.png        — shared 1200x630 brand card
  public/og/surah-{n}.png      — per-surah 1200x630 cards (Arabic + Russian name)

Design tokens mirror src/styles/design-tokens.css (--sys-accent #596575 on
light, slate family) rendered as a dark card for contrast on social feeds.

Requires: Pillow + libraqm (for Arabic shaping). Fonts:
  - /mnt/HC_Volume_106549717/.fonts/NotoNaskhArabic.ttf (Arabic)
  - scripts/../public/fonts/manrope-700.ttf (Cyrillic UI)

Usage (from repo root):  python3 scripts/gen-og.py
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_OG = os.path.join(ROOT, 'public', 'og')
INDEX = os.path.join(ROOT, 'data', 'quran', 'index.json')

AR_FONT = next(
    (p for p in (
        os.path.join(ROOT, 'scripts', 'fonts', 'NotoNaskhArabic.ttf'),
        '/mnt/HC_Volume_106549717/.fonts/NotoNaskhArabic.ttf',
        '/usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf',
        '/usr/share/fonts/truetype/amiri/Amiri-Regular.ttf',
    ) if os.path.exists(p)),
    None,
)
if not AR_FONT:
    sys.exit('Arabic font not found (Noto Naskh Arabic or Amiri TTF required for shaping)')
RU_FONT = os.path.join(ROOT, 'public', 'fonts', 'manrope-700.ttf')
BRAND = os.path.join(ROOT, 'public', 'brand-mark.png')

W, H = 1200, 630
# Brand-ish slate palette
BG_TOP = (63, 74, 88)      # #3f4a58
BG_BOT = (35, 42, 52)      # darker slate
ACCENT = (174, 184, 198)   # #aeb8c6
TEXT = (245, 247, 250)
MUTED = (207, 213, 222)

GOLD = (212, 175, 55)      # subtle accent for ornaments


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def vertical_gradient(size, top, bottom):
    w, h = size
    img = Image.new('RGB', size)
    for y in range(h):
        color = lerp(top, bottom, y / (h - 1))
        ImageDraw.Draw(img).line([(0, y), (w, y)], fill=color)
    return img


def draw_card(draw, font_ar, font_ar_big, font_ru, font_ru_small, font_meta,
              arabic_text, ru_name, ru_meaning, label, meta_text):
    # decorative rule
    draw.rounded_rectangle([60, 74, 220, 78], radius=2, fill=GOLD)
    draw.rounded_rectangle([60, 84, 96, 88], radius=2, fill=ACCENT)

    # top-left brand + site
    try:
        brand = Image.open(BRAND).convert('RGBA').resize((56, 56), Image.LANCZOS)
    except Exception:
        brand = None
    if brand:
        # paste handled by caller (needs base image); here just draw site text
        pass
    draw.text((76, 78), 'quran.nurtech.dev', font=font_meta, fill=MUTED)

    # Arabic surah name (big, centered)
    bbox = draw.textbbox((0, 0), arabic_text, font=font_ar_big)
    aw = bbox[2] - bbox[0]
    ax = (W - aw) / 2 - bbox[0]
    ay = 220
    draw.text((ax, ay), arabic_text, font=font_ar_big, fill=TEXT)

    # Russian name
    bbox = draw.textbbox((0, 0), ru_name, font=font_ru)
    rw = bbox[2] - bbox[0]
    rx = (W - rw) / 2 - bbox[0]
    draw.text((rx, 430), ru_name, font=font_ru, fill=ACCENT)

    # meaning
    if ru_meaning:
        bbox = draw.textbbox((0, 0), ru_meaning, font=font_ru_small)
        mw = bbox[2] - bbox[0]
        mx = (W - mw) / 2 - bbox[0]
        draw.text((mx, 492), ru_meaning, font=font_ru_small, fill=MUTED)

    # footer line
    draw.text((60, 556), label, font=font_meta, fill=MUTED)
    tb = draw.textbbox((0, 0), meta_text, font=font_meta)
    draw.text((W - 60 - (tb[2] - tb[0]), 556), meta_text, font=font_meta, fill=MUTED)


def make_card(arabic_text, ru_name, ru_meaning, label, meta_text, out_path, ar_size=150):
    base = vertical_gradient((W, H), BG_TOP, BG_BOT)
    draw = ImageDraw.Draw(base)
    font_ar = ImageFont.truetype(AR_FONT, ar_size)
    font_ar_big = ImageFont.truetype(AR_FONT, ar_size)
    font_ru = ImageFont.truetype(RU_FONT, 46)
    font_ru_small = ImageFont.truetype(RU_FONT, 30)
    font_meta = ImageFont.truetype(RU_FONT, 26)

    draw_card(draw, font_ar, font_ar_big, font_ru, font_ru_small, font_meta,
              arabic_text, ru_name, ru_meaning, label, meta_text)

    # brand mark top-left
    try:
        brand = Image.open(BRAND).convert('RGBA').resize((48, 48), Image.LANCZOS)
        base.paste(brand, (60, 60), brand)
    except Exception:
        pass

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    base.save(out_path, 'PNG', optimize=True)
    return os.path.getsize(out_path)


def main():
    index_path = INDEX
    if not os.path.exists(index_path):
        # fall back to generated public/data/index.json
        alt = os.path.join(ROOT, 'public', 'data', 'index.json')
        if os.path.exists(alt):
            index_path = alt
        else:
            sys.exit('surah index not found; run npm run data first')

    surahs = json.load(open(index_path, encoding='utf-8'))

    total = 0
    default = make_card(
        'ٱلْقُرْآن',
        'Коран онлайн',
        'Чтение, перевод, тафсир и аудио — 114 сур, 6236 аятов',
        'quran.nurtech.dev',
        'по-русски и по-арабски',
        os.path.join(PUBLIC_OG, 'default.png'),
        ar_size=170,
    )
    total += default
    print(f'default.png {default} bytes')

    for s in surahs:
        n = s['n']
        label = f'Сура {n} · {s["c"]} аятов'
        p = os.path.join(PUBLIC_OG, f'surah-{n}.png')
        size = make_card(
            s['na'],
            s['nr'],
            s['nm'],
            label,
            'quran.nurtech.dev',
            p,
        )
        total += size
        if n % 20 == 0 or n == 114:
            print(f'... {n}/114 done')

    print(f'TOTAL {total} bytes ({total/1024:.1f} KiB) for {len(surahs)+1} cards')


if __name__ == '__main__':
    main()
