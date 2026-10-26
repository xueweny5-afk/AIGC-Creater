# ASSET CONTRACT

## IDENTITY

- **Asset ID：** LOC-BATTLEFIELD-001
- **Type：** LOCATION
- **Working Name：** 香积寺附近连续战场
- **Version：** V1.2
- **Status：** READY_FOR_DERIVATION
- **Purpose：** 为 S001—S008 提供同一战场的空间拓扑、尺度、地表和状态连续性；保证前军、中军、东翼与战后原阵位之间关系可解释。
- **Source Visual Bible Version：** World & Visual Bible V1
- **Evidence Status：** DOCUMENTED GEOGRAPHIC RELATION / CREATIVE RECONSTRUCTION

## LOCKED FEATURES

- 一个连续城外战场，不是寺院攻防场景。
- 七个功能区：A 前军起始阵地、B 追击走廊、C 中军、D 退路/重组区、E 推进区、F 东侧骑兵走廊、G 战后原阵位。
- G 与 A/B 的地表和固定尺度参照必须能够比对，不能另造一个战后场景。
- F 必须位于真实东侧，并具备绕向唐军侧后的机动关系。
- 中军位于前军之后、辎重之前；前军溃退能够物理上冲击中军方向。
- 地面为黄褐至灰褐的压实土、松土、碎石和稀疏草根组合；无沙漠沙丘。
- 不把现存香积寺塔、寺院建筑或清晰长安城墙作为固定地标。
- 空间源资产保持 CLEAN AIR；扬尘以独立环境状态叠加，不能成为唯一拓扑参考。

## VARIABLE STATES

- B0 战前：地表旧足迹有限，低杂物密度，旗杆提供尺度。
- B1 溃乱：追击路径出现密集足迹、马蹄、滑痕、倒旗和少量散落兵器。
- B2 推进：沿主战轴增加重复脚印、拖痕、局部碎甲和受损旗号。
- B3 战后：在 B0/B1 同一空间增加重叠足迹、遗物、折旗和大量无人占据的阵位。
- 天光从午后到黄昏变化，但不改变地形和固定锚点。

## PRESENTATION CHOICES

- 首个拓扑资产采用中性制作示意图：上方标记“燕军方向”，下方标记“唐军后方”，右侧标记“东翼”；这是工作坐标，不是历史罗盘复原。
- 地面整体资产使用自然中性光和清洁空气，避免戏剧性逆光、极端天气和人物表演。
- 正反关系图用于验证空间，不作为最终镜头构图。

## UNKNOWN / OPEN FIELDS

- 757 年实际战线朝向与正东方位夹角。
- 当日天气、风向、湿度与地表真实含水量。
- 河流、寺院建筑和长安城墙是否在任一战场位置可见。
- 远方地平线、微地形起伏和植被密度的精确历史状态。
- 战场实际尺寸；制作资产只锁定相对尺度与通行关系。

## REQUIRED VIEWS / PLATES

1. `topology-plan-v001`：七个功能区、主战轴、东翼与唐军后方关系。
2. `overview-tang-front-to-yan-v001`：从前军起始区理解追击走廊与敌军方向的中性空间参考。
3. `overview-pursuit-to-tang-rear-v001`：反向验证重组区、中军和后方关系。
4. `overview-east-corridor-v001`：验证东侧骑兵走廊与唐军侧后关系。
5. `state-b0-prebattle-v001`：干净战前状态。
6. `state-b3-aftermath-v001`：从同一拓扑派生的战后状态。
7. `detail-ground-system-v001`：压实土、松土、碎石、枯草与足迹尺度。

## CANONICAL FACE / BODY ANCHORS

- **Canonical Face Front Close-up：** NOT_APPLICABLE
- **Canonical Body：** NOT_APPLICABLE
- **Required Head Angles：** NOT_APPLICABLE
- **Required Full-body Six Views：** NOT_APPLICABLE

## VIEW MATRIX

