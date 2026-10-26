"""Local-only reference inspection; does not upload or alter source media."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageDraw, ImageChops, ImageStat
import subprocess
import hashlib
import json

SOURCE = Path(r'D:\project\qita\电影感\AIGC电影\香积寺之战1.mp4')
FFMPEG = Path(r'D:\.pnpm-store\v11\projects\1aef549a252559f54eddc325d9335d77\node_modules\@remotion\compositor-win32-x64-msvc\ffmpeg.exe')
ROOT = Path(__file__).resolve().parent
FRAMES = ROOT / 'sequence-frames'
SHEETS = ROOT / 'sequence-sheets'
FRAMES.mkdir(exist_ok=True)
SHEETS.mkdir(exist_ok=True)


def extract(index):
    path = FRAMES / f'{index:04d}.jpg'
    if path.exists():
        return
    result = subprocess.run(
        [str(FFMPEG), '-hide_banner', '-loglevel', 'error', '-ss', str(index / 2),
         '-i', str(SOURCE), '-frames:v', '1', '-vf', 'scale=630:-1', '-q:v', '3',
         '-y', str(path)], capture_output=True)
    if result.returncode or not path.exists():
        raise RuntimeError(f'{index / 2}: {result.stderr.decode(errors="replace")}')


def label(index):
    seconds = index / 2
    return f'{int(seconds // 60):02d}:{seconds % 60:04.1f}'


def sheet(indices, path, columns=3, width=630):
    height = round(width * 1080 / 2520)
    rows = (len(indices) + columns - 1) // columns
    canvas = Image.new('RGB', (columns * width, rows * (height + 28)), '#171717')
    draw = ImageDraw.Draw(canvas)
    for position, index in enumerate(indices):
        x = position % columns * width
        y = position // columns * (height + 28)
        with Image.open(FRAMES / f'{index:04d}.jpg') as frame:
            canvas.paste(frame.resize((width, height)), (x, y))
        draw.text((x + 10, y + height + 7), label(index), fill='white')
    canvas.save(path, quality=90)


if __name__ == '__main__':
    indices = list(range(418))  # 0.0 through 208.5 seconds, exact source seek requests.
    with ThreadPoolExecutor(max_workers=6) as pool:
        list(pool.map(extract, indices))
    overview = indices[::4]
    for page, start in enumerate(range(0, len(overview), 15), 1):
        sheet(overview[start:start + 15], SHEETS / f'overview-{page:02d}.jpg')
    scores = []
    previous = None
    for index in indices:
        with Image.open(FRAMES / f'{index:04d}.jpg') as frame:
            current = frame.resize((84, 36)).convert('RGB')
        if previous is not None:
            score = sum(ImageStat.Stat(ImageChops.difference(previous, current)).mean) / 3
            scores.append({'time_s': index / 2, 'pixel_difference': round(score, 3)})
        previous = current
    # Image differences are navigation aids, never verified cut boundaries.
    (ROOT / 'frame-differences.json').write_text(json.dumps(scores, indent=2), encoding='utf-8')
    digest = hashlib.sha256()
    with SOURCE.open('rb') as media:
        for block in iter(lambda: media.read(1024 * 1024), b''):
            digest.update(block)
    metadata = {'source': str(SOURCE), 'sha256': digest.hexdigest(), 'sample_interval_s': .5,
                'first_source_seek_s': 0, 'last_source_seek_s': 208.5, 'frame_count': len(indices),
                'overview_pages': 7, 'full_audiovisual_playback': False,
                'audio_semantic_review': False}
    (ROOT / 'inspection-metadata.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(metadata, ensure_ascii=False))
