"""Render SH01 as a bounded 2D camera move over the approved source plate."""

from pathlib import Path
import subprocess
import sys

import imageio_ffmpeg
import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "storyboard/frames/F01-海岸灯塔/source-v1.png"
END_FRAME = ROOT / "storyboard/frames/F01-海岸灯塔/end-v2.png"
OUTPUT = ROOT / "generation/灯塔远望-运镜版-v2.mp4"
FPS = 24
SECONDS = 8

plate = Image.open(SOURCE).convert("RGB")
width, height = plate.size
if (width, height) != (760, 950):
    raise RuntimeError(f"Unexpected source size: {width}x{height}")


def frame_at(second: float) -> Image.Image:
    progress = np.clip((second - 1.5) / 5.0, 0.0, 1.0)
    ease = progress * progress * (3.0 - 2.0 * progress)
    zoom = 1.0 + 0.55 * ease
    center_x = width / 2 + 120.0 * ease
    center_y = height / 2 - 17.0 * ease
    half_w, half_h = width / (2 * zoom), height / (2 * zoom)
    if center_x - half_w < 0 or center_x + half_w > width:
        raise RuntimeError("Crop exceeds source width")
    if center_y - half_h < 0 or center_y + half_h > height:
        raise RuntimeError("Crop exceeds source height")
    inverse = 1.0 / zoom
    return plate.transform(
        (width, height), Image.Transform.AFFINE,
        (inverse, 0, center_x - width * inverse / 2,
         0, inverse, center_y - height * inverse / 2),
        resample=Image.Resampling.BICUBIC,
    )


end_frame = frame_at(SECONDS)
end_frame.save(END_FRAME)
if "--frame-only" in sys.argv:
    print(END_FRAME)
    raise SystemExit(0)

command = [
    imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-f", "rawvideo", "-vcodec", "rawvideo",
    "-s", f"{width}x{height}", "-pix_fmt", "rgb24", "-r", str(FPS),
    "-i", "-", "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
    "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(OUTPUT),
]
with subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL,
                      stderr=subprocess.PIPE) as process:
    try:
        for index in range(FPS * SECONDS):
            process.stdin.write(frame_at(index / FPS).tobytes())
    finally:
        process.stdin.close()
    errors = process.stderr.read().decode("utf-8", errors="replace")
    if process.wait() != 0:
        raise RuntimeError(errors[-2000:])
print(OUTPUT)
