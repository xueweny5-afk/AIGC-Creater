# ASSET CONTRACT

## IDENTITY

- **Asset ID：** CHAR-ANXI-001
- **Type：** CHARACTER
- **Working Name：** 无名安西军士
- **Version：** V1.6
- **Status：** CANON_APPROVED_DERIVING
- **Purpose：** 建立贯穿 S001—S008 的普通军士身份锚点；后续所有头部角度、身体、服装组合和战损状态均从该身份派生。
- **Source Visual Bible Version：** World & Visual Bible V1
- **Evidence Status：** CREATIVE / HISTORICALLY PERMISSIBLE / USER-LOCKED CULTURAL IDENTITY

## LOCKED FEATURES

- 成年男性军士，约 30—40 岁的暂定年龄带；不是少年新兵，也不是老年统帅。
- 用户已确认其为安西军中的汉人老兵；这是本项目合成人物设计，不宣称对应史载个体。
- 耐力型、长期负重行军可成立的身体；不以健美肌肉或魁梧身高制造英雄感。
- 普通前军层级，无贵族饰物、统帅标志、传奇伤疤或主角光环式外貌。
- 面部必须适合“恐惧中仍能行动”的普通人，不按善恶或勇怯推断五官。
- 同一脸型、颅骨比例、眼距、鼻口关系、耳形和发际线跨全部状态不漂移。
- Canon Face 阶段只建立身份，不穿正式盔甲、不持兵器、不加入战场尘土和戏剧性表演。
- 正式服装识别锚点为后续 COST-ANXI-FRONT-001 的固定肩部修补；不属于裸脸身份特征。

## VARIABLE STATES

- C0 中性身份：无表情、无遮挡、清洁皮肤基准。
- C1 戒备：呼吸收紧、眼神寻找同列，不改变五官。
- C2 溃乱：汗、局部积尘、呼吸失控，无夸张哭喊。
- C3 推进：极度疲劳、局部轻伤、积尘增加，身份保持不变。
- C4 战后：动作停止、掌心压痕、尘汗仍在，不出现胜利笑容。

## PRESENTATION CHOICES

- Canon Face：平视、正面、无表情、无遮挡、均匀中性光、简单灰背景。
- Body Identity：中性站姿、基础内层服装，不穿正式甲胄，不持兵器。
- 头部角度和六视图必须从已批准 Canon Face / Body 逐张派生；不使用一次多格生成替代独立原图。
- 表情状态只制作 C1、C3、C4 三种剧情必要状态；不制作通用九宫格。

## UNKNOWN / OPEN FIELDS

- 精确年龄、脸型、眉眼、鼻口、耳形、肤色范围、发式和胡须。
- 身高、肩宽、四肢比例与惯用手。
- 是否有日晒分界、轻微旧伤等非叙事特征；不得擅自加入显眼伤疤。
- 基础内层服装的具体领型、织物和颜色，依赖 COST-ANXI-FRONT-001。

## REQUIRED VIEWS / PLATES

按依赖顺序逐步执行：

1. `canon-face-front-v001`：首个审批 Gate。
2. `head-left45-v001`、`head-left-profile-v001`、`head-right-profile-v001`、`head-right45-v001`：从批准正脸逐张派生。
3. `body-identity-front-v001`：基础内层、中性站姿，锁定体态比例。
4. 全身六视图：正面、左前 45°、左侧、背面、右侧、右前 45°，逐张派生。
5. `expression-c1-alert-v001`、`expression-c3-exhausted-v001`、`expression-c4-aftermath-v001`。
6. `detail-skin-hair-hands-v001`：皮肤、发际/头发、胡茬候选和手部基准。

## CANONICAL FACE / BODY ANCHORS

- **Canonical Face Front Close-up：** REQUIRED；可进入首个生成与审批 Gate。
- **Canonical Body：** REQUIRED；在 Canon Face 批准后制作。
- **Required Head Angles：** Front / Left 45° / Left Profile / Right Profile / Right 45°
- **Required Full-body Six Views：** Front / Left-front 45° / Left / Back / Right / Right-front 45°

## VIEW MATRIX

