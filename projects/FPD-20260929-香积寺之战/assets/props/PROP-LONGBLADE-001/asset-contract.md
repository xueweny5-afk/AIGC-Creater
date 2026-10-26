# ASSET CONTRACT

## IDENTITY

- **Asset ID：** PROP-LONGBLADE-001
- **Type：** PROP
- **Working Name：** 前军步兵长刀候选系统
- **Version：** V1.2
- **Status：** SELECTED_FOR_DEVELOPMENT
- **Purpose：** 为无名军士、李嗣业和前列军士建立同一兵器家族内可持用、可重复、可体现重量的步兵长刀视觉重构。
- **Source Visual Bible Version：** World & Visual Bible V1
- **Evidence Status：** DOCUMENTED FUNCTION / FORM OPEN / CREATIVE RECONSTRUCTION

## LOCKED FEATURES

- 史料安全表述是“步兵所持长刀/陌刀制度名称”，不宣称唯一出土实物形制。
- 兵器必须可由步兵双手持用，支持列阵推进、挥击、回收和长时间携行。
- 兵器有明显重量和惯性，但不得夸张到三米十公斤式奇观。
- 前军版本共享同一制造逻辑和比例家族，允许维护、缠握和磨损差异。
- 主角兵器在所有状态中保持同一身份；瘦高军士遗刀必须与主角版本可区分。
- 李嗣业版本可在同一体系中略宽重或维护度不同，但不能变成幻想英雄武器。
- 刀身只在正确受光角度出现窄高光；木柄和缠握区吸汗积尘。

## VARIABLE STATES

- W0 完整使用旧。
- W1 握持区汗尘加深、凹处积尘。
- W2 刃缘微小缺口、连接处擦损、局部污迹。
- W3 遗落地面；保持同一几何，不因无人持有而改变长度比例。
- CAND-A / CAND-B / CAND-C：最多三个并列重构候选，差异只集中在刀身—柄比例、刀尖和护手/连接结构。

## PRESENTATION CHOICES

- 第一轮只做中性道具研究板，不配历史人物、不放战场动作、不形成镜头构图。
- 每个候选以相同尺度、相同方向、相同中性背景呈现，旁置人体比例尺但不添加虚构文字铭文。
- 最终只批准一个基础兵器家族；未选候选保留 REJECTED/ARCHIVED 记录，防止下游混用。

## UNKNOWN / OPEN FIELDS

- 总长、刀身长度、柄长、重量和重心。
- 单刃/双刃、刀尖、护手和柄尾的唯一可靠形制。
- 757 年参战前军的具体装备一致程度。
- “陌刀”是否可直接用于每一名无名军士的视觉标签。
- 木材、缠握材料和金属表面处理的精确历史类型。

## REQUIRED VIEWS / PLATES

1. `candidate-comparison-v001`：2—3 个证据受控候选并列。
2. 每个候选的全形侧视、刃背关系、连接结构和柄尾视图。
3. `human-scale-hold-v001`：不穿正式服装的中性人体双手持握比例验证。
4. `material-detail-v001`：刀身、连接、木柄、缠握和刃口。
5. `state-w0-w3-v001`：完整、汗尘、轻损、遗落四状态。
6. `identity-variant-v001`：主角、李嗣业、瘦高军士遗刀的同家族差异。

## CANONICAL FACE / BODY ANCHORS

- **Canonical Face Front Close-up：** NOT_APPLICABLE
- **Canonical Body：** 仅需中性成人比例尺，不建立人物身份。
- **Required Head Angles：** NOT_APPLICABLE
- **Required Full-body Six Views：** NOT_APPLICABLE

## VIEW MATRIX

| View / Plate | Required | Derivation Parent | File Path | Status | Review Notes |
|---|---|---|---|---|---|
| Candidate comparison V1 | Yes | Contract V1 | `candidate-comparison-v001.png` | REWORK_ARCHIVED | 三件几乎同形，且整体滑向长柄偃月刀/关刀语汇 |
| Candidate comparison V2 | Yes | V1 edit | `candidate-comparison-v002.png` | SELF-REVIEWED_PASS | 三条结构路线已拉开；B 型推荐进入持握验证 |
| Candidate A structure | Yes | Candidate comparison V2 | — | ARCHIVED_NOT_SELECTED | 保留研究记录，不进入下游 |
| Candidate B structure | Yes | Candidate comparison V2 | — | READY_FOR_DEVELOPMENT | 建立全形、刃背、套筒和柄尾结构图 |
| Candidate B structure generated | Yes | Candidate comparison V2 middle B | `structure-b-detail-v001.png` | SELF-REVIEWED_CANDIDATE | 全形、刃背厚度、铆接套筒与柄尾可读；几何母图仍为候选比较 V2 中 B 型，联合审核后再晋升 |
| Candidate C structure | Optional | Candidate comparison V2 | — | ARCHIVED_NOT_SELECTED | 保留研究记录，不进入下游 |
| Human scale/hold | Yes | Candidate B | `human-scale-hold-b-v001.png` | SELF-REVIEWED_PASS | 双手间距、重心和全长可用；不作为结构母图 |
| Formation spacing | Yes | Candidate B + hold validation | `formation-spacing-b-v001.png` | SELF-REVIEWED_PASS | 三人同列可保持平行刀向与实用间距 |
| Material detail | Yes | Candidate B + MAT-BATTLEFIELD-001 | — | READY_FOR_DEVELOPMENT | 材质不改变结构 |
| W0—W3 states | Yes | APPROVED base | — | BLOCKED_BY_PARENT | 所有状态从同一母资产派生 |
| Character variants | Yes | APPROVED base | — | BLOCKED_BY_PARENT | 差异受控，不重造新武器体系 |

