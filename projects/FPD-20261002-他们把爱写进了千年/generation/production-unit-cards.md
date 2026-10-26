# Production Unit Cards｜S01–S08（生成前编译视图）

**状态更正：** STALE / BLOCKED BY G3–G4。G2 v3 已通过，但八张首帧获得的是分镜视觉方向认可，不是 Stage 08 独立资产 P0 批准；旧卡的动作仍不含短对白。此表不能作为执行入口，上游通过后须重新编译。见 `../qc/workflow-gate-audit.md`。

共同参数目标：9:16，单镜取 3 秒稳定画面；文字与音效在后期完成。逐镜可复制提示词在 `../prompts/pre-video-prompt-package.md`；负向限制已写入相应主提示词，待确定平台是否支持独立负向字段。每镜以实际首帧起步，视频模型不得自行生成人物消失转场。

| Unit | 主任务 / 注意力 | 输入 P0 与状态 | 主动作 → 交接 | 核心风险 / 验收 | 依赖 |
|---|---|---|---|---|---|
| S01 | MAIN：建立李赵共同校看 | `../storyboard/frames/F01-li-zhao/S01-start-v1.png`；LOC01/PROP01/L-WARM-v1 | 指尖沿碑拓轻移 → 手势未完切 | 手指与碑拓稳定；二人身份稳定 | S02 用同一碑拓 |
| S02 | HOLD：让空位被发现 | `../storyboard/frames/F01-li-zhao/S02-start-v1.png`；LOC01/PROP01/L-LONELY-v1 | 托腮望空位 → 静止后换组 | 赵明诚不重现；碑拓和空间可辨 | S01 同物件 |
| S03 | MAIN：王弗指书记忆 | `../storyboard/frames/F02-su-wang/S03-start-v1.png`；LOC02/PROP02/L-WARM-v1 | 指尖轻移 → 指书未完切 | 脸与书页稳定；不生成文字 | S04 同书页 |
| S04 | HOLD：空椅回应 | `../storyboard/frames/F02-su-wang/S04-start-v1.png`；LOC02/PROP02/L-LONELY-v1 | 托腮侧目空椅 → 静止后换组 | 王弗不重现；椅与书可辨 | S03 同物件 |
| S05 | MAIN：两人同路 | `../storyboard/frames/F03-lu-tang/S05-start-v1.png`；LOC03/PROP03/L-WARM-v1 | 慢行相视 → 步伐未停切 | 人脸、石径、门洞稳定 | S06 同园路 |
| S06 | HOLD：独对园路 | `../storyboard/frames/F03-lu-tang/S06-start-v1.png`；LOC03/PROP03/L-LONELY-v1 | 停步看折信 → 视线下落后换组 | 唐氏不重现；信件不变形 | S05 同园路 |
| S07 | MAIN：平常一餐 | `../storyboard/frames/F04-shen-chen/S07-start-v1.png`；LOC04/PROP04/L-WARM-v1 | 相视轻笑 → 碗声切 | 双碗与餐具数量稳定 | S08 同饭桌；首个未来试镜候选 |
| S08 | HOLD：空碗结尾 | `../storyboard/frames/F04-shen-chen/S08-start-v1.png`；LOC04/PROP04/L-LONELY-v1 | 托腮看空碗 → 静止结束 | 陈芸不重现；空碗保持空着 | S07 同饭桌；首个未来试镜候选 |

**验收与回退：** 单镜看身份、肢体、道具、机位和有效 3 秒；成对看同物件硬切是否立即读出缺席。若核心物件或人物在首帧已不连续，返回 `../storyboard/frame-manifest.md` 的对应 Frame ID 迭代；若仅动态漂移，先缩小动作并逐次只改一个变量。真实模型、参数、Take 路径和 QC 结论只有执行后才填写到 `generation-manifest.md` 的后续版本。
