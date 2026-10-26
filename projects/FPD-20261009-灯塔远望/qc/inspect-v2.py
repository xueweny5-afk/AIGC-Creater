"""Decode every frame and build a compact visual review sheet for UNIT01."""

from pathlib import Path
import hashlib
import json

import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
VIDEO = ROOT / "generation/灯塔远望-运镜版-v2.mp4"
SHEET = ROOT / "qc/六帧检查-v2.jpg"
RESULT = ROOT / "qc/decode-v2.json"
selected = {0, 36, 72, 108, 156, 191}
reader = imageio_ffmpeg.read_frames(str(VIDEO), pix_fmt="rgb24")
meta = next(reader)
width, height = meta["size"]
count = 0
last = None
differences = []
frames = {}
for raw in reader:
    array = np.frombuffer(raw, dtype=np.uint8).reshape(height, width, 3)
    if last is not None:
        differences.append(float(np.abs(array.astype(np.int16) - last).mean()))
    if count in selected:
        frames[count] = Image.fromarray(array.copy())
    last = array.astype(np.int16)
    count += 1

sheet = Image.new("RGB", (width * 3 // 2, height), "#101820")
draw = ImageDraw.Draw(sheet)
for slot, index in enumerate(sorted(frames)):
    thumb = frames[index].resize((width // 2, height // 2), Image.Resampling.LANCZOS)
    x = slot % 3 * (width // 2)
    y = slot // 3 * (height // 2)
    sheet.paste(thumb, (x, y))
    draw.text((x + 8, y + 8), f"{index / 24:.2f}s", fill="white", stroke_width=2, stroke_fill="black")
sheet.save(SHEET, quality=92)

result = {
    "file": str(VIDEO),
    "sha256": hashlib.sha256(VIDEO.read_bytes()).hexdigest(),
    "bytes": VIDEO.stat().st_size,
    "metadata": meta,
    "decoded_frames": count,
    "frame_step_mean_abs_min": min(differences),
    "frame_step_mean_abs_max": max(differences),
    "frame_step_mean_abs_average": sum(differences) / len(differences),
    "sample_indices": sorted(frames),
}
RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