| View / Plate | Required | Derivation Parent | File Path | Status | Review Notes |
|---|---|---|---|---|---|
| Topology plan V1 | Yes | Contract V1 | `topology-plan-v001.png` | REWORK_ARCHIVED | 斜向航拍环境概念；区域与轴线未被稳定区分 |
| Topology plan V2 | Yes | V1 edit | `topology-plan-v002.png` | SELF-REVIEWED_PASS | 中央主战轴与右侧东翼通道清楚；与 A—G 覆盖图共同构成制作父资产 |
| A—G production overlay | Yes | Topology plan V2 | `topology-zones-v001.svg` / `.png` | SELF-REVIEWED_PASS | 七区、三方向和主要动线已明确；明确标注非历史测绘 |
| Tang front → Yan direction | Yes | APPROVED topology | — | BLOCKED_BY_PARENT | 不得自行改变 A—E 关系 |
| Pursuit corridor → Tang rear | Yes | APPROVED topology | — | BLOCKED_BY_PARENT | 与上一视图互为同一空间反向关系 |
| East cavalry corridor | Yes | APPROVED topology | — | BLOCKED_BY_PARENT | 必须明确真实东侧和侧后路径 |
| B0 prebattle state | Yes | APPROVED clean topology | — | BLOCKED_BY_PARENT | 无明显悬浮尘土 |
| B3 aftermath state | Yes | APPROVED B0 state | — | BLOCKED_BY_PARENT | 只添加损耗，不改变地形 |
| Ground detail plate | Yes | MAT-BATTLEFIELD-001 | — | PLANNED | 与材质资产联合审核 |

## MATERIAL DETAIL PLATES

| Material / Detail | Scale / Location | Construction / Surface | Roughness / Reflection / Translucency | Weight / Drape / Movement | Clean / Wet / Dirty / Damaged State | File Path | Status | Review Notes |
|---|---|---|---|---|---|---|---|---|
| 压实土 | 阵位与中军通行区 | 细土、碎石、反复踩踏 | 高粗糙、低反射、不透光 | 固定表面 | 干燥旧使用痕迹 | — | PLANNED | 不得像平滑泥塑 |
| 松土 | 追击与骑兵路径 | 表层颗粒松散 | 高粗糙 | 可被脚步马蹄扰动 | 干燥/扬尘后 | — | PLANNED | 必须能解释尘源 |
| 稀疏草根 | 非主要通行区域 | 枯草、低矮根系 | 哑光 | 风与踩踏下局部移动 | 干燥/倒伏 | — | PLANNED | 禁止茂密草原化 |

## ENVIRONMENT DETAIL & STATE PLATES

| Zone / Layer | Ground / Wall / Ceiling / Dressing | Use Traces / Aging | Dust / Moisture / Smoke / Vegetation | Moving Elements | Time / Weather State | File Path | Status |
|---|---|---|---|---|---|---|---|
| A/G 原阵位 | 压实土、旗杆锚点、低杂物密度 | 战前旧足迹；战后重叠足迹和遗物 | S001 CLEAN AIR；S008 轻尘沉降 | 旗布、松散纤维 | 午后 / 黄昏；天气 UNKNOWN | — | PLANNED |
| B/D/E 主战轴 | 松土、碎石、稀疏草根 | 滑痕、拖痕、碎甲随事件增加 | 动作驱动尘土；无烟雾 | 人马和旗帜 | 午后至黄昏 | — | PLANNED |
| C 中军 | 较压实土、旗杆、辎重边缘 | 使用痕迹密集但动线清楚 | 前景清洁、背景远尘 | 旗手、役夫与马匹 | 午后 | — | PLANNED |
| F 东翼 | 开阔干土地表 | 并行马蹄扰动带 | 骑兵方向性尘尾 | 骑队转向 | 黄昏前 | — | PLANNED |

## COMBINED LOOK DEPENDENCIES

- **Character Version：** NOT_APPLICABLE
- **Costume Version：** NOT_APPLICABLE
- **Makeup / Hair Version：** NOT_APPLICABLE
- **Validation Views：** NOT_APPLICABLE

## REFERENCE ROLE MAP

| Reference | Role | Allowed Influence | Must Not Override |
|---|---|---|---|
| Research CLM-001 / CLM-014 / CLM-017 | TOPOLOGY / EVIDENCE | 香积寺附近、沣水以东、长安西南的关系与地理边界 | 不推断精确寺塔、河道或城墙可见性 |
| World & Visual Bible V1 | TOPOLOGY / MATERIAL | A—G 功能区、地表和空气分层 | 不得由外部影片构图覆盖 |
| 外部电影参考组 | STYLE only | 军阵作为地形、空间层次的抽象方法 | 不复制具体战场、构图、色彩和建筑 |

## DERIVATION / EDIT CONTRACT

- **Parent / Edit Target：** 首先创建 Topology Plan；后续全部环境视图以批准版拓扑为父资产。
- **Change：** 各状态只改变人群、旗帜、足迹、遗物、时间和空气状态。
- **Preserve：** 地形轮廓、功能区关系、主战轴、东翼、固定尺度参照。
- **Constraints：** 不在状态派生中镜像、旋转或重造战场；带尘版本不得替代清洁拓扑资产。

## NEGATIVE CONSTRAINTS

- 无现存香积寺塔复刻、无清晰长安城墙、无宫殿、无寺院攻城。
- 无沙漠沙丘、江南水田、茂密森林、雪山或奇幻地貌。
- 无无来源烟雾、电影雾、体积光柱、发光尘埃和统一金色黄昏。
- 无现代道路、规则壕沟、火炮阵地、现代车辙或文字标牌。
- 无锁死的最终镜头构图。