## MATERIAL DETAIL PLATES

| Material / Detail | Scale / Location | Construction / Surface | Roughness / Reflection / Translucency | Weight / Drape / Movement | Clean / Wet / Dirty / Damaged State | File Path | Status | Review Notes |
|---|---|---|---|---|---|---|---|---|
| 刀身 | 全长与刃口 | 锻造细节仅作受控重构 | 中等粗糙、窄高光、不透明 | 体现重量和惯性 | W0—W2 | — | PLANNED | 不镜面、不奇幻纹样 |
| 刀柄 | 双手握持区 | 木质基础，连接结构待研究 | 高粗糙；握持区较平滑 | 硬，有重心传递 | W0—W3 | — | PLANNED | 不使用现代防滑胶纹 |
| 缠握 | 局部握持区 | 织物/皮革候选 | 哑光，吸汗 | 有压缩和磨损 | W0—W2 | — | PLANNED | 不做装饰性彩带 |
| 连接 | 刀身与柄部 | 金属套、铆接或其他候选 | 低光泽 | 必须承受挥击受力 | W0—W2 | — | PLANNED | 不允许结构悬空 |

## ENVIRONMENT DETAIL & STATE PLATES

| Zone / Layer | Ground / Wall / Ceiling / Dressing | Use Traces / Aging | Dust / Moisture / Smoke / Vegetation | Moving Elements | Time / Weather State | File Path | Status |
|---|---|---|---|---|---|---|---|
| 中性资产板 | 简单背景与尺度参照 | 使用旧痕迹 | 无空气介质 | 无 | 中性校准光 | — | PLANNED |
| 战后遗落状态 | MAT-BATTLEFIELD-001 地表 | 接触点和落地擦痕 | 轻尘沉降；无烟湿 | 仅松散纤维轻动 | 黄昏关系由下游继承 | — | BLOCKED_BY_PARENT |

## COMBINED LOOK DEPENDENCIES

- **Character Version：** CHAR-ANXI-001、CHAR-LISIYE-001、GROUP-TANG-FRONT-001 后续版本
- **Costume Version：** COST-ANXI-FRONT-001、COST-LISIYE-001
- **Makeup / Hair Version：** NOT_APPLICABLE
- **Validation Views：** 双手持握侧向、正斜向、回收状态

## REFERENCE ROLE MAP

| Reference | Role | Allowed Influence | Must Not Override |
|---|---|---|---|
| CLM-003 / CLM-007 | EVIDENCE | 长刀、步兵持用、如墙推进的功能 | 不推断唯一尺寸与形制 |
| CLM-013 / CLM-016 | EXCLUSION / LIMIT | 记录长度重量争议和未证阵法 | 不使用三米十公斤、两千人、三排半跪作为硬事实 |
| MAT-BATTLEFIELD-001 | MATERIAL | 金属、木柄、缠握和积尘响应 | 不改变武器几何 |
| 外部影视参考 | STYLE only | 重量与受力的抽象要求 | 不复制任何标志性兵器 |

## DERIVATION / EDIT CONTRACT

- **Parent / Edit Target：** 先生成候选比较；选定后建立 Base Prop；所有人物版本和损伤状态从 Base Prop 编辑派生。
- **Change：** 候选阶段只改变结构比例；状态阶段只改变磨损、积尘和局部维护差异。
- **Preserve：** 选定后的总比例、刃柄连接、刀尖、护手/套筒和材料身份。
- **Constraints：** 不因角色身份把兵器放大成英雄武器；不在状态派生中镜像或变形。

## NEGATIVE CONSTRAINTS