| View / Plate | Required | Derivation Parent | File Path | Status | Review Notes |
|---|---|---|---|---|---|
| Canon Face front V1 | Yes | Contract V1.1 | `canon-face-front-v001.png` | REWORK_ARCHIVED | 身份成立；高发髻、散发和偏锐表情待修 |
| Canon Face front V2 | Yes | V1 edit | `canon-face-front-v002.png` | APPROVED | 同一身份；用户于 2026-10-01 锁定为 Canon Face |
| Head left 45° | Yes | APPROVED Canon Face V2 | `head-left45-v001.png` | SELF-REVIEWED_PASS | 五官与耳形连续；发髻体积略增，后续角度必须收紧 |
| Head left profile | Yes | APPROVED Canon Face V2 | `head-left-profile-v001.png` | SELF-REVIEWED_PASS | 耳形、鼻口和发际线连续；发髻轮廓保持收紧 |
| Head right profile | Yes | APPROVED Canon Face V2 | `head-right-profile-v001.png` | SELF-REVIEWED_PASS | 独立派生，未以左侧镜像替代 |
| Head right 45° | Yes | APPROVED Canon Face V2 | `head-right45-v001.png` | SELF-REVIEWED_PASS | 五官比例和年龄连续 |
| Body Identity front | Yes | APPROVED Canon Face V2 | `body-identity-front-v001.png` | SELF-REVIEWED_PASS | 耐力型体态、手脚和基础衣层成立；近景脸仍以 Canon Face 为准 |
| Full-body six views | Yes | APPROVED Body Identity | `body-identity-front-v001.png`；`body-left45-v001.png`；`body-left-profile-v001.png`；`body-back-v001.png`；`body-right-profile-v001.png`；`body-right45-v001.png` | SELF-REVIEWED_PASS | 五张新图为用户提供；全身同一衣层和体型；近景脸仍以 Canon V2 为准 |
| C1 alert | Yes | APPROVED Canon Face V2 | `expression-c1-alert-v001.png` | SELF-REVIEWED_CANDIDATE | 眼神向侧方寻找同列；表情收紧，无新伤 |
| C3 exhausted | Yes | APPROVED Canon Face V2 | `expression-c3-exhausted-v001.png` | SELF-REVIEWED_CANDIDATE | 汗尘与额头、面颊小擦伤可读；这些伤痕若保留，C4 必须继承 |
| C4 aftermath | Yes | C3 state + Canon Face V2 | `expression-c4-aftermath-v001.png` | REWORK_ARCHIVED | 脸和神情可用，但额头与面颊擦伤消失、汗尘变少，违反单向状态；不能作正式 C4 |
| C4 aftermath V2 | Yes | C3 state + Canon Face V2 | `expression-c4-aftermath-v002.png` | CONTINUITY_PASS_CANDIDATE | 额角及双颊擦伤、汗尘延续 C3；神情仅微幅放松，与 C3 的情绪区分较弱，待跨状态并排复核 |
| Skin/hair/hands detail | Yes | APPROVED Face + Body | `detail-skin-hair-hands-v001.png` | SELF-REVIEWED_CANDIDATE | 发际、胡茬、双耳/手背/掌心参考；皮肤微纹偏强化，不作唯一肤质母图 |

## MATERIAL DETAIL PLATES

| Material / Detail | Scale / Location | Construction / Surface | Roughness / Reflection / Translucency | Weight / Drape / Movement | Clean / Wet / Dirty / Damaged State | File Path | Status | Review Notes |
|---|---|---|---|---|---|---|---|---|
| 皮肤 | 面部、颈部、手 | 自然毛孔、晒痕与局部纹理 | 局部皮脂/汗光，不均匀 | 随表情和呼吸变化 | C0 清洁→C4 汗尘 | — | BLOCKED_BY_PARENT | 禁止蜡像皮和统一灰脸 |
| 头发/胡茬 | 头部和面部 | 发式与胡须待身份决定后研究 | 低至中反射 | 受汗和头部防护影响 | 干→汗尘 | — | BLOCKED_BY_PARENT | 不用现代造型和夸张飘发 |
| 手 | 双手与掌心 | 正常解剖、握持磨损 | 皮肤局部汗光 | 能承受长刀双手握持 | 清洁→压痕/汗尘 | — | BLOCKED_BY_PARENT | 掌心压痕位置需与刀柄一致 |

## ENVIRONMENT DETAIL & STATE PLATES

| Zone / Layer | Ground / Wall / Ceiling / Dressing | Use Traces / Aging | Dust / Moisture / Smoke / Vegetation | Moving Elements | Time / Weather State | File Path | Status |
|---|---|---|---|---|---|---|---|
| Canon Identity | 简单灰背景 | 无 | CLEAN AIR | 无 | 中性光 | — | PLANNED |
| 状态测试 | 简单背景，不使用战场构图 | 汗、尘、轻伤分层 | 仅人物材料附着，不加环境雾 | 呼吸、头发和衣物小幅变化 | 继承状态需要 | — | BLOCKED_BY_PARENT |

## COMBINED LOOK DEPENDENCIES

- **Character Version：** CHAR-ANXI-001 V1 APPROVED 后锁定
- **Costume Version：** COST-ANXI-FRONT-001，尚未建合同
- **Makeup / Hair Version：** 如发式无法由 Character 合同充分管理，再建立独立资产；当前 DEFERRED
- **Validation Views：** Front / Side / Back；先正面，再侧面和背面

## REFERENCE ROLE MAP

