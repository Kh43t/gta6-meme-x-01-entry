#!/usr/bin/env python3
"""Build the gta6-meme-x-01 meme: AI scene + make.fun ghost + GTA captions.

Reads scene2.jpg (Pollinations) and assets-mark.png (make.fun press kit),
writes meme.png (1024x1024). Run from the entry repo root.
"""
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIZE = 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def cover(img, size):
    """Resize so the image covers a square, then centre-crop."""
    w, h = img.size
    scale = max(size / w, size / h)
    img = img.resize((round(w * scale), round(h * scale)), Image.LANCZOS)
    left = (img.width - size) // 2
    top = (img.height - size) // 2
    return img.crop((left, top, left + size, top + size))


def outlined(draw, centre_x, y, text, font, fill, stroke, stroke_width):
    """Draw centred text with a thick outline, return its bottom edge."""
    box = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    width = box[2] - box[0]
    draw.text(
        (centre_x - width / 2 - box[0], y),
        text,
        font=font,
        fill=fill,
        stroke_width=stroke_width,
        stroke_fill=stroke,
    )
    return y + (box[3] - box[1])


def main():
    scene = Image.open(os.path.join(HERE, "scene2.jpg")).convert("RGB")
    canvas = cover(scene, SIZE)

    # Gentle darkening at the very top and bottom so captions stay readable.
    shade = Image.new("L", (SIZE, SIZE), 0)
    sh = ImageDraw.Draw(shade)
    sh.rectangle((0, 0, SIZE, 260), fill=70)
    sh.rectangle((0, SIZE - 190, SIZE, SIZE), fill=80)
    shade = shade.filter(ImageFilter.GaussianBlur(90))
    canvas.paste(Image.new("RGB", (SIZE, SIZE), (0, 0, 0)), (0, 0), shade)

    draw = ImageDraw.Draw(canvas)

    # The joke, GTA death-screen style, big across the sky.
    wasted = ImageFont.truetype(BOLD, 178)
    outlined(draw, SIZE // 2, 34, "WASTED", wasted, "white", "black", 10)

    # make.fun's ghost, standing on the street beside the fallen player,
    # holding its magenta star coin. Real press-kit mark, not a redraw.
    ghost = Image.open(os.path.join(HERE, "assets-mark.png")).convert("RGBA")
    ghost_size = 296
    ghost = ghost.resize((ghost_size, ghost_size), Image.LANCZOS)
    gx, gy = 712, 496
    shadow = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.ellipse((gx + 18, gy + ghost_size - 26, gx + ghost_size - 18, gy + ghost_size + 6), fill=(0, 0, 0, 110))
    shadow = shadow.filter(ImageFilter.GaussianBlur(10))
    canvas.paste(Image.alpha_composite(canvas.convert("RGBA"), shadow).convert("RGB"), (0, 0))
    draw = ImageDraw.Draw(canvas)
    canvas.paste(ghost, (gx, gy), ghost)

    # The brand name under the ghost, so the logo reads even at 480 px.
    brand = ImageFont.truetype(BOLD, 42)
    outlined(draw, gx + ghost_size // 2, gy + ghost_size + 8, "make.fun", brand, "white", "black", 5)

    # The punchline along the bottom.
    punch = ImageFont.truetype(BOLD, 64)
    outlined(draw, SIZE // 2, SIZE - 108, "13 YEARS OF WAITING", punch, "white", "black", 6)

    canvas.save(os.path.join(HERE, "meme.png"), "PNG")
    print("wrote meme.png", canvas.size)


if __name__ == "__main__":
    main()
