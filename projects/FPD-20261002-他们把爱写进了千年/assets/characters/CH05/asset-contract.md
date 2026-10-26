# ASSET CONTRACT｜CH05 陆游

## IDENTITY
- **Asset ID / Type：** CH05 / CHARACTER
- **Version / Status：** v1-plan / PLANNED
- **Purpose：** S005/S006 的回身伸手、独处持信；建立独立正面身份锚点
- **Source Visual Bible：** ../../../visual-development/world-visual-bible.md v3
- **Evidence Status：** CREATIVE visual reconstruction；非历史肖像复原

## LOCKED FEATURES
- 人物名称、四组关系与剧本中的出现范围不变；成为 Canon 后，同一人的脸部比例、体态和发型轮廓跨所需场景不变。
- 用户认可的旧分镜仅提供外观方向。正面脸审核前，不把其中的脸或服饰宣布为 Canon。

## VARIABLE STATES
- 剧本所需的回身伸手、独处持信；表情、视线和手势可随场景改变，不改变身份。

## PRESENTATION CHOICES
- 第一张为正面、平视、无表情、无遮挡的头部近照；均匀中性光、简洁背景、无正式戏服和道具。

## UNKNOWN / OPEN FIELDS
- 真实历史外貌、精确年龄、具体妆发与衣装形制 UNKNOWN；图像只表达本片重构。

## REQUIRED VIEWS / PLATES
- 首批仅 Canon Face Front；通过后按用户明确要求，逐张派生左右 45°、左右侧面头部图；再审全身正面体态，派生全身六视图，每张独立原图。
- 所有衍生图使用同一已批准身份母图；不得在新角度重新抽脸或体态。

## CANONICAL FACE / BODY ANCHORS
- **Canonical Face Front Close-up：** PLANNED，目标 `canon-face-front-v1.png`
- **Canonical Body：** PLANNED；不得先于正面脸审核
- **Required Head Angles：** 正面、左 45°、左侧、右侧、右 45°；待正面脸批准后派生
- **Required Full-body Six Views：** 正面、左前 45°、左侧、背面、右侧、右前 45°；待全身正面批准后逐张派生

## VIEW MATRIX
| View / Plate | Required | Derivation Parent | File Path | Status | Review Notes |
|---|---|---|---|---|---|
| 正面脸 | YES / batch-01 | 旧分镜仅为临时外观方向 | `canon-face-front-v1.png`（目标） | PLANNED | 需真实像素审核 |
| 头部四角度 | YES / batch-02 | 已批准正面脸；侧面兼用同侧 45° | 尚无 | PLANNED | 不得独立重抽身份 |
| 全身正面与另五视图 | YES / batch-02 | 已批准正面脸→全身正面→其他视图 | 尚无 | PLANNED | 不得独立重抽体态 |

## MATERIAL DETAIL PLATES
- 皮肤与头发的局部差异在正面脸审核时检查；独立服装材料由 CST05 负责。

## ENVIRONMENT DETAIL & STATE PLATES
- NOT_APPLICABLE；背景应中性，场景图由对应 LOC 资产负责。

## COMBINED LOOK DEPENDENCIES
- Character: CH05 的已批准 Canon；Costume: CST05 待建；Makeup/Hair: 暂不单列；先验正面再验所需侧面。

## REFERENCE ROLE MAP
| Reference | Role | Allowed Influence | Must Not Override |
|---|---|---|---|
| `../../../storyboard/frames/F03-lu-tang/S05-start-v1.png` | IDENTITY（临时外观线索，画面右侧男子） | 面部大体感觉；供第一张候选参考 | 剧本身份、史实边界；不能直接当 Canon |
| `../../../storyboard/sequence-contact-v1.jpg` | STYLE / COMPOSITION | 八镜整体画面感觉 | 正面身份图须中性、单人、无叙事场景 |

## DERIVATION / EDIT CONTRACT
- **Parent / Edit Target：** 首张为新建候选；后续角度从已批准正面脸编辑派生
- **Change：** 从合成分镜提取单人正面可审核身份
- **Preserve：** 画面右侧男子的整体外观方向和人物关系
- **Constraints：** 不能复制分镜的姿势、光线、服饰与背景

## NEGATIVE CONSTRAINTS
- 无其他人物、戏服抢戏、遮脸、夸张表情、戏剧灯光、道具、文字、水印、额外肢体；不声称历史真人肖像。

## FILES AND PATHS
- 目标：`assets/characters/CH05/canon-face-front-v1.png`；当前无图片文件。

## REVIEW RESULTS
- **Review Evidence：** NOT_GENERATED
- **Files Inspected：** 无
- **Passed / Failed / Decision：** 尚未审核；PLANNED

## DOWNSTREAM USE
- 与 CST05 LOC03 PROP03 的对应独立资产组合后，供 S005/S006 身份连续性审查；G3 前不得当作批准源。

## CHANGE LOG
- 2026-10-03：依据 G2 剧本 v3 与 Visual Bible v3 建立计划合同。
