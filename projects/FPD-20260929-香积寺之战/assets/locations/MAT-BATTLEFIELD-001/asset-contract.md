# ASSET CONTRACT

## IDENTITY

- **Asset ID：** MAT-BATTLEFIELD-001
- **Type：** MATERIAL
- **Working Name：** 战场地表与军事材质校准组
- **Version：** V1.2
- **Status：** BASE_PLATES_DERIVING
- **Purpose：** 统一土地、暗色金属、军用织物、皮革和木柄在人物、场景与道具中的重量、磨损、反光和污染响应。
- **Source Visual Bible Version：** World & Visual Bible V1
- **Evidence Status：** RESEARCH-INFERRED + CREATIVE CALIBRATION

## LOCKED FEATURES

- 所有材料必须保持物理差异，不能被统一灰滤镜或塑料光泽抹平。
- 地表由黄褐至灰褐细土、碎石和草根构成，包含压实区与松土区。
- 暗色金属不做镜面；高光只出现在受光角度、磨损边缘和接触区。
- 军用织物低光泽；汗湿后颜色变深、垂坠增加；积尘集中在暴露面和褶皱。
- 皮革接触区、弯折区和扣件周围磨亮，非接触区保持哑光。
- 木柄握持区颜色更深、表面更平滑；非握持区保持粗糙和尘土。
- 污渍、擦伤、汗、血和尘土必须有位置与来源，不平均铺满。

## VARIABLE STATES

- 土地：D0 干燥未扰动；D1 压实；D2 扬尘后；D3 战后沉降与重叠足迹。
- 金属：M0 使用旧；M1 积尘；M2 边缘擦损/局部污迹。
- 织物：T0 干燥使用旧；T1 汗湿；T2 积尘；T3 边缘撕裂。
- 皮革：L0 使用旧；L1 接触磨亮；L2 汗尘混合。
- 木柄：W0 干燥；W1 握持区汗尘加深。

## PRESENTATION CHOICES

- 使用中性、均匀、可比较的材料校准展示；不采用戏剧性背景和极端景深。
- 每种材料提供干净基准与剧情所需状态对照，不把所有状态合成一张不可分辨的“做旧板”。
- 另提供在 LLS-ORDER、LLS-ADVANCE、LLS-AFTERMATH 三种光线关系下的响应对照，但不生成镜头图。

## UNKNOWN / OPEN FIELDS

- 具体土壤粒径、含水量与历史当日状态。
- 唐军不同甲型的精确金属表面处理。
- 军用织物纤维、织法与染色工艺的最终选择。
- 皮革鞣制和木材种类；在专项研究前仅锁定可观察的物理表现。
- 血污用量与具体受伤位置由场景设计决定；本资产只定义材料吸收规则。

## REQUIRED VIEWS / PLATES

1. `material-ground-v001`：土地四状态。
2. `material-dark-metal-v001`：暗色金属三状态。
3. `material-military-textile-v001`：织物四状态。
4. `material-leather-v001`：皮革三状态。
5. `material-wood-grip-v001`：木柄两状态。
6. `material-light-response-v001`：三种 Look/Light State 下的统一对照。
7. `material-dust-interaction-v001`：尘土与皮肤、织物、金属、皮革、木柄的局部附着逻辑。

## CANONICAL FACE / BODY ANCHORS

- **Canonical Face Front Close-up：** NOT_APPLICABLE
- **Canonical Body：** NOT_APPLICABLE
- **Required Head Angles：** NOT_APPLICABLE
- **Required Full-body Six Views：** NOT_APPLICABLE

## VIEW MATRIX

