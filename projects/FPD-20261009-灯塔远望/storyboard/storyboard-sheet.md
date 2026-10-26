# Storyboard Sheet｜v1

| Shot | Frame | 画面 | 来源 | 状态 |
|---|---|---|---|---|
| `SH01` | `F01-START` | 源图全幅，人物左前景、灯塔右远景 | `frames/F01-海岸灯塔/source-v1.png` | `SOURCE-APPROVED` |
| `SH01` | `F01-END` | 同图向右取景并推进，人物退到左缘，灯塔与海岸更突出 | `frames/F01-海岸灯塔/end-v2.png` | `COMPOSITION-ONLY`，本地二维裁切预览；不是图生视频末帧批准 |

- Composition Guide：`CG01/v1`，复用源图锁定二维平面坐标；主体占比、前中后景、栏杆遮挡和屏幕方向不得重绘。对 `SH01` 为 `COMPOSITION APPROVED FOR CROP ONLY`。
- Guide Allowed Influence：仅裁切窗口、取景重心和尺度。Must Not Transfer：不推导人物正面、灯塔背面、风向、三维景深或真实地理。
- Sequence Review：单镜无跨镜跳切；首尾必须保留同一灯塔与海岸地标。
- Rhythm Map：`0–1.5s HOLD`，`1.5–6.5s MAIN MOVE`，`6.5–8s HOLD/SETTLE`；无对白或声音桥。
- Static review：已查看源图与本地裁切预览的实际像素；源图边界内取景，人物、海岸、灯塔、栏杆关系清楚。`G4 READY` 仅覆盖这个单镜的构图和画内状态，不覆盖未来模型的动态像素。
- Animatic：单镜由实际视频候选承担时长预览；生成前状态 `NOT_RENDERED`。无跨镜顺序风险。
