# ASSET CONTRACT｜CST06 唐氏衣装

## IDENTITY
- **Asset ID / Type / Version / Status：** CST06 / COSTUME / v1-plan / PLANNED
- **Purpose：** 唐氏在本片步行时保持同一穿着结构
- **Source Visual Bible：** ../../../visual-development/world-visual-bible.md v3
- **Evidence：** CREATIVE；旧分镜中的服装是已认可的外观方向，未经历史服饰考据

## LOCKED FEATURES
- 服装批准后，层数、领袖、衣摆、系结、主色关系、织物垂坠在所有角度及组合定妆中一致。
- 衣袖不遮住步行动作；不得凭空增加纹样、盔甲、礼服或现代元素。

## VARIABLE STATES
- 角度、姿态导致的自然褶皱、受光变化；不构成换装或破损。

## PRESENTATION CHOICES
- 正面/侧面/背面各一张无脸人台独立图，均匀中性光、简单背景；不混入人物脸或场景。

## UNKNOWN / OPEN FIELDS
- 精确朝代形制与真实人物衣着 UNKNOWN；此版以视觉重构制作，不标“复原”。

## REQUIRED VIEWS / PLATES
| View | Parent | Target | Status |
|---|---|---|---|
| 正面 | 旧分镜仅作 WARDROBE 方向 | `front-v1.png` | PLANNED |
| 左侧 | 已批准正面 | `side-v1.png` | PLANNED |
| 背面 | 已批准正面与侧面 | `back-v1.png` | PLANNED |
| 织物/袖口细节 | 已批准服装视图 | 需要时 `detail-fabric-v1.png` | PLANNED |

## CANONICAL FACE / BODY ANCHORS
- NOT_APPLICABLE；此资产不能定义脸或体态。

## MATERIAL DETAIL PLATES
- 浅暖色多层衣装的织物层次、局部磨损、低光泽和步行时的袖口/衣摆响应，随正面和侧面共同审核。

## ENVIRONMENT DETAIL & STATE PLATES
- NOT_APPLICABLE。

## COMBINED LOOK DEPENDENCIES
- 依赖已批准 CH06 正面脸和全身体态，再按 `../../prompts/costume-combined-multiview-v1.md` 做组合六视图；服装图不得修改 CH06 身份。

## REFERENCE ROLE MAP
| Reference | Role | Allowed Influence | Must Not Override |
|---|---|---|---|
| `../../../storyboard/frames/F03-lu-tang/S05-start-v1.png` | WARDROBE / provisional（左侧女子） | 浅暖色多层衣装的整体方向 | 人脸、空间与历史准确性 |

## DERIVATION / EDIT CONTRACT
- 正面为 CREATE NEW；侧面和背面以已批准服装图 EDIT FROM。
- **Change：** 只改变观察角度。**Preserve：** 层次、版型、织物和色彩。**Constraints：** 无脸、无场景、无随意增减配件。

## NEGATIVE CONSTRAINTS
- 不要人物面孔、其他服装、结构跳变、塑料光泽、均匀做旧、文字、水印。

## FILES AND PATHS
- 目标目录 `assets/costumes/CST06/`；当前无独立图片。

## REVIEW RESULTS
- **Evidence / Files / Decision：** NOT_GENERATED / 无 / PLANNED

## DOWNSTREAM USE
- 与 CH06 已批准身份组合，供对应场景与分镜引用；G3 前不可标 APPROVED。

## CHANGE LOG
- 2026-10-03：依据用户多角度一致性要求建立计划合同。