- 无关刀、薙刀、三尖两刃刀、欧洲长柄斧、幻想巨剑或现代刀具特征。
- 无夸张三米长度、十公斤视觉奇观、宽到不可挥动的刀身。
- 无龙纹、发光纹、宝石、金饰、华丽铭文和现代机加工质感。
- 无悬空连接、弯曲木柄、错误双手数量或不可持用重心。
- 无战斗场景、血浆构图和电影镜头表现。

## FILES AND PATHS

- Contract：`assets/props/PROP-LONGBLADE-001/asset-contract.md`
- Planned asset root：`assets/props/PROP-LONGBLADE-001/`
- `assets/props/PROP-LONGBLADE-001/candidate-comparison-v001.png`，1672×941，用户生成并于 2026-10-01 归档。
- `assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png`，1672×941，AI 结构重构并于 2026-10-01 归档。
- `assets/props/PROP-LONGBLADE-001/human-scale-hold-b-v001.png`，1672×941，B 型双手持握验证，2026-10-01 归档。
- `assets/props/PROP-LONGBLADE-001/formation-spacing-b-v001.png`，1672×941，B 型三人列阵间距验证，2026-10-01 归档。

## REVIEW RESULTS

- **Review Evidence：** SELF-REVIEWED
- **Files Inspected：** `candidate-comparison-v001.png`（原始像素）
- **Passed：** 展示背景中性、无文字水印；人体比例轮廓干净；金属、木柄与缠握材质基本可辨；三件道具处于同一展示尺度。
- **Failed：** 三个候选在刀身、刀尖、套筒和总比例上几乎没有有效差异，未完成候选比较任务；全部呈明显上弯长刃和长套筒，接近后世长柄偃月刀/关刀视觉语汇，触发合同明确排除项；兵器总长和刀身比例偏夸张，人体轮廓也呈现代健美体型；下端重复包缠缺乏功能依据；图像不能支持选择陌刀/步兵长刀的证据受控路线。
- **Decision：** REWORK。当前版本不得进入人物持握、阵列或场景资产；下一版必须显著缩短并拉开候选结构差异。

### V2 REWORK REVIEW

- **Files Inspected：** `candidate-comparison-v002.png`（原始像素）
- **Passed：** 三候选在刃宽、刀身长度和重心上已形成有效差异；偃月刀/关刀式大弧刃和夸张上挑基本消除；总长回到约等身至略高于人体的可用区间；铁木材质和套筒结构清楚。
- **Remaining：** 人体比例剪影仍略健壮，只能作尺度尺；三种形制均为项目视觉重构，不是确证陌刀复原；必须通过双手持握、挥击回收和列阵间距验证后再批准基础兵器家族。
- **Recommendation：** 选择 B 型进入 `human-scale-hold-v001`。它的较短宽刃最容易读出重量，同时较少接近关刀或长柄剑。
- **Decision：** CANDIDATE_SELECTION_PENDING；V1 禁止下游使用，V2 可用于选择与验证。

### B CANDIDATE VALIDATION

- **Selection：** 用户于 2026-10-01 接受继续推进，按审核推荐选择 B 型作为开发基础。
- **Passed：** 单人双手握持时两手间距、站姿和重心可解释；约等身至略高的总长未形成奇观化；三人同列时兵器可维持平行方向和必要横向间距。
- **Continuity Warning：** 动作验证图的刀尖弧度较结构候选板略有漂移。`candidate-comparison-v002.png` 中的 B 型仍是唯一几何母图；两张验证图只证明人体工学与间距，不得反向覆盖刀身几何。
- **Decision：** SELECTED_FOR_DEVELOPMENT。允许继续制作 B 型结构细节和角色版本；完成连接、材料和 W0—W3 状态前不标记最终 APPROVED。

## DOWNSTREAM USE

- 无名军士、李嗣业、前军群体和瘦高军士遗物的共同兵器父资产。
- 队列动作、持握和近身碰撞设计的尺度依据。
- 任何下游文字只能称“本项目视觉重构候选”，不得宣传为陌刀唯一历史复原。

## CHANGE LOG

- V1 / 2026-09-30：建立 PLAN_ONLY 合同；采用并列候选而非单一断言。
- V1 review / 2026-10-01：收到用户生成图并完成像素审核；因候选同形和关刀化，状态改为 REWORK。
- V1.1 / 2026-10-01：完成 `candidate-comparison-v002.png`；结构自审通过，推荐 B 型进入持握验证。
- V1.2 / 2026-10-01：B 型完成单人双手持握及三人列阵间距验证，状态改为 SELECTED_FOR_DEVELOPMENT。
- V1.2 supplement / 2026-10-04：生成 B 型全形结构细节板，候选入库；李嗣业持刀图归 COST-LISIYE-001，刀尖轻微漂移不反向覆盖母图。