| Reference | Role | Allowed Influence | Must Not Override |
|---|---|---|---|
| Character System V1 | IDENTITY | 普通成年军士、有限能动性、无名、非英雄化 | 不添加家庭、创伤、贵族和传奇身份 |
| World & Visual Bible V1 | IDENTITY / STYLE | 约 30—40 岁暂定、耐力体态、自然肤质 | 不由外部影片演员脸覆盖 |
| Research CLM-006 | EVIDENCE | 安西军参与及合成人物历史可容许性 | 不声称史料证明该个体或其固定兵种 |
| 外部电影参考组 | STYLE only | 疲惫、自然光、粗粝但真实的抽象目标 | 不复制演员肖像、妆发和服装 |

## DERIVATION / EDIT CONTRACT

- **Parent / Edit Target：** 创建 Canon Face；后续全部角度、身体和状态以批准资产为编辑母图。
- **Change：** 头部角度改变观看方向；状态板只改变表情、汗尘和疲劳；Combined Look 只增加批准服装妆发。
- **Preserve：** 颅骨比例、五官关系、年龄带、肤色范围、发际线、耳形、体态和手部身份。
- **Constraints：** 禁止从每个提示词重新生成“相似的人”；禁止用服装遮挡身份漂移；左右侧面分别派生，不以镜像替代。

## NEGATIVE CONSTRAINTS

- 无明星脸、网红脸、偶像少年、白净书生、健美英雄、伤疤反派脸或现代军人发型。
- 无夸张民族刻板特征、混血奇观化或未确认族属符号。
- 无正式盔甲、武器、旗帜、战场背景、烟尘和戏剧性轮廓光进入 Canon Face。
- 无面部遮挡、头盔、血污、咆哮、哭泣、英雄微笑和极端表情。
- 无多余手指、耳饰、纹身、现代修眉、美妆和皮肤磨皮。
- 无外部影视角色或演员的可识别相似性。

## FILES AND PATHS

- Contract：`assets/characters/CHAR-ANXI-001/asset-contract.md`
- Planned asset root：`assets/characters/CHAR-ANXI-001/`
- `assets/characters/CHAR-ANXI-001/canon-face-front-v001.png`，1536×1024，用户生成并于 2026-10-01 归档。
- `assets/characters/CHAR-ANXI-001/canon-face-front-v002.png`，1536×1024，AI 定点修订并于 2026-10-01 归档。
- `assets/characters/CHAR-ANXI-001/head-left45-v001.png`，1536×1024，从批准 Canon Face 派生，2026-10-01 归档。
- `assets/characters/CHAR-ANXI-001/head-left-profile-v001.png`，1536×1024，从批准 Canon Face 派生，2026-10-01 归档。
- `assets/characters/CHAR-ANXI-001/head-right-profile-v001.png`，1536×1024，从批准 Canon Face 独立派生，2026-10-01 归档。
- `assets/characters/CHAR-ANXI-001/head-right45-v001.png`，1536×1024，从批准 Canon Face 派生，2026-10-01 归档。
- `assets/characters/CHAR-ANXI-001/body-identity-front-v001.png`，1024×1536，从批准 Canon Face 派生，2026-10-01 归档。
- `body-left45-v001.png`、`body-left-profile-v001.png`、`body-back-v001.png`、`body-right-profile-v001.png`、`body-right45-v001.png`，均 1024×1536，用户提供并于 2026-10-02 归档。
- `expression-c1-alert-v001.png`、`expression-c3-exhausted-v001.png`、`expression-c4-aftermath-v001.png`、`detail-skin-hair-hands-v001.png`，均 1024×1536，用户提供并于 2026-10-02 归档；C4 V1 为返工留档。
- `expression-c4-aftermath-v002.png`，用户提供并于 2026-10-03 归档；伤痕连续性通过，情绪辨识仍待与 C1/C3 联合审核。

## REVIEW RESULTS

- **Review Evidence：** SELF-REVIEWED
- **Files Inspected：** `canon-face-front-v001.png`（原始像素）
- **Passed：** 正面、平视、无遮挡、简单灰背景和均匀校准光成立；年龄约 35—40 岁，汉人边军老兵身份可读；普通、克制、不像贵族或超级武将；脸部具有稳定识别点，真实毛孔、日晒色差、轻微不对称和短胡茬均符合合同；无盔甲、兵器、血污、文字和明显演员复刻；可作为后续头部角度的身份父图。
- **Failed：** 发髻偏高且有较多松散发丝，稍带通用“浪人/武侠”造型感；人物神情略显锐利，距离完全无表情有轻微偏差；正式锁定前需用户确认是否接受这两个特征。服装领口仅可视为临时内层，不得反向定义 COST-ANXI-FRONT-001。
- **Decision：** GENERATED_PENDING_REVIEW。技术自审通过，等待用户明确接受后方可升级 APPROVED。