## FILES AND PATHS

- Contract：`assets/locations/LOC-BATTLEFIELD-001/asset-contract.md`
- Planned asset root：`assets/locations/LOC-BATTLEFIELD-001/`
- `assets/locations/LOC-BATTLEFIELD-001/topology-plan-v001.png`，1672×941，用户生成并于 2026-10-01 归档。
- `assets/locations/LOC-BATTLEFIELD-001/topology-plan-v002.png`，1672×941，AI 定点修订并于 2026-10-01 归档。
- `assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.svg`，可编辑七区覆盖图，2026-10-01 归档。
- `assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png`，1672×941，覆盖图渲染预览，2026-10-01 归档。

## REVIEW RESULTS

### A029 B0尝试审核

- `state-b0-prebattle-v001.png`、`state-b0-prebattle-v002.png`、`state-b0-prebattle-v003.png` 均已留档，HOLD_GROUND_TEXTURE。
- 宏观地形、右侧通道与交叉路线基本连续，但空地微纹理呈过密重复卷曲/蹄形痕迹，V2移除微纹理与V3仅改天光均未解决；三版均不得作为战前基准。
- 已完成三次有明确假设的尝试，不继续对相同问题无界重试；后续应以局部更低复杂度地表试验解决，不降低B0验收标准。

- **Review Evidence：** SELF-REVIEWED
- **Files Inspected：** `topology-plan-v001.png`（原始像素）
- **Passed：** 开阔战场尺度成立；中央主战空间、前后两个后勤/阵位带与右侧宽阔骑兵通道均有可用基础；未出现寺塔、城墙、烟雾或密集战斗；色彩与地表粗粝度基本符合视觉圣经。
- **Failed：** 画面是斜向航拍环境概念，不是正交或清晰制作拓扑；A—G 七区不可直接辨认，唐军后方、燕军方向与真实东翼没有可靠制作标识；右侧道路过于“既成道路化”，部分双轴车辆具有近现代拖车观感；植被与岩石密度偏地中海荒原，关中黄土平原感不足；中央多条车辙路径过度随机，难以作为后续正反视图的唯一父资产。
- **Decision：** REWORK。保留为 `TOPOLOGY / ENVIRONMENT CANDIDATE`，不得作为批准拓扑父资产。

### V2 REWORK REVIEW

- **Files Inspected：** `topology-plan-v002.png`（原始像素）
- **Passed：** 开阔连续战场、中央主战轴和右侧东翼通道关系明显增强；现代拖车感、旗杆杂物和随机支路显著减少；空气、色彩和地表尺度保持中性，可继续承担空间开发父图。
- **Remaining：** 图中没有直接编码 A—G 七区和唐军后方/燕军方向；右侧仍是一条较明确的既成通道，因此不得直接宣称为历史测绘复原。
- **Decision：** GENERATED_PENDING_REVIEW。允许派生七区覆盖图；覆盖图通过前不升级为最终 APPROVED。

### A—G OVERLAY REVIEW

- **Passed：** A 前军、B 追击/溃退走廊、C 中军、D 退路/重组区、E 反攻推进轴、F 东侧骑兵走廊与 G 战后原阵位全部可辨；上、下、右分别标明燕军方向、唐军后方和真实东翼；G 明确与 A/B 共用同一地面。
- **Boundary：** 所有区域均为叙事制作拓扑，不宣称具体部队坐标、距离或历史测绘精度。
- **Decision：** READY_FOR_DERIVATION。允许制作正反环境视图和 B0/B3 状态派生，底图与七区关系不得随镜头重造。

## DOWNSTREAM USE

- 场景设计、分镜和镜头空间关系的唯一战场拓扑父资产。
- MAT-BATTLEFIELD-001、ENV-ATMOSPHERE-001、群体阵列与东翼骑兵资产的空间依赖。
- 不作为任何单一镜头的最终构图要求。

## CHANGE LOG

- V1 / 2026-09-30：建立 PLAN_ONLY 合同；锁定七区连续战场和清洁拓扑优先规则。
- V1 review / 2026-10-01：收到用户生成图并完成像素审核；状态改为 REWORK，要求保留开阔尺度，简化道路、车辆和植被，并建立清晰正交七区关系。
- V1.1 / 2026-10-01：完成 `topology-plan-v002.png` 定点修订；结构自审通过，等待七区覆盖图验证。
- V1.2 / 2026-10-01：完成可编辑 A—G 覆盖图与 PNG 预览；功能拓扑通过，可进入环境视图派生。
