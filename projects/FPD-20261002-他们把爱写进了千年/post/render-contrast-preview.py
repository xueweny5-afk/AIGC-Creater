from pathlib import Path
import math
import subprocess
import wave

import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "post" / "contrast-preview"
OUT.mkdir(parents=True, exist_ok=True)
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
FONT = "C:/Windows/Fonts/NotoSerifSC-VF.ttf"
SANS = "C:/Windows/Fonts/NotoSansSC-VF.ttf"

PAIRS = [
    ("F01-li-zhao", "李清照 × 赵明诚", "相对展玩，校书至夜", "后来，书还在，人不在", "据《金石录后序》"),
    ("F02-su-wang", "苏轼 × 王弗", "她记得，他忘记的书", "十年生死两茫茫", "据《亡妻王氏墓志铭》《江城子》"),
    ("F03-lu-tang", "陆游 × 唐琬", "春色里，曾有两人", "山盟虽在，锦书难托", "据陆游《钗头凤》"),
    ("F04-shen-chen", "沈复 × 陈芸", "布衣菜饭，可乐终身", "后来，桌上只剩一只空碗", "据《浮生六记》"),
]


def cover(image, size):
    w, h = image.size
    tw, th = size
    ratio = tw / th
    if w / h > ratio:
        crop_w = round(h * ratio)
        left = (w - crop_w) // 2
        image = image.crop((left, 0, left + crop_w, h))
    else:
        crop_h = round(w / ratio)
        top = (h - crop_h) // 2
        image = image.crop((0, top, w, top + crop_h))
    return image.resize(size, Image.Resampling.LANCZOS)


def centered(draw, y, text, font, fill):
    box = draw.textbbox((0, 0), text, font=font)
    draw.text(((1080 - (box[2] - box[0])) / 2, y), text, font=font, fill=fill)


def card(index, pair, after):
    frame_id, names, warm, lonely, source = pair
    image = Image.open(ROOT / "storyboard" / "frames" / frame_id / "v1.png").convert("RGB")
    half = image.height // 2
    panel = image.crop((0, half + 5, image.width, image.height)) if after else image.crop((0, 0, image.width, half - 5))
    panel = cover(panel, (1080, 1080))
    canvas = Image.new("RGB", (1080, 1920), "#0c1018")
    canvas.paste(panel, (0, 330))
    draw = ImageDraw.Draw(canvas)
    title_font = ImageFont.truetype(FONT, 57)
    name_font = ImageFont.truetype(SANS, 35)
    line_font = ImageFont.truetype(FONT, 56)
    source_font = ImageFont.truetype(SANS, 28)
    centered(draw, 62, "他们把爱，写进了千年", title_font, "#f4eadb")
    centered(draw, 211, names, name_font, "#c8cbd0")
    centered(draw, 1502, lonely if after else warm, line_font, "#f6ecdd")
    centered(draw, 1770, source, source_font, "#9ba0aa")
    path = OUT / f"shot-{index + 1:02d}-{'after' if after else 'before'}.png"
    canvas.save(path)
    return path


def score():
    rate, duration = 48000, 24
    t = np.arange(rate * duration, dtype=np.float64) / rate
    sound = np.zeros_like(t)
    chords = [(146.83, 174.61, 220.0), (130.81, 164.81, 196.0),
              (146.83, 196.0, 233.08), (130.81, 174.61, 220.0)]
    for section, chord in enumerate(chords):
        start = section * 6
        local = t - start
        active = (local >= 0) & (local < 6)
        gate = np.zeros_like(t)
        gate[active] = np.minimum(local[active] / 0.65, 1) * np.minimum((6 - local[active]) / 0.5, 1)
        for note in chord:
            sound += 0.044 * gate * np.sin(2 * math.pi * note * t)
        after = (local >= 3) & (local < 6)
        sound[after] += 0.05 * np.sin(2 * math.pi * chord[0] / 2 * t[after])
        cut = (local >= 3) & (local < 3.25)
        sound[cut] *= 0.06
    sound *= np.minimum(t / 0.6, 1) * np.minimum((duration - t) / 0.8, 1)
    path = OUT / "contrast-score.wav"
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(rate)
        wav.writeframes((np.clip(sound, -1, 1) * 32767).astype("<i2").tobytes())
    return path


def render(cards, audio):
    clips = []
    for i, still in enumerate(cards):
        clip = OUT / f"shot-{i + 1:02d}.mp4"
        filters = "zoompan=z='min(zoom+0.00005,1.005)':d=1:s=1080x1920:fps=30"
        if i == 0:
            filters += ",fade=t=in:st=0:d=0.15"
        if i == len(cards) - 1:
            filters += ",fade=t=out:st=2.75:d=0.25"
        subprocess.run([
            FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-loop", "1", "-framerate", "30", "-i", str(still),
            "-vf", filters, "-t", "3", "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p", str(clip)
        ], check=True)
        clips.append(clip)
    manifest = OUT / "concat.txt"
    manifest.write_text("".join(f"file '{p.as_posix()}'\n" for p in clips), encoding="utf-8")
    target = ROOT / "delivery" / "他们把爱写进了千年-前后反差预演-v2.mp4"
    subprocess.run([
        FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(manifest),
        "-i", str(audio), "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(target)
    ], check=True)
    return target


if __name__ == "__main__":
    shots = [card(i, pair, after) for i, pair in enumerate(PAIRS) for after in (False, True)]
    print(render(shots, score()))
