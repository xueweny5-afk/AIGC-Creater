from pathlib import Path
import subprocess

import cv2
import imageio_ffmpeg
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "storyboard/frames/F01-海岸灯塔/source-v1.png"
OUTPUT = ROOT / "generation/灯塔远望-运镜版-v1.mp4"
FPS = 24
DURATION = 8

image = cv2.imdecode(np.fromfile(str(SOURCE), dtype=np.uint8), cv2.IMREAD_COLOR)
if image is None:
    raise RuntimeError(f"Cannot read source image: {SOURCE}")
height, width = image.shape[:2]

command = [
    imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-f", "rawvideo", "-vcodec", "rawvideo",
    "-s", f"{width}x{height}", "-pix_fmt", "bgr24", "-r", str(FPS),
    "-i", "-", "-an", "-c:v", "libx264", "-preset", "medium",
    "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(OUTPUT),
]

with subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL,
                      stderr=subprocess.PIPE) as process:
    try:
        for frame_number in range(FPS * DURATION):
            t = frame_number / (FPS * DURATION - 1)
            ease = t * t * (3 - 2 * t)
            zoom = 1.0 + 0.15 * ease
            center_x = width * (0.5 + 0.08 * ease)
            center_y = height * (0.5 - 0.015 * ease)
            matrix = np.float32([
                [zoom, 0, width / 2 - zoom * center_x],
                [0, zoom, height / 2 - zoom * center_y],
            ])
            frame = cv2.warpAffine(image, matrix, (width, height),
                                   flags=cv2.INTER_CUBIC,
                                   borderMode=cv2.BORDER_REFLECT_101)
            process.stdin.write(frame.tobytes())
    finally:
        process.stdin.close()
    errors = process.stderr.read().decode("utf-8", errors="replace")
    if process.wait() != 0:
        raise RuntimeError(errors[-2000:])

print(OUTPUT)
