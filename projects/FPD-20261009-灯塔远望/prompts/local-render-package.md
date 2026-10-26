# SH01 / UNIT01 Local Render Package｜v1

- Package status：`SUPERSEDED FOR CURRENT REQUEST`；这是本地二维试作的执行记录。本次用户明确要求图生视频提示词，当前交接见 `image-to-video-prompt-v1.md`。
- Execution profile：本地 Python/Pillow 逐帧二维仿射裁切 + FFmpeg H.264；可复现脚本 `../generation/render-camera-move-v2.py`。这不是在线图生视频模型，因而无模型语法或图生视频能力声明。
- Source lock：`PLATE01/v1`、`CG01/v1`、Shot List v1、Motion Spec v1、`NLA01/LL01/AM01`。
- Input role：`../storyboard/frames/F01-海岸灯塔/source-v1.png` 是唯一、必须、用户提供的完整画面参考。脚本不上传外部平台。
- Output：`../generation/灯塔远望-运镜版-v2.mp4`，8 秒、24 fps、760×950、无声。
- MAIN：逐渐把注意力从人物背影交给灯塔。SUPPORT：保留海岸纵深。HOLD：所有源图内部像素状态。
- Response chain：无前镜 → 灯塔光点 → 1.5 秒观察 → 取景缓慢推进与右移 → 在灯塔和海岸关系上停留。
- Rejection criteria：黑边、反射补边、人物或灯塔消失、突然跳帧、越过源图边界、声称环境独立运动。

## 13-item coverage receipt

| # | Item | Status / Destination |
|---:|---|---|
| 1 | Reference anchors | `MAPPED` → 源图路径与哈希 |
| 2 | Overall concept | `MAPPED` → Shot List / 本包 MAIN |
| 3 | Dynamic description | `MAPPED` → Motion Spec 时间曲线 |
| 4 | Image texture / cinematography intent | `MAPPED` → 保持原图像素质感；二维平稳推进 |
| 5 | Shot language | `MAPPED` → 单镜，推进与右向取景 |
| 6 | Scene | `MAPPED` → `SC01` 原图 |
| 7 | Color / style | `MAPPED` → 不改色，继承 `NLA01` |
| 8 | Light | `MAPPED` → `LL01` 保持 |
| 9 | Composition | `MAPPED` → `CG01/v1` 与末帧 |
| 10 | Emotion / observable performance | `MAPPED` → 注意力转移；人物表演 `HOLD` |
| 11 | Shot timeline | `MAPPED` → 0–1.5 / 1.5–6.5 / 6.5–8 秒 |
| 12 | Sound | `NOT_APPLICABLE` → 无声版本 |
| 13 | Exclusions | `MAPPED` → 无新物体、无画内独立动画、无越界 |

## Execution and reverse check

只执行 `UNIT01`；无需高风险 Pilot。先运行脚本、记录真实媒体，再由 QC 解码全帧并抽查边界/关键帧。核对包中每个约束均能回到已审的 Brief、Shot、Frame 或 Motion；本包不添加新的故事、空间或动作事实。