| View / Plate | Required | Derivation Parent | File Path | Status | Review Notes |
|---|---|---|---|---|---|
| Ground states V1 | Yes | Contract V1 | `material-ground-v001.png` | REWORK_ARCHIVED | 前两栏可用；第三栏是明显偶蹄印而非马蹄，第四栏状态语义混杂 |
| Ground states V2 | Yes | V1 edit | `material-ground-v002.png` | SELF-REVIEWED_PASS | 偶蹄印已修为单蹄马印；第四栏仅作为战后扰动材料参考 |
| Dark metal states | Yes | Contract V1 | `material-dark-metal-v001.png` | SELF-REVIEWED_CANDIDATE | 三态可读；刀身仅用于表面，不锁定形制 |
| Textile states V1 | Yes | Contract V1 | `material-military-textile-v001.png` | REWORK_ARCHIVED | T1 汗湿差异不足 |
| Textile states V2 | Yes | V1 edit | `material-military-textile-v002.png` | CONDITIONAL_CANDIDATE | T1 较 V1 可读，但差异仍偏细微；仅供近景参考 |
| Leather states V1 | Yes | Contract V1 | `material-leather-v001.png` | REWORK_ARCHIVED | L1 磨亮范围过宽、整体偏油亮 |
| Leather states V2 | Yes | V1 edit | `material-leather-v002.png` | SELF-REVIEWED_CANDIDATE | L1 恢复大面积哑光；其余栏纹理有轻微漂移 |
| Wood grip states | Yes | Contract V1 | `material-wood-grip-v001.png` | SELF-REVIEWED_CANDIDATE | W0/W1 可读；与长刀 B 型柄联合审核待做 |
| Light response comparison | Yes | Approved base plates | — | BLOCKED_BY_PARENT | 不改变材料身份 |
| Dust interaction | Yes | Approved materials + ATM Register | — | BLOCKED_BY_PARENT | 尘土只在合理位置附着 |

## MATERIAL DETAIL PLATES

| Material / Detail | Scale / Location | Construction / Surface | Roughness / Reflection / Translucency | Weight / Drape / Movement | Clean / Wet / Dirty / Damaged State | File Path | Status | Review Notes |
|---|---|---|---|---|---|---|---|---|
| 战场土 | 地表至足迹尺度 | 细土、碎石、草根 | 高粗糙、低反射 | 可被脚步和马蹄扰动 | D0—D3 | — | PLANNED | 不表现成沙漠细沙 |
| 暗色金属 | 甲片、刀身、扣件 | 锻造/连接细节待研究 | 中高粗糙，窄高光，不透明 | 硬、重 | M0—M2 | — | PLANNED | 不镜面、不统一黑色 |
| 军用织物 | 衣层、旗布、缠带 | 织法待研究 | 哑光，局部透光仅限薄边缘 | 按层级软硬不同 | T0—T3 | — | PLANNED | 纤维尺度必须可信 |
| 皮革 | 带、马具、护具 | 缝合和扣合待研究 | 哑光，接触区中低光泽 | 有弯折记忆 | L0—L2 | — | PLANNED | 无均匀油亮 |
| 木柄 | 长刀握持区 | 木材和缠握结构待研究 | 粗糙，握持区较平滑 | 硬，有重量传递 | W0—W1 | — | PLANNED | 无塑胶纹理 |

## ENVIRONMENT DETAIL & STATE PLATES

| Zone / Layer | Ground / Wall / Ceiling / Dressing | Use Traces / Aging | Dust / Moisture / Smoke / Vegetation | Moving Elements | Time / Weather State | File Path | Status |
|---|---|---|---|---|---|---|---|
| LOC-001-A/G | 压实土、松土边界 | 旧足迹→重叠足迹 | 干尘→沉降；无烟 | 仅受人马和轻风驱动 | 午后→黄昏；天气 UNKNOWN | — | PLANNED |
| 人物接触层 | 甲、衣、皮肤、兵器 | 握持、摩擦、汗湿 | 局部积尘、无均匀灰膜 | 随动作接触变化 | 继承各 LLS | — | PLANNED |

## COMBINED LOOK DEPENDENCIES

- **Character Version：** NOT_APPLICABLE
- **Costume Version：** 将被 COST-ANXI-FRONT-001 等引用
- **Makeup / Hair Version：** NOT_APPLICABLE
- **Validation Views：** Front / Side / Material Close Comparison

## REFERENCE ROLE MAP

