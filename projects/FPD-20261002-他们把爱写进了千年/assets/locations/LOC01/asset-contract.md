# ASSET CONTRACT｜LOC01 李赵书房

## IDENTITY
- **Asset ID / Type / Version / Status：** LOC01 / LOCATION / v1-plan / PLANNED
- **Purpose：** S001–S002 中前后同处的空间连续性
- **Source Visual Bible：** ../../../visual-development/world-visual-bible.md v3
- **Evidence：** CREATIVE reconstruction；旧分镜仅为可见空间方向，不是故居证据

## LOCKED FEATURES
- 书案、后方书架、格窗、灯位在主、左约 30°、右约 30° 三视图中保持三维相对位置、比例和朝向。
- 人物缺席的座位/路径位置固定，不能因视角变化镜像翻转。

## VARIABLE STATES
- 剧本前后可因时间/天气调整灯光与环境活跃度；空间结构、固定材质与使用痕迹不变。空气始终 NONE / CLEAN AIR。

## PRESENTATION CHOICES
- 无人物、无核心可移动道具；主视图及同侧左、右约 30° 各一张；中性基础光。反向墙面当前未知，不生成凭空完整背视图。

## UNKNOWN / OPEN FIELDS
- 不可见的房间背墙/园门外路径、历史真实建筑尺度和装饰 UNKNOWN；新增镜头引用前须补拓扑证据。

## REQUIRED VIEWS / PLATES
| View / Plate | Parent | Target | Status |
|---|---|---|---|
| 无人主视图 | 旧分镜仅为 TOPOLOGY 临时线索 | `topology-main-v1.png` | PLANNED |
| 左约 30° | 已批准无人主视图 | `view-left30-v1.png` | PLANNED |
| 右约 30° | 已批准无人主视图 | `view-right30-v1.png` | PLANNED |
| 结构/材料细节 | 已批准主视图 | `detail-surface-v1.png` | PLANNED |

## CANONICAL FACE / BODY ANCHORS
- NOT_APPLICABLE。

## MATERIAL DETAIL PLATES
- 对书案、后方书架、格窗、灯位的木/石/纸接触表面做局部使用痕迹审核；不能所有区域均匀做旧。

## ENVIRONMENT DETAIL & STATE PLATES
- 主视图、左右角度与材料板须保持同一锚点；前后 Look/Light State 见 Visual Bible 对应 LLS-LOC01-TOGETHER-v1 / ALONE-v1。空气 NONE / CLEAN AIR。

## COMBINED LOOK DEPENDENCIES
- 场面组合需已批准人物、服装与 PROP01；此空间图不含它们。

## REFERENCE ROLE MAP
| Reference | Role | Allowed Influence | Must Not Override |
|---|---|---|---|
| `../../../storyboard/frames/F01-li-zhao/S01-start-v1.png` | TOPOLOGY / provisional | 已可见的书案、后方书架、格窗、灯位关系 | 人物身份、历史真实性、未见反向空间 |

## DERIVATION / EDIT CONTRACT
- 主视图从旧分镜 EDIT FROM，清除人物/道具；左右角度从已批准主视图 EDIT FROM。
- **Change：** 仅视角与可解释遮挡。**Preserve：** 书案、后方书架、格窗、灯位。**Constraints：** 不镜像、不换房、不增无因空气介质。

## NEGATIVE CONSTRAINTS
- 无人物、手、字、水印、虚构门廊、镜像、飘雾或任意材质替换。

## FILES AND PATHS
- 目标目录 `assets/locations/LOC01/`；当前无独立图片。

## REVIEW RESULTS
- **Evidence / Files / Decision：** NOT_GENERATED / 无 / PLANNED

## DOWNSTREAM USE
- 与 PROP01 及人物资产组合；三视图逐张审核后按实际镜头范围申请 G3。

## CHANGE LOG
- 2026-10-03：依据用户多角度一致性要求建立计划合同。

