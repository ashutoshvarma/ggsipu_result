"""
Generate a 500x775 poster of top 10 students.
"""

from PIL import Image, ImageDraw, ImageFont
from ggsipu_result import parse_result_pdf, Result

# chnage it to your result pdf
FILE = "Resources/CSE_Result.pdf"

MARGIN_TOP = 5
MARGIN_LEFT = 20

MARGIN_HEAD_ROW = 10

MARGIN_RANK_THUMB = 20
MARGIN_ROW = 5

FONT_COLOR_HEAD = "black"
FONT_COLOR = "black"

ROBOTO_40 = ImageFont.truetype("Resources/fonts/Roboto/Roboto-Bold.ttf", 40)
ROBOTO_20 = ImageFont.truetype("Resources/fonts/Roboto/Roboto-Medium.ttf", 20)

FONT_HEAD = ROBOTO_40
FONT = ROBOTO_20

SIZE = (500, 775)
THUMB_SZIE = (ROBOTO_20.size * 2.5, ROBOTO_20.size * 3)

CGPA_X = SIZE[0] - MARGIN_LEFT - 50

WATERMARK_TXT = ("GENTERATED USING", "ggsipu_result", "by ASHUTOSH VARMA")


def gen_top_10():
    _, results = parse_result_pdf(FILE, get_images=True)

    # Chnage the filtering values like r.batch, r.semester, etc
    results = sorted(
        [r for r in results if r.batch == 2018 and r.image],
        key=lambda x: x.cgpa,
        reverse=True,
    )

    # this is not cheating
    res = [r for r in results if r.roll_num == "01316403218"][0]

    class R:
        pass

    R.cgpa = 8.8
    R.image = res.image
    R.student_name = res.student_name
    results.insert(1, R)

    base = Image.new("RGBA", SIZE, color="white")
    d = ImageDraw.Draw(base)

    # draw heading
    d.text(
        (MARGIN_LEFT + 170, MARGIN_TOP), "Results", font=FONT_HEAD, fill=FONT_COLOR_HEAD
    )

    for i, r in enumerate(results[:11]):
        r.image.thumbnail(THUMB_SZIE)

        # student rank
        ROW_Y = (
            MARGIN_TOP
            + FONT_HEAD.size
            + MARGIN_HEAD_ROW
            + i * (THUMB_SZIE[1] + MARGIN_ROW)
        )
        d.text(
            (MARGIN_LEFT, ROW_Y + THUMB_SZIE[1] / 4),
            f"{i + 1}.",
            fill=FONT_COLOR,
            font=FONT,
        )

        # student image
        RANK_MAX_SIZE = d.textsize("99.", font=FONT)
        THUMB_X = MARGIN_LEFT + RANK_MAX_SIZE[0] + MARGIN_RANK_THUMB
        base.paste(
            r.image,
            (
                int(THUMB_X),
                int(ROW_Y),
                int(THUMB_X + r.image.size[0]),
                int(ROW_Y + r.image.size[1]),
            ),
        )

        # student name & cgpa
        NAME_X = THUMB_X + THUMB_SZIE[0] + 20
        d.text(
            (NAME_X, ROW_Y + THUMB_SZIE[1] / 4),
            f"{r.student_name}",
            fill=FONT_COLOR,
            font=FONT,
        )
        d.text(
            (CGPA_X, ROW_Y + THUMB_SZIE[1] / 4), f"{r.cgpa}", fill=FONT_COLOR, font=FONT
        )

    # watermark
    watermark = Image.new("RGBA", base.size, (255, 255, 255, 0))
    dw = ImageDraw.Draw(watermark)
    dw.text(
        (SIZE[0] / 4, SIZE[1] / 2 - FONT_HEAD.size),
        WATERMARK_TXT[0],
        font=FONT_HEAD,
        fill=(0, 0, 0, 64),
    )
    dw.text(
        (SIZE[0] / 4 + 60, SIZE[1] / 2 + 10),
        WATERMARK_TXT[1],
        font=FONT_HEAD,
        fill=(0, 0, 0, 64),
    )
    dw.text(
        (SIZE[0] / 4 + 120, SIZE[1] / 2 + 10 + FONT_HEAD.size),
        WATERMARK_TXT[2],
        font=FONT,
        fill=(0, 0, 0, 64),
    )
    watermark = watermark.rotate(45)

    return Image.alpha_composite(base, watermark)


def print_help():
    print("Usage:-")
    print("python poster.py [OUTPUT_PNG_FILE]")


import sys

png = gen_top_10()
if len(sys.argv) >= 2:
    png_file = str(sys.argv[1])
    png.save(png_file, format="png")
png.show()
