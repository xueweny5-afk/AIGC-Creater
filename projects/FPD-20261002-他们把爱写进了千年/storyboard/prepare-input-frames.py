from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent
FRAME_IDS = ["F01-li-zhao", "F02-su-wang", "F03-lu-tang", "F04-shen-chen"]


def cover_square(image):
    w, h = image.size
    side = min(w, h)
    x = (w - side) // 2
    y = (h - side) // 2
    return image.crop((x, y, x + side, y + side)).resize((1080, 1080), Image.Resampling.LANCZOS)


for pair_index, frame_id in enumerate(FRAME_IDS):
    folder = ROOT / "frames" / frame_id
    source = Image.open(folder / "v1.png").convert("RGB")
    half = source.height // 2
    for after in (False, True):
        panel = source.crop((0, half + 5, source.width, source.height)) if after else source.crop((0, 0, source.width, half - 5))
        canvas = Image.new("RGB", (1080, 1920), "#0c1018")
        canvas.paste(cover_square(panel), (0, 330))
        shot_id = pair_index * 2 + (2 if after else 1)
        path = folder / f"S{shot_id:02d}-start-v1.png"
        canvas.save(path)
        print(path)
