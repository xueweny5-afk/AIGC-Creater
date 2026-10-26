# ASSET CONTRACT｜PROP03 折信

## IDENTITY
- **Asset ID / Type / Version / Status：** PROP03 / PROP / v1-plan / PLANNED
- **Purpose：** S006 的接触动作与前后物件连续性
- **Source Visual Bible：** ../../../visual-development/world-visual-bible.md v3
- **Evidence：** CREATIVE；不是被证明属于历史人物的实物

## LOCKED FEATURES
- 一封单手可持的未展纸信；尺寸、材料、边缘和使用痕迹在状态变化中保持同一件物品。

## VARIABLE STATES
- 只允许剧本明确需要的平展/卷曲、固定书行、信的持握角度或碗内食物变化；不得换物。

## PRESENTATION CHOICES
- 独立道具、无人物手、无完整场景、均匀中性光；不生成可读伪史料文字。

## UNKNOWN / OPEN FIELDS
- 历史真实器物形制与所属实物 UNKNOWN；设计只服务当前动作。

## REQUIRED VIEWS / PLATES
| View / State | Parent | Target | Status |
|---|---|---|---|
| 基础图 | 创作设计，旧分镜仅作尺寸/材料线索 | `folded-v1.png` | PLANNED |
| 变化态 | 已批准基础图 | `—` | NOT_REQUIRED |
| 材料细节 | 已批准基础图 | 按近景需求补 | PLANNED |

## CANONICAL FACE / BODY ANCHORS
- NOT_APPLICABLE。

## MATERIAL DETAIL PLATES
- 纸/木/陶/食物按本资产材料呈现局部结构和接触反应；不做塑料高光或均匀做旧。

## ENVIRONMENT DETAIL & STATE PLATES
- NOT_APPLICABLE；放入 LOC03 时遵守该空间的主视图和三角度拓扑。

## COMBINED LOOK DEPENDENCIES
- 与 LOC03 和对应 CH/CST 资产结合后才形成剧情接触图，不反向改变独立物件。

## REFERENCE ROLE MAP
| Reference | Role | Allowed Influence | Must Not Override |
|---|---|---|---|
| `../../../storyboard/frames/F03-lu-tang/S06-start-v1.png` | MATERIAL / SCALE provisional | 物件在画面中的大体尺度 | 剧本状态、人物身份和历史真实性 |

## DERIVATION / EDIT CONTRACT
- 基础图 CREATE NEW；变化态从已批准基础图 EDIT FROM。
- **Change：** 只改剧本指定的物理状态。**Preserve：** 一封单手可持的未展纸信。**Constraints：** 无人、无字、无物件数量漂移。

## NEGATIVE CONSTRAINTS
- 不要人物、手、额外道具、可读汉字、品牌、水印、材质突变。

## FILES AND PATHS
- 目标目录 `assets/props/PROP03/`；当前无独立图片。

## REVIEW RESULTS
- **Evidence / Files / Decision：** NOT_GENERATED / 无 / PLANNED

## DOWNSTREAM USE
- S006 动作与空间连续性；真实原图审核前不得标 G3 APPROVED。

## CHANGE LOG
- 2026-10-03：依据 G2 剧本与 USER_GENERATE 交接建立计划合同。

