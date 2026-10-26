from pathlib import Path
import math
import subprocess
import wave

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "post" / "preview"
OUT.mkdir(parents=True, exist_ok=True)
FONT = "C:/Windows/Fonts/NotoSerifSC-VF.ttf"
SANS = "C:/Windows/Fonts/NotoSansSC-VF.ttf"
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

SEGMENTS = [
    ("F01-li-zhao", "李清照 × 赵明诚", "相对展玩，校书至夜", "后来，书还在，人不在", "据《金石录后序》"),
    ("F02-su-wang", "苏轼 × 王弗", "她记得，他忘记的书", "十年生死两茫茫", "据《亡妻王氏墓志铭》《江城子》"),
    ("F03-lu-tang", "陆游 × 唐琬", "春色里，曾有两人", "山盟虽在，锦书难托", "据陆游《钗头凤》"),
    ("F04-shen-chen", "沈复 × 陈芸", "布衣菜饭，可乐终身", "后来，桌上只剩一只空碗", "据《浮生六记》"),
]


def fit_panel(image):
    width, height = image.size
    target_ratio = 1080 / 810
    if width / height > target_ratio:
        new_width = round(height * target_ratio)
        left = (width - new_width) // 2
        image = image.crop((left, 0, left + new_width, height))
    else:
        new_height = round(width / target_ratio)
        top = (height - new_height) // 2
        image = image.crop((0, top, width, top + new_height))
    return image.resize((1080, 810), Image.Resampling.LANCZOS)


def draw_center(draw, y, string, font, color):
    left, top, right, bottom = draw.textbbox((0, 0), string, font=font)
    draw.text(((1080 - (right - left)) / 2, y), string, font=font, fill=color)


def make_card(index, item):
    frame_id, names, upper_caption, lower_caption, source = item
    src = Image.open(ROOT / "storyboard" / "frames" / frame_id / "v1.png").convert("RGB")
    split = src.height // 2
    top = fit_panel(src.crop((0, 0, src.width, split - 5)))
    bottom = fit_panel(src.crop((0, split + 5, src.width, src.height)))
    card = Image.new("RGB", (1080, 1920), (11, 13, 18))
    card.paste(top, (0, 150))
    card.paste(bottom, (0, 978))

    overlay = Image.new("RGBA", card.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 836, 1080, 960), fill=(3, 7, 12, 150))
    od.rectangle((0, 1664, 1080, 1788), fill=(3, 7, 12, 150))
    card = Image.alpha_composite(card.convert("RGBA"), overlay)
    draw = ImageDraw.Draw(card)
    title_font = ImageFont.truetype(FONT, 57)
    caption_font = ImageFont.truetype(FONT, 48)
    small_font = ImageFont.truetype(SANS, 29)
    source_font = ImageFont.truetype(SANS, 25)
    draw_center(draw, 49, "他们把爱，写进了千年", title_font, "#f4eadb")
    draw.text((38, 187), names, font=small_font, fill="#fff5e8", stroke_width=2, stroke_fill="#182029")
    draw_center(draw, 858, upper_caption, caption_font, "#fff7e9")
    draw.text((38, 1015), "后来", font=small_font, fill="#fff5e8", stroke_width=2, stroke_fill="#182029")
    draw_center(draw, 1686, lower_caption, caption_font, "#fff7e9")
    draw_center(draw, 1831, source, source_font, "#a9acb4")
    p = OUT / f"card-{index + 1:02d}.png"
    card.convert("RGB").save(p)
    return p


def make_audio():
    rate = 48000
    seconds = 24
    t = np.arange(rate * seconds, dtype=np.float64) / rate
    audio = np.zeros_like(t)
    chords = [(146.83, 174.61, 220.0), (130.81, 164.81, 196.0),
              (146.83, 196.0, 233.08), (130.81, 174.61, 220.0)]
    for section, chord in enumerate(chords):
        start = section * 6
        local = t - start
        active = (local >= 0) & (local < 6)
        env = np.zeros_like(t)
        env[active] = np.minimum(local[active] / 1.2, 1) * np.minimum((6 - local[active]) / 1.2, 1)
        for note in chord:
            audio += 0.018 * env * np.sin(2 * math.pi * note * t)
        bell_env = np.zeros_like(t)
        bell_env[active] = np.exp(-1.6 * local[active])
        audio += 0.027 * bell_env * np.sin(2 * math.pi * chord[1] * 2 * t)
    audio *= 4 * np.minimum(t / 0.8, 1) * np.minimum((seconds - t) / 1.2, 1)
    p = OUT / "preview-score.wav"
    with wave.open(str(p), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(rate)
        wav.writeframes((np.clip(audio, -1, 1) * 32767).astype("<i2").tobytes())
    return p


def render(cards, audio):
    clips = []
    for i, card in enumerate(cards):
        clip = OUT / f"segment-{i + 1:02d}.mp4"
        subprocess.run([
            FFMPEG, "-hide_banner", "-loglevel", "error", "-y",
            "-loop", "1", "-framerate", "30", "-i", str(card),
            "-vf", "zoompan=z='min(zoom+0.000035,1.007)':d=1:s=1080x1920:fps=30,fade=t=in:st=0:d=0.2,fade=t=out:st=5.8:d=0.2",
            "-t", "6", "-c:v", "libx264", "-preset", "veryfast", "-crf", "22", "-pix_fmt", "yuv420p", str(clip)
        ], check=True)
        clips.append(clip)
    manifest = OUT / "concat.txt"
    manifest.write_text("".join(f"file '{p.as_posix()}'\n" for p in clips), encoding="utf-8")
    target = ROOT / "delivery" / "他们把爱写进了千年-动态预演-v1.mp4"
    target.parent.mkdir(exist_ok=True)
    subprocess.run([
        FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0",
        "-i", str(manifest), "-i", str(audio), "-c:v", "copy", "-c:a", "aac",
        "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(target)
    ], check=True)
    return target


if __name__ == "__main__":
    cards = [make_card(i, item) for i, item in enumerate(SEGMENTS)]
    audio = make_audio()
    print(render(cards, audio))