### V2 REWORK REVIEW

- **Files Inspected：** `canon-face-front-v002.png`（原始像素）
- **Passed：** 人物身份、年龄、五官比例、肤质、胡茬、服装和光线保持连续；侧边散发减少，头发收束更整洁；眉眼与下颌略放松，仍保持边军老兵的警觉感。
- **Remaining：** 发髻仍位于后上方，但轮廓已不再被松散发丝强化；这属于可接受的创作性发式，需要用户决定是否锁为 Canon Face。
- **Decision：** APPROVED。用户于 2026-10-01 接受 V2；后续头部角度、Body Identity、表情和定妆均必须从该图派生。

### DERIVATION REVIEW V1

- **Head left 45°：** 同一人物身份成立，眼距、鼻口、下颌、耳形和肤质连续；发髻在斜角中略显更大，后续侧面不得继续放大。
- **Body Identity front：** 正面中性站姿、耐力型体态、完整手脚和基础衣层通过；脸在全身尺度下略显更硬朗，所有近景继续以 `canon-face-front-v002.png` 为身份最高优先级。
- **Additional head angles：** 左侧、右侧和右前 45°均保持同一颅骨、鼻口、耳形、年龄和肤质；左右侧分别独立派生，无镜像替代。
- **Decision：** 头部五视图与 Body Identity 正面均 SELF-REVIEWED_PASS，可继续派生身体角度、表情和定妆；不改变 Canon Face 的用户批准状态。

### USER IMAGE INTAKE REVIEW｜2026-10-02

- **Files inspected：** 桌面 `picture` 目录的 9 张 1024×1536 图片，已按内容映射到五张身体角度、C1/C3/C4 与细节板。源文件保留原位。
- **Passed for derivation：** 五张全身图与既有正面构成六视图；灰褐内层衣、腰带、绑腿、鞋、发髻、体态连续。C1 眼神变化克制；C3 疲劳、汗尘和小擦伤可读；细节板双手结构可读。
- **Risk：** 全身角度中的脸型和腰带褶皱有细微漂移，近景身份继续以 Canon V2 优先；细节板皮肤微纹偏强化。
- **Failed：** C4 图相较 C3 擦伤消失且尘汗减轻；不能作为同一时间线的战后最终状态。保留文件供返工参考，不放行下游。
- **Decision：** 五个身体角度 SELF-REVIEWED_PASS；C1/C3/细节为候选；C4 REWORK。资产整体未完成。

### C4 V2 REWORK REVIEW｜2026-10-03

- **Source：** 用户在对话中提供的单幅修订图；以 C3 为直接连续性参考，C4 V1 保留但不再用作执行参考。
- **Passed：** C3 画面左侧额角及双颊的小擦伤保留在对应位置；额头、眼周、两颊、颈部的汗光与尘痕未清除；脸型、发际和衣领保持同一身份。
- **Caveat：** 眉眼与嘴部仅微幅放松，战后情绪与 C3 疲劳状态的差别偏弱；在 C1/C3/C4 并排检视及后续定妆场景中仍需确认可读性。
- **Decision：** `expression-c4-aftermath-v002.png` 为 CONTINUITY_PASS_CANDIDATE，替代 V1 成为当前 C4 候选；尚非角色整套状态最终放行。

## DOWNSTREAM USE

- 主角头部角度、身体、服装组合、表情、战损状态和所有场景复用的身份母资产。
- 在 Canon Face 获批前，禁止生成主角正式定妆、六视图、场景图、分镜和镜头关键帧。

## CHANGE LOG

- V1 / 2026-09-30：建立 PLAN_ONLY 合同；识别出文化/族属身份为生成前阻断项。
- V1.1 / 2026-09-30：用户确认“安西军中的汉人老兵”；解除身份门槛，允许生成 Canon Face 首图。
- V1.1 review / 2026-10-01：收到用户生成图并完成像素审核；Canon Face 技术通过，等待用户锁定发髻与神情。
- V1.2 / 2026-10-01：完成 `canon-face-front-v002.png` 定点修订；身份连续性通过，等待用户锁定。
- V1.2 approval / 2026-10-01：用户确认继续；V2 正式锁定为 Canon Face，解除头部角度与 Body Identity 阻断。
- V1.3 / 2026-10-01：完成左前 45°与 Body Identity 正面；自审通过并记录发髻体积连续性限制。
- V1.4 / 2026-10-01：补齐左侧、右侧与右前 45°头部角度；五视图身份连续性自审通过。
- V1.5 / 2026-10-02：用户桌面 9 图入库；五个身体角度完成候选，C1/C3/细节入库，C4 因擦伤与尘汗回退标记返工。
- V1.6 / 2026-10-03：C4 V2 入库；C3→C4 的擦伤及汗尘连续性通过，跨状态情绪辨识待复核。