| Reference | Role | Allowed Influence | Must Not Override |
|---|---|---|---|
| World & Visual Bible V1 | MATERIAL | 锁定色彩关系、材料差异和损耗规则 | 不添加无来源湿润、光泽和颗粒 |
| Atmosphere Register V1 | MATERIAL / ENVIRONMENT | 尘土来源、附着和沉降 | 不把空气尘土画成统一材质噪点 |
| CLM-008 | EVIDENCE | 唐代甲胄类别与可见结构范围 | 不把墓葬武士俑直接当实战全套 |
| 外部电影参考组 | STYLE only | 重量、粗粝、使用痕迹的抽象目标 | 不复制调色、服装和材质结果 |

## DERIVATION / EDIT CONTRACT

- **Parent / Edit Target：** 每类材料先批准基础板，再派生污染和损伤状态。
- **Change：** 只改变使用痕迹、汗湿、积尘、擦损和光线状态。
- **Preserve：** 材料身份、结构、尺度、基础颜色和物理属性。
- **Constraints：** 状态派生不得把织物变皮革、金属变塑料、干土变泥地；不以全局滤镜模拟脏污。

## NEGATIVE CONSTRAINTS

- 无塑料甲、镜面黑甲、镀铬高光、均匀油亮皮革。
- 无全局胶片颗粒、锐化噪点、黑柔光晕或“做旧滤镜”替代材料细节。
- 无平均分布的血、泥、尘和划痕。
- 无无来源水珠、凝露、雨湿或烟熏。
- 无奇幻发光纹理和现代工业涂层。

## FILES AND PATHS

- Contract：`assets/locations/MAT-BATTLEFIELD-001/asset-contract.md`
- Planned asset root：`assets/locations/MAT-BATTLEFIELD-001/`
- `assets/locations/MAT-BATTLEFIELD-001/material-ground-v001.png`，1672×941，用户生成并于 2026-10-01 归档。
- `assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png`，1672×941，AI 定点修订并于 2026-10-01 归档。

## REVIEW RESULTS

- **Review Evidence：** SELF-REVIEWED
- **Files Inspected：** `material-ground-v001.png`（原始像素）
- **Passed：** 四栏均保持干燥黄褐—灰褐地表家族；颗粒、碎石、压实与松土差异清楚；无塑料光泽、烟雾、文字或大面积血污；第一栏适合作为未扰动干土地表参考，第二栏适合作为压实土参考。
- **Failed：** 第三栏主要印迹为偶蹄动物的分瓣足迹，不是骑兵马蹄；第四栏混有平行车辙、不同足迹和拖痕，但不足以清晰表达“战后沉降”；四栏光色与颗粒尺度差异略大，状态连续性不够；没有明确展示细尘只在近地短暂扬起的交互。
- **Decision：** REWORK。保留第一、第二栏的材料语言；重做第三、第四栏，不批准整张状态板。

### V2 REWORK REVIEW

- **Files Inspected：** `material-ground-v002.png`（原始像素）
- **Passed：** 前两栏语言保持；第三栏不再出现分瓣偶蹄印，已形成单蹄马印序列；整体色温、颗粒和尺度一致性提高。
- **Remaining：** 第四栏的军靴、木轮浅辙和拖痕仍偏弱，只能作为“扰动后沉降地表”参考，不作为足迹考古复原；暗色金属、织物、皮革和木柄板仍未制作。
- **Decision：** Ground plate SELF-REVIEWED PASS；资产总状态保持 GENERATED_PENDING_REVIEW。

## DOWNSTREAM USE

- LOC-BATTLEFIELD-001 地表细节、全部服装、甲胄、兵器、马具和空气交互的统一材料父资产。
- 生成资产审核时用于排除塑料光泽、平均污渍和无来源湿润。

## CHANGE LOG

- V1 / 2026-09-30：建立 PLAN_ONLY 材质校准合同。
- V1 review / 2026-10-01：收到用户生成图并完成像素审核；发现偶蹄印与状态语义错误，状态改为 REWORK。
- V1.1 / 2026-10-01：完成 `material-ground-v002.png`；偶蹄印硬伤已修正，地表板通过自审。
- V1.2 / 2026-10-02：新增暗色金属、军用织物、皮革、木柄四板。皮革 V1 的 L1 光泽问题通过 V2 修订；织物 T1 通过 V2 增强，但差异仍偏细微。材料光线响应和尘土交互仍缺。
