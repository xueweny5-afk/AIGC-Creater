# ASSET CONTRACT｜CH02 赵明诚

## IDENTITY
- **Asset ID / Type：** CH02 / CHARACTER
- **Version / Status：** v2-face / GENERATED_PENDING_REVIEW（正脸 APPROVED / SELF-REVIEWED；其余必需视图待生成审核）
- **Purpose：** S001 的按住纸角回应；建立独立正面身份锚点
- **Source Visual Bible：** ../../../visual-development/world-visual-bible.md v3
- **Evidence Status：** CREATIVE visual reconstruction；非历史肖像复原

## LOCKED FEATURES
- 人物名称、四组关系与剧本中的出现范围不变；成为 Canon 后，同一人的脸部比例、体态和发型轮廓跨所需场景不变。
- 用户认可的旧分镜仅提供外观方向。正面脸审核前，不把其中的脸或服饰宣布为 Canon。

## VARIABLE STATES
- 剧本所需的按住纸角回应；表情、视线和手势可随场景改变，不改变身份。

## PRESENTATION CHOICES
- 第一张为正面、平视、无表情、无遮挡的头部近照；均匀中性光、简洁背景、无正式戏服和道具。

## UNKNOWN / OPEN FIELDS
- 真实历史外貌、精确年龄、具体妆发与衣装形制 UNKNOWN；图像只表达本片重构。

## REQUIRED VIEWS / PLATES
- 首批仅 Canon Face Front；通过后按用户明确要求，逐张派生左右 45°、左右侧面头部图；再审全身正面体态，派生全身六视图，每张独立原图。
- 所有衍生图使用同一已批准身份母图；不得在新角度重新抽脸或体态。

## CANONICAL FACE / BODY ANCHORS
- **Canonical Face Front Close-up：** `canon-face-front-v2.png` / APPROVED / SELF-REVIEWED；后续身份派生的唯一母图
- **Canonical Body：** PLANNED；不得先于正面脸审核
- **Required Head Angles：** 正面、左 45°、左侧、右侧、右 45°；待正面脸批准后派生
- **Required Full-body Six Views：** 正面、左前 45°、左侧、背面、右侧、右前 45°；待全身正面批准后逐张派生

## VIEW MATRIX
| View / Plate | Required | Derivation Parent | File Path | Status | Review Notes |
|---|---|---|---|---|---|
| 正面脸 | YES / batch-01 | `canon-face-front-v1-candidate.png` 仅作修复源 | `canon-face-front-v2.png` | APPROVED / SELF-REVIEWED | 完整发髻入画，脸与胡须同 v1 候选视觉一致；v2 为后续唯一身份母图 |
| 头部四角度 | YES / batch-02 | 已批准正面脸；侧面兼用同侧 45° | 尚无 | PLANNED | 不得独立重抽身份 |
| 全身正面与另五视图 | YES / batch-02 | 已批准正面脸→全身正面→其他视图 | 尚无 | PLANNED | 不得独立重抽体态 |

## MATERIAL DETAIL PLATES
- 皮肤与头发的局部差异在正面脸审核时检查；独立服装材料由 CST02 负责。

## ENVIRONMENT DETAIL & STATE PLATES
- NOT_APPLICABLE；背景应中性，场景图由对应 LOC 资产负责。

## COMBINED LOOK DEPENDENCIES
- Character: CH02 的已批准 Canon；Costume: CST02 待建；Makeup/Hair: 暂不单列；先验正面再验所需侧面。

## REFERENCE ROLE MAP
| Reference | Role | Allowed Influence | Must Not Override |
|---|---|---|---|
| `canon-face-front-v2.png` | IDENTITY / EDIT TARGET（批准正脸母图） | 后续头部角度与全身正面的人脸、发际、发髻和胡须轮廓 | 视角、体态和正式服装仍需独立审核 |
| `../../../storyboard/frames/F01-li-zhao/S01-start-v1.png` | IDENTITY（临时外观线索，画面右侧男子） | 面部大体感觉；供第一张候选参考 | 剧本身份、史实边界；不能直接当 Canon |
| `../../../storyboard/sequence-contact-v1.jpg` | STYLE / COMPOSITION | 八镜整体画面感觉 | 正面身份图须中性、单人、无叙事场景 |

## DERIVATION / EDIT CONTRACT
- **Parent / Edit Target：** 首张为新建候选；后续角度从已批准正面脸编辑派生
- **Change：** 从合成分镜提取单人正面可审核身份
- **Preserve：** 画面右侧男子的整体外观方向和人物关系
- **Constraints：** 不能复制分镜的姿势、光线、服饰与背景

## NEGATIVE CONSTRAINTS
- 无其他人物、戏服抢戏、遮脸、夸张表情、戏剧灯光、道具、文字、水印、额外肢体；不声称历史真人肖像。

## FILES AND PATHS
- 历史候选：`assets/characters/CH02/canon-face-front-v1-candidate.png`（REWORK，不作派生源）。批准正脸母图：`assets/characters/CH02/canon-face-front-v2.png`。

## REVIEW RESULTS
- **Review Evidence：** 2026-10-03 AI 目视自审；v1 候选 1122×1402，SHA256 `71F0ACC7D9B52526E24D2821CF78D73083728F97D130AA852A42AD4FD15B87EA`；v2 修复版 1086×1448，SHA256 `844264634B2DD5E8028C600881F138A37D877D0D6F7A2C8C684B6F9278DC96AC`。
- **Files Inspected：** `canon-face-front-v1-candidate.png`、`canon-face-front-v2.png`；并与 `../../../storyboard/frames/F01-li-zhao/S01-start-v1.png` 的外观方向对照。
- **Passed：** 单人正面、五官无遮挡、平视克制表情、中性背景与光线；发髻轮廓完整且上方有留白；脸和胡须与 v1 候选无明显身份漂移。
- **Failed：** 正脸无阻断项；尚无头部其他四角度和全身六视图，跨视图一致性未验证。
- **Decision：** 正脸 `APPROVED / SELF-REVIEWED`；整项人物资产仍待多视图审核。后续仅从 v2 母图派生，不用 v1 候选。

## DOWNSTREAM USE
- v2 正脸可作为 CH02 头部角度与全身正面的批准身份源；与 CST02 LOC01 PROP01 的对应独立资产组合后，供 S001 身份连续性审查。G3 前不得把整项人物资产当作已批准镜头组合源。

## CHANGE LOG
- 2026-10-03：依据 G2 剧本 v3 与 Visual Bible v3 建立计划合同。
- 2026-10-03：收到用户生成的正面候选并审核；脸部与胡须保留，发髻顶端需补全。
- 2026-10-03：收到并审核修复版 v2；正脸通过 AI 自审，锁定为唯一派生母图。
