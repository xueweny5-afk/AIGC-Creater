# AIGC FILM PRODUCTION PIPELINE

**Version:** V1.27 Scoped Delivery & Recovery Evidence  
**Updated:** 2026-10-18  
**Purpose:** 用一套可追溯、可暂停、可回退的阶段接口，把模糊创意发展为最终影片。创作主版本与模型执行版本始终分离。

## Pipeline principles

**入口交付范围：** 新需求先明确是否仅交付剧本、分镜文字、提示词等内容，由 RunningHub 或其他平台承担图片/视频生成与剪辑。范围未说明时优先询问并推荐该分工；已明确则沿用。仅内容交付按相关创作阶段保证故事、镜头和提示词一致，不以完成全部生产阶段或回传真实媒体作为文本交付前提；需要真实资产、画面或样片才能验证的项目保持待验证，不能标记相应生产 Gate 已通过。进入实际制作后，再从最早未通过的生产关口推进。此范围选择先于下文的手动/自动生成方式，内容交付本身不意味着等待用户生成后继续制作。

1. **Intent first:** 先保护用户意图，再扩展创作。
2. **Research before assertion:** 历史、现实、文化和科学信息先研究，再进入叙事。
3. **Human-readable master:** Project Brief、Treatment、Screenplay、Visual Bible 和 Director Plan 是主版本；模型 Prompt 只是后期编译结果。
4. **Explicit state:** 全程使用 `LOCKED / OPEN / ASSUMED`，研究内容另标 `RESEARCHED / DISPUTED / UNKNOWN`。
5. **One stage, one job:** 每个 Skill 只做一个可交接阶段；缺口返回正确上游，不在下游偷偷修补。
6. **Format-aware scope:** 单支短片、独立单元系列、共享世界系列和连续剧情剧集使用不同的延续边界。
7. **Approval gates:** 世界观、人物造型、剧本、导演方案和分镜等高成本节点在进入下一阶段前保持可审阅。
8. **Asset before shot generation:** 人物、服装、场景、道具与空间拓扑先形成可复用资产合同，再进入生产级分镜和逐镜头生成。
9. **Static before motion:** 先用静态分镜验证叙事、构图、身份和空间，再设计运动；不让视频生成承担未解决的导演决定。
   - **Composition before populated frame:** 复杂或关键镜头先建立并审核 `Composition Guide`，只锁机位、景别、主体占比、前中后景、负空间、遮挡和屏幕方向；再以纯场景底图、身份、服装和道具参考生成正式 Frame。构图图不承担身份、美术和最终像素批准。
10. **Pilot before scale:** 存在高风险镜头时，先用最小技术样片验证身份、动作、空间或特效，再批量生产。
11. **One shot, one primary job:** 每个生成 Clip 只承担一个主要叙事任务和一个主要动作层；复杂高潮拆成可连续的小镜头。
12. **Evidence-led iteration:** 失败必须记录可见证据、责任层、修改假设和实际变化字段；不靠堆叠风格词或无界重试碰运气。
13. **Contract before expansion:** 故事扩写前先固定原始事实、必须呈现、允许连接和禁止改写；增加镜头只拆解已有因果，不自动增加转折或戏剧配额。
14. **Evidence-bounded space:** 场景与镜头明确区分 `VISIBLE / INFERRED / UNKNOWN`；单张参考图不能证明不可见空间，画面左右不能代替世界坐标。
15. **Dependency-aware continuity:** 人物、物件、知识与动作状态使用稳定 ID 和前后状态传递；先验证改变状态的关键帧或镜头，再制作依赖它的内容。
16. **Preserve approved work:** 已批准资产、画面和 Take 默认冻结；返工只修改可见失败及其受影响依赖，不以重新生成整批替代诊断。
17. **Sequence before scale:** 多镜段落先用顺序 Contact Sheet 和带临时时长/声音的 Animatic 验证观看体验，再进入批量视频生成。
18. **Version-bound references:** 每镜必须绑定人物、服装、妆发、场景、道具、材质与环境状态的确切 Asset ID 和版本；工作名或模糊描述不能作为生产引用。
19. **Reference semantics before prompting:** 外部参考先转换为 `HARD_ANCHOR / SOFT_REFERENCE / EXCLUSION`；硬锚点只能来自已批准的项目合同，不能从风格参考反推身份、服装、空间或史实。
20. **Inherit look states:** 核心场景先建立可追踪的 `Scene Look & Light State ID`；镜头、分镜和运动默认继承，只记录有剧情触发的偏差与变化。
21. **Coverage receipt, compact execution:** Prompt Adapter 用十三项覆盖回执证明信息被映射、降级或退回；可复制 Prompt 仍保持模型原生、紧凑，不把检查表机械拼入正文。
22. **Purpose-routed prompt library:** 人物/服装/场景资产、静态镜头、动态表演、材质空气和局部返工使用同一共享提示词库的不同模块；各阶段只加载与职责相符的模块，不用一个万能长 Prompt 混合创作、资产、分镜和视频执行。
23. **Emotional thesis before aesthetic treatment:** Project Brief 先记录创作者真正想触达的关系、经验和核心意象；视觉、镜头、声音与节奏必须回指该情感命题，不用模型技巧制造替代性的“感动”。
24. **Narrative rhythm and physical atmosphere:** 叙事时期先形成 Narrative Look Arc，场景空气介质必须有来源、分布和驱动力；Scene → Shot → Animatic → Post 使用 Rhythm Map 传递压力、能量、必要反应/静默和变化触发，快慢不由固定镜长或音乐模板决定。
25. **Evidence before reusable advice:** Prompt、模型或参数经验必须能追到真实输入、Take、QC 和改变变量；单次漂亮结果只记 Local Observation。只有有边界的受控比较或重复证据才能提升为项目/模型/跨项目模式，模型升级或相反证据会触发复核或退役。
26. **One source, derived execution views:** Screenplay、Visual Bible、Shot、Frame、Motion 与资产合同是事实源；逐镜执行卡、整合提示词手册和批次清单是由这些事实源编译的交付视图，不得反向成为独立创作主版本。
27. **Change impact before downstream reuse:** 已批准上游发生变化时，先登记版本差异和影响范围，再将下游标为 `CURRENT / STALE / BLOCKED / RECOMPILE`；只重编译或返工真正受影响的依赖。
28. **Attention and response continuity:** 每镜明确 `MAIN / SUPPORT / HOLD`，并在适用时传递 `PREVIOUS RESIDUE → TRIGGER → DELAY → VISIBLE CHANGE → HANDOFF`；Prompt 只压缩这条已批准的注意力与表演链，不自行补“生命感”。
29. **Hypothesis-led pilots:** 技术样片按具体失败假设组织，尽量一次只改变一个变量；样片结论只覆盖实际测试的模型、入口、镜头类型与风险，不从单个漂亮结果外推整片。
30. **Methods accelerate, never overrule:** 经验证的 `film-method-*` 只向 Method Adoption Receipt 授权的字段提供专业覆盖；优先级始终是用户当前要求、项目批准合同、Method、公共流程、通用模型经验。
31. **Open method taxonomy:** Method 按可复用制作机制建立、组合、拆分或退役，不维护封闭的题材/风格分类，也不把参考作品独有表达固化成模板。
32. **Execution route at project start:** Project Brief 分别记录资产图片、分镜/关键帧图片、镜头视频的默认执行方式 `USER_GENERATE / AUTO_GENERATE / OPEN`，以及手动执行的交接位置。方式只决定谁操作生成工具，不改变阶段顺序、资产版本和审核门；单批可经用户明确要求覆盖，并记录在该批次中。

## Stage map

| # | Stage / Skill | Primary Input | Primary Output | Status |
|---|---|---|---|---|
| 00 optional | `film-source-ingestor` | 用户提供的小说、故事、剧本、纪实材料或长文原作 | `Source Intake` + `Source Coverage` | Implemented + Validated |
| 01 | `film-project-director` | 模糊想法、限制、参考意图、可选 Method | 含 Emotional Thesis / Core Image Seed / Method Adoption 摘要（适用时）的 `Film Project Brief` | Implemented + Validated |
| 02 | `film-researcher` | Project Brief、Obsidian 范围、公开来源 | `Research Pack` + `Source Index` | Implemented + Validated |
| 03 | `film-story-developer` | Brief + Research | `Story Blueprint` | Implemented + Validated |
| 04 | `film-character-developer` | Blueprint + Research | `Character System` | Implemented + Validated |
| 05 | `film-treatment-developer` | Blueprint + Characters + Research | `Film Treatment` | Implemented + Validated |
| 06 | `film-screenplay-developer` | Approved Treatment + Characters | `Screenplay Master` + `Screenplay Register` | Implemented + Validated |
| 07 | `film-world-visual-designer` | Brief + Research + Screenplay | 含 Narrative Look Arc / Atmospheric Medium State 的 `World & Visual Bible` + `Asset Requirements` | Implemented + Validated |
| 08 | `film-asset-designer` | Visual Bible + Character System + Screenplay | 按用途的身份母版、必要视图与状态、独立服化道、场景/材质/环境资产及批准范围 | Implemented + Validated |
| 09 | `film-scene-director` | Screenplay + Visual Bible + asset use scope | `Scene Design Pack`：行动回应链、空间/艺术调度、跨场承接与 Scene Review；空间敏感场景含方位卡 | Implemented + Validated |
| 10 | `film-shot-director` | READY Scene Design Pack + scoped approved asset uses | `Shot List` + `Shot Continuity Ledger`：观看立场、构图关系、Scene Beat 覆盖与 Shot Review；在方位卡上叠加机位与轴线 | Implemented + Validated |
| 11 | `film-storyboard-designer` | Shot List + scoped approved asset uses | Composition Guides + Storyboard / Keyframes：瞬间与注意力可读性、State Pair Check、单帧/顺序审核 + Animatic / Rhythm Map | Implemented + Validated |
| 12 | `film-motion-designer` | Approved Storyboard + Shot List + scoped asset/artistic rules | 状态连接、接触节点、分层时间/注意力与转场运动规格 + Motion Review | Implemented + Validated |
| 13 | `film-prompt-adapter` | Visual/Shot/Motion contracts + entry-specific model profile；草稿注明待验证 | 意图保留映射、模型专用 Prompt Packages / Unit Cards、Prompt Review 与分范围执行状态 | Implemented + Validated |
| 14 | `film-generation-producer` | Per-unit ready Prompt Packages + scoped inputs + authorization | Takes、Unit/Batch 预算账目、恢复/重试与手动回传记录、样片范围证据 | Implemented + Validated |
| 15 | `film-continuity-qc` | Real Takes + current scoped creative/artistic contracts | 正确性/表达审核、Take/Boundary/Sequence 分范围结论、问题诊断与新版本复核、选片 | Implemented + Validated |
| 16 | `film-post-production-director` | QC-selected 或 USER-APPROVED takes + scoped creative/artistic and sound intent | 可追溯声画 EDL、艺术规则与修复记录、最终候选 Post Review 和 PICTURE_LOCKED 回执 | Implemented + Validated |
| 17 | `film-master-delivery` | Actual PICTURE_LOCKED + scoped delivery specs；计划可列待补 | 本次所需母版/变体、逐文件与整包验收、表达保护及归档恢复证据 | Implemented + Validated |

Stage 09 按实际行动段组织事件/持续状态、察觉、行动回应、变化或保持与承接，不强制对抗、移动或策略转折。跨场继承已批准时间逻辑，物理与艺术变化分别依据对应规则。Scene Review PASS、无阻断项且当前所需 P0 用途在批准范围内才标 READY FOR SHOT DESIGN；内容稿可带待验证依赖交付，文字审阅不等于表演、画面或动态验证通过。

Stage 10 先确定观看立场和信息先后，再把 Scene Beat 投影为构图、注意力、静止/运动及切点；继承批准的艺术空间与时间规则，创作意图和生成风险分别评估。Shot Review PASS、当前范围上游就绪、资产具体用途有批准证据且无阻断项才为 READY FOR STORYBOARD。未产生的关键帧只登记 Planned Frame Need / State Dependency，由 Stage 11 创建后绑定实际版本，不构成 Stage 10 循环前置；仅内容稿可用 SHOT EXPLORATION 带待验证依赖交付，不代表画面或模型效果通过。

Stage 11 继承观看立场、构图和艺术规则，选准代表瞬间，分别检查画面正确性与表达。关键状态对的静态衔接不代表运动可行；文字计划、单帧、顺序画面和 Animatic 预览各记范围与证据。仅内容交付可保持 PLANNED、列待补参考/构图图与执行依赖；实际生成和放行再检查批准用途。多镜段落 READY FOR MOTION DESIGN 须所需帧及顺序通过，并有确切 Animatic 实际预览的完整播放审核或用户明确批准；计划 PASS / NOT_RENDERED 不代替播放验证。单镜不适用多镜 Gate 时说明理由。

Stage 12 从已知状态规划必经动作/接触节点和保持项，区分当前输入与目标尾帧；无尾图但已有批准结束状态时可先设计，不强制每镜首尾图。持续动作、等待和观察允许 HOLD，人物/摄影机可按批准方案同步，阶段主时间线闭合而不累加并行层时长。物理响应与艺术变化分别继承依据。Motion Review PASS、当前范围上游/用途证据就绪且无阻断项才 READY FOR PROMPT ADAPTATION；MOTION EXPLORATION 可进入提示词内容草稿，待验证依赖明示，不标生成就绪。文本可理解不代表实际运动或模型能力已验证。

Stage 13 以实际参考/职责/顺序、Prompt 与已核实控制项共同承载观看立场、构图、注意力、停顿和结束状态；分别编译图片瞬间、视频持续/变化及物理/艺术规则。Profile 按平台、版本、任务入口、输入模式及账户/地区核实，不从同名模型外推。CONTENT DRAFT 可完整交付文字和待验证项，卡保持 NOT_READY；生产 Unit 须当前源版本/用途/依赖就绪、Profile VERIFIED、Prompt Review PASS 且回执无未解决冲突，并遵守 Pilot Gate。文本审核不代表模型效果，混合包不整体冒称就绪。

Stage 14 逐 Unit 拒绝内容草稿和未就绪依赖，核对具体入口与用途批准；已有授权范围内不重复询问。Pilot 检验创作意图与可观察风险，PILOT_VALIDATED 或用户明确 USER_ACCEPTED_RISK 只放行对应范围。预算区分尝试、在途预留、实际费用与未知账目，恢复区分查询、下载和新生成；未知任务不盲目重提，同类失败无新依据则停止/返回。USER_HANDOFF 未回传不伪造生成，人工批准按文件/版本/范围记录，不冒充 QC_PASS 或全序列通过；只重做失败及受影响依赖。

Stage 15 按媒体类型取证：图片看原图，视频完整播放、适用声音实际听取；缺媒体或检查能力只交计划/缺口并保持未评估。正确性与观看立场、注意力、必要停顿及艺术表达分别核对，Take/Boundary/Sequence 不互相外推。源变更先查实际影响，无关变更经上游确认并刷新引用后可复用，不因版本号变化重生成。问题分开可见症状与根因假设，后期可修必须保护构图、动作、停顿和艺术规则；只有新版本实际复核才关闭问题，人工批准继续独立按范围记录。

Stage 16 剪辑按批准观看顺序保留立场、注意力、静默、感知和艺术变化，不强制每切新剧情；声音职责与进入/退出明确，调色/VFX 不抹掉批准风格。EDL 绑定确切素材版本、源/时间线时间基、声音偏移和变速/裁切修改理由。仅内容交付可完成 POST PLAN 与待补计划；实际锁片须最终确切渲染文件的两项全片声画审核及问题/权利门通过，旧候选证据不能套用新版本。状态统一 PICTURE_LOCKED，与 Stage 17 接口一致，不等于平台版本交付或发布。

Stage 17 按用途/接收对象定义 Required/Optional 与来源规格，未知平台要求保持未核实。画幅与声画转换保留立场、留白/遮挡、动作、静默和艺术规则；逐文件绑定 checksum、实际规格与播放证据，修复后验证新版本。所有 Required 文件及约定归档要求满足才整包合格，部分通过只交列明文件。归档列相对依赖、软件/插件、缺失项与恢复步骤，NOT_TESTED/PARTIAL/VERIFIED 只按实际测试范围声明，不承诺模型复现。无锁片仍可交 DELIVERY PLAN，本地导出/归档不自动等于上传发布。

## Cross-stage supporting skills

`film-atmosphere-designer` 是 Stage 07–15 的辅助 Skill，不新增制作阶段。核心空间存在显著、重复、会变化或连续性敏感的灰尘、蒸汽、烟、雾、湿气、花粉、飞沫等介质时，它在 `visual-development/atmosphere-state-register.md` 建立稳定状态；Visual Bible、Asset、Scene/Shot、Motion、Prompt 和 QC 按职责引用。简单清洁空气或单一低风险状态直接写入 Visual Bible，不强制创建额外文件。

`film-generation-pattern-curator` 是 Stage 13–15 的学习辅助 Skill，不新增制作阶段。原始成功/失败案例保存在 `projects/<project-id>/generation/learning/`；只有具有真实媒体、QC、模型版本、输入模式、Changed Variable 和适用边界的结论，才去项目化提升到 `pipeline/knowledge/generation-pattern-catalog.md`。公共模式不能覆盖当前项目合同、当前 Model Profile 或 Pilot Gate。

`film-video-method-curator` 是 Stage 01–17 的开放式方法学习与复用辅助 Skill，不新增制作阶段。它把用户认可的参考视频拆成 Study 与候选 Method Pack，经真实 Pilot 和 QC 后才创建 `film-method-<slug>` 专项 Skill。项目通过 `direction/method-adoption.md` 锁定 Method ID、版本、范围、受控字段、项目保护字段、冲突裁决和 Pilot；未采用的阶段不加载该 Method。

两类学习不可混用：跨阶段的叙事、视觉、镜头、动态、声音和专项验收回到 `film-video-method-curator`；特定模型、Prompt、参数和参考输入的受控比较回到 `film-generation-pattern-curator`。

### Optional craft passes

以下 Skill 按项目需要嵌入已有阶段，不增加 Stage 或批准门，也不替代该阶段的主 Skill。只把其结果写回对应的主合同或项目阶段目录；没有触发条件时直接跳过。

| Skill | 触发与插入位置 | 交接结果与边界 |
|---|---|---|
| `film-realist-prompt-designer` | 项目明确需要现实主义、生活流或纪实感时，在 Stage 07 建立风格基线与少量叙事变体；场景/镜头需要具体化时复用同一基线 | 模型中立的摄影、美术与材质意图写入 Visual Bible 的 Look Arc / Scene Look & Light State；Stage 13 `film-prompt-adapter` 才编译模型语法。影视参考先经 Method Curator 拆解，不能把片名或风格词直接当生产合同 |
| `film-character-model-sheet-designer` | Stage 08 中，需要角色身份多视图、头部角度或设定板返工时 | 根据批准的身份锚点与 Character Asset Contract 设计独立视图、提示词和像素审核标准；`film-asset-designer` 负责实际资产、版本、manifest 与批准。预览合板不能独自成为 Canon Face/Body |
| `film-micro-performance-designer` | Stage 09 的关键反应、克制表演或抽象情绪需要动作化时建立 Performance Beat；Stage 10–13 只投影或压缩其已批准动作链 | Scene 保留目标/触发，Shot 检查景别可读性，Storyboard 选可见瞬间，Motion 排列时间链，Prompt 编译当前 Clip；不改人物目标、对白、镜头或结局。无基线或触发时返回 Scene / Screenplay |
| `film-storyboard-lighting-designer` | Stage 11 的构图与动作状态至少已审为 `COMPOSITION ONLY / STATE ONLY`，且有批准的 Look/Light State 与独立 Frame 原图时；在 G4 前执行需要的 Lighting Pass | 逐帧继承世界光源、画面投影、人物与环境受光及跨镜连续性；编辑结果作为同一 Frame ID 的新版本返回 Storyboard Review。缺少上游光线合同时返回 Stage 07/09；不得借灯光 Pass 改构图、身份或场景拓扑 |

常见执行顺序是 `Visual Bible（现实主义基线，若适用）→ Asset（角色多视图，若需要）→ Scene / Shot（关键 Performance Beat，若需要）→ Storyboard 构图与状态 → Lighting Pass（若需要）→ Storyboard 顺序审核与 Animatic → Motion → Prompt → Pilot / Generation → QC`。四项辅助产物都沿用现有 G3/G4/G5：文本设计不等于资产或画面通过，实际图片和视频仍须按对应 Gate 审核。

## V1.9 execution and Method overlay

### Manual and automatic generation handoff

项目启动时在 Project Brief 的 Production Frame 中确定三个独立选择：资产图片、分镜/关键帧图片、镜头视频。用户可分别选择手动或自动；尚未决定的项目标 `OPEN`，到对应批次执行前再确定。`AUTO_GENERATE` 只表示按项目授权和当前工具能力代为执行，不自动授予外部上传、付费或发布权限。`USER_GENERATE` 表示交付可复制执行包，等待用户生成并回传真实媒体；用户未给出审核结论时进入 Codex 审核，用户明确批准时直接按批准范围入库。项目默认方式持续适用；用户可针对单个批次明确改选，记录覆盖范围和版本，不反复要求选择。

手动执行包按生产顺序拆成可单独复制到无限画布的卡片：`资产图 → 分镜/关键帧图 → 镜头视频`。每张卡以稳定 Asset/Frame/Shot/Unit ID 开头，依次给出目标文件名、先决依赖、参考图上传顺序与用途、`直接复制｜主提示词`、适用时的 `直接复制｜负向提示词`、平台参数、`不要复制｜验收与回传`。提示词正文保持独立连续文本；路径、说明和验收项放在正文外。依赖上一步实际结果的卡片先标 `WAITING_DEPENDENCY`，不得伪装成可立即执行。自动执行也使用同一批准内容，只由执行者提交并记录结果。

每份手动交接包必须在提示词前给出当前批次的编号执行顺序，并在每张卡写明可操作步骤：`确认 READY 与前置批准 → 选择目标平台/任务入口 → 按编号上传对应版本的参考图 → 设置平台支持的参数 → 仅复制主提示词及独立负向栏（适用时）→ 生成并保存原文件 → 按卡片 ID 回传；用户可同时说“审核通过”，否则进入 Codex 审核 → 按批准范围解锁依赖项`。每步写清实际文件、槽位或待确认项；平台未选或能力未核实时标明 `MODEL VERIFICATION REQUIRED`，不编造按钮、`@` 语法或参数。批次清单标出哪些卡可并行、哪些必须等待指定结果通过，以及失败时从哪张卡局部返工。

分镜图片或镜头视频的手动交接按场景成组交付：场景方位/人物走位图（Stage 09，空间敏感时）→ 同一底图上的机位/关系轴叠加图（Stage 10）→ 按镜号排列的 Frame/Unit 卡片与提示词。图可用清晰的文字示意或实际图文件，但必须带 Scene/Card/Shot ID、版本、地标、人物路径、机位朝向及未知空间边界；普通单点场景若上游记为 `NOT_NEEDED`，直接说明原因，不为凑图制造方位卡。交接视图从批准的 Scene/Shot 合同汇总，不在下游重新设计站位和机位；同一场景的图在本组只放一次，让用户在无限画布上紧邻对应镜头使用。

用户回传图片或视频后，按卡片 ID 登记真实路径、版本、模型/参数（已知时）和实际结果；未附人工审核结论时进入相应 QC。文件存在本身不等于通过；未回传时停在对应交接节点，不将计划稿标为已生成或已批准。

用户对可识别的文件、卡片或批次明确说“审核通过 / 就用这版”时，以该人工决定作为相应范围的验收：确认文件真实存在且 ID/版本对应后直接归入阶段目录、更新 manifest/合同与 `USER-APPROVED` 来源，冻结该版本并推进其依赖；不再要求 Codex 重做画面或视频 QC，也不把人工批准写成 `QC_PASS`。只记录批准对象、范围、时间和来源；未明确覆盖的其他镜头、整段顺序或成片仍按各自关口处理。用户修改或撤回批准时只重检受影响依赖。

V1.9 不新增阶段，把现有合同组织成三层，并在其上增加经项目采用的 Method 覆盖：

| Layer | Purpose | Editing rule |
|---|---|---|
| `CREATIVE / VISUAL SOURCE` | 剧本、Visual Bible、资产、Shot、Frame、Motion 等批准事实 | 在对应责任阶段维护 |
| `COMPILED EXECUTION VIEW` | 逐镜执行卡、整合提示词手册、上传与生成顺序 | 从确切源版本重新编译，不在此发明或静默改写事实 |
| `OBSERVED EVIDENCE` | 实际 Take、参数、QC、Actual Observation 与失败证据 | 只记录真实执行和审核结果，不倒改计划状态 |

每个可生成 Unit 应提供一张 `Production Unit Card`。它不是新合同或新阶段，而是把同一镜头已批准的信息按执行顺序汇总：镜头任务、注意力层级、前镜残留、触发—延迟—可见变化—交接、资产/状态版本、`@` 绑定、可复制主/负向 Prompt、不可复制验收项、风险假设、当前状态与实际 Take/QC 链接。底层合同继续分阶段保存；执行人员不应为了生成一个镜头在多份文件之间人工拼接。

### Revision intake and freshness

收到新稿、用户修改或批准资产替换时：

1. 保存新输入版本，不静默覆盖当前 `LOCKED` 版本；
2. 记录变更字段、替代关系和用户是否已批准晋升为新主版本；
3. 从最早变化的源合同列出 `Affected Dependents`；
4. 给下游条目设置 freshness：
   - `CURRENT`：与当前批准源版本一致；
   - `STALE`：源事实已变化，继续使用会错误；
   - `BLOCKED`：缺少批准、资产、能力或依赖证据；
   - `RECOMPILE`：创作事实未失效，只需从新版本重新输出执行视图；
5. 只重新审核受影响字段和依赖；不受影响的已批准工作保持冻结。

`STALE / BLOCKED` 的 Unit 不得进入生成。整合手册中直接改字只能作为待回写差异；必须先更新正确的源合同，再重新编译，避免执行视图与主版本分叉。

### Consolidated approval points

阶段内可以持续整理和编译，但用户确认尽量集中在高成本选择：创作主版本、视觉/资产基准、分镜序列与 Animatic、技术样片方向、最终 Take/Picture Lock。格式整理、状态传播和从已批准合同重新编译不额外制造审批节点。

## Cross-stage approval gates

17 个 Skill 是责任分工，不代表每次都可以无条件向后推进。项目至少经过以下 Gate：

Stage 01 在 Project Brief 的 Production Frame 中明确本次交付产物与终止阶段，并在 Decision Register 记录 `G0 Review` 的依据、阻断项和可延期开放项。具体按 [项目定义决策指南](../skills/film-project-director/references/decision-guide.md) 的入口与 G0 审阅执行；READY 只表示定义可交接，不代表用户批准全部假设或下游生产就绪。已有项目只复核变更及受影响范围。

| Gate | Evidence required | Pass condition | Failure route |
|---|---|---|---|
| G0 Scope Lock | Project Brief | 形式、范围、意图、Emotional Thesis / Core Image Seed、Method Adoption（适用时）与 Research Gate 清楚；开放项明确而非假装锁定 | Project Direction / Method Fit Return |
| G1 Research Ready | Research Pack + Source Index + Research Question Map / G1 Readiness | 当前范围关键问题有充分依据或处于明确允许的虚构范围；事实、作品观察与艺术提议分开；阻断与延期问题、责任阶段清楚。已定方向不重选，纯艺术表达不以史实门槛筛除；PARTIAL 不等于全项目通过 | Research Return / 影响合同的 Project Direction Return |
| G2 Creative Master | Story + Character + Treatment + Screenplay | 原始故事合同与各创作主版本完整一致；叙事作品的行动、因果、选择与后果可理解，诗性/观察作品的关联原则、情绪递进与结尾回应可感知；人物行为与关系回应有依据，变化或稳定服务故事，事实层与授权重构分开；详纲正文经顺读修正且与蓝图、人物系统和段落映射一致；必要时间线索、前文支撑及开放解释范围清楚，主要配角、规则与奇观有明确作用。Story Review、Character Review 与 Treatment Review 各自只覆盖本阶段，不代替剧本验收 | 最早失效的 Story / Character / Treatment / Screenplay |
| G3 Visual Asset Ready | Visual Bible + Reference Translation（适用时）+ Narrative Look Arc + Scene Look & Light / Atmospheric Medium States + 当前镜头所需的 APPROVED P0 assets | 当前镜头的参考语义、人物身份、服装、场景拓扑、空间证据边界、灯光/材质/空气状态、道具和关键状态稳定；时期变化有叙事触发，空气介质有物理原因或明确为 NONE | Visual / Asset Revision |
| G4 Static Storyboard Ready | Shot List + reviewed Composition Guides（或逐镜 `NOT_NEEDED`）+ reviewed Frames + 适用 Sequence Review / 实际 Animatic + Rhythm Map | 复杂/关键 Frame 的构图获准；画面正确性、主要注意与表达符合观看立场和艺术规则，完整含义结合所需声音审核；确切用途版本、视觉状态、静态状态对与依赖连续性通过。多镜有顺序画面及实际预览播放/明确人工批准证据，计划不代替；静态审核不证明运动或模型可行 | Scene / Shot / Composition Guide / Storyboard Revision |
| G5 Technical Pilot Validated | Prompt Coverage Receipt + Production Unit Card + Model Compatibility + Method Adoption/Pilot Receipt（适用时）+ 高风险代表镜头的真实 Takes + QC + Model Routing Result | 源版本为 CURRENT；十三项已明确映射、降级或退回；风险假设、单次 Changed Variable、Method-specific QC、真实样片结论和适用边界明确 | Method / Asset / Shot / Motion / Prompt / Generation Revision |
| G6 Sequence Ready | QC-selected 或 USER-APPROVED Takes + 跨镜审核或明确的整段人工批准 | 单镜可用且按顺序播放成立；或用户明确批准该整段范围，未做 QC 的维度保持 NOT_EVALUATED | 最早责任层返工 |
| G7 Picture Lock | 确切最终渲染版本/checksum、Post Review 与两项全片声画审核证据 | 故事/注意/艺术表达、声音、文字、权利和技术门通过；状态 PICTURE_LOCKED，旧候选证据不套新文件 | Post / Upstream Return |
| G8 Delivery Verified | 本次 Required 交付文件、逐文件验证与归档/恢复范围记录 | 规格、表达保护、适用完整播放与校验通过；所有 Required 和约定归档要求满足才整包合格，恢复能力按实际证据声明 | Delivery / Post Return |

G2 的剧本部分还须有完整正文、场间承接、对白或沉默的关系作用、艺术内容可读性与结尾支撑的审阅证据；Screenplay Review 只覆盖文本。时长检查注明范围、方法与估算限制，明确目标存在未解决冲突时不得正式交接视觉阶段；文字估时不替代后续 Animatic 的播放验证。

Stage 08 的视图/状态按剧本动作、预计观看范围与风险确定，不默认六视图，也不要求先完成 Shot List。G3 检查当前所需 P0 用途是否落在确切文件/版本的 Approval Scope 内，不能从单图或资产级 APPROVED 外推全部视图、互动与状态；新增用途只补受影响扩展版本，保留已有批准。艺术资产继承 Stage 07 呈现规则，物理与非物理层分开；仅内容交付可继续标明依赖待验证的草稿，不冒称生产通过。

Stage 07 的视觉命题、关系语法、变化触发与核心规则的资产/验收映射须完成文本审阅，才为 READY FOR ASSET DESIGN；它不等于 G3 或实际画面已通过。PHYSICAL / STYLIZED / MIXED 明确呈现范围，非物理艺术效果独立记 CREATIVE 规则、作用和状态触发，不冒充 Atmospheric Medium State 的真实空气；真实空气仍须物理来源或 NONE。下游继承批准艺术规则的允许变化，不以缺物理原因一概否定非写实表达，也不借艺术模式改写身份、事实承诺或剧本。

G3 按已锁定镜头的实际可见需求验收：先确定镜头表和每镜使用的资产版本，再检查这些镜头所需的身份、服装、空间方向、道具接触及跨镜状态。未入镜的视角、细节板和全部预设状态可留在资产清单中，不阻断场景、分镜或提示词编写；新增镜头引用它们时再补齐并复核。草稿可以先行，执行用提示词只能引用已审核的实际资产版本；关键身份、阵营、空间方向或史实证据有冲突的镜头不得放行。G3 记录应明确已覆盖的镜头范围，不把局部通过写成全片通过。

G5 不是要求每个低风险项目额外制作测试片。只有 Shot List 标出高风险，或首次使用新的模型、角色方案、复杂动作、多人交互、特效、口型/对白方案时才强制。样片通过只验证对应生产假设，不等于全片已经通过。

用户明确接受记录在案的真实技术样片风险并要求继续时，可按风险与适用范围登记 USER_ACCEPTED_RISK 并进入相应批次；仅批准单个样片不自动接受全部未验证风险。它不等于 PILOT_VALIDATED 或 Codex 已完成技术 QC，未提供的可见状态不填为 Actual Observation。

## Optional creative-reference lane

用户提供电影、AIGC 短片、小说、游戏或案例拆解时，参考资料在 G1 前后进入研究包，但不新增一个强制阶段：

```text
实际看到或读到的内容
→ 对其作用的解释
→ 可迁移的叙事/视觉/制作机制
→ 本项目的验证假设
→ 明确不可复制的独特表达
```

参考作品不能充当历史、现实或科学证据，也不能直接变成复刻指令。未经本项目小样验证的方法保持 `REFERENCE HYPOTHESIS`，不能标成已证实的生产规则。

当用户明确希望把参考沉淀为跨项目能力时，进入 Method Learning Lane：

```text
参考媒体与 USER_VALUED 结果
→ 完整 Study：OBSERVED / INFERRED / WORK_SPECIFIC / TEST_REQUIRED
→ 与现有 Method 比较：更新 / 模块 / 组合 / 新建
→ CANDIDATE Method Pack
→ 项目 Method Adoption Receipt
→ 最小真实 Pilot + 通用 QC + Method-specific QC
→ VALIDATED_FOR_SCOPE
→ film-method-<slug> 专项 Skill
→ 新项目证据回流、复核或退役
```

Study 与候选 Method 不自动进入项目；项目必须显式采用。一个项目可以组合多个 Method，但每个受控字段必须只有明确 Owner；冲突无法字段级裁决时返回用户决定。

视觉参考进入生产前必须登记来源、版本/路径、权利状态、允许影响与禁止覆盖项，并分类为：

- `HARD_ANCHOR`：来自已批准项目合同、必须保持的事实；外部风格图本身不能建立硬锚点。
- `SOFT_REFERENCE`：只迁移质感、色彩关系、材料、空间或节奏等方法。
- `EXCLUSION`：水印、错误人物、文字、品牌、时代错误及其他不得进入结果的元素。

## Optional source-adaptation lane

当项目来自小说、故事、剧本、纪实材料或较长原作时，在 Stage 01 前运行 Stage 00：

```text
原文件与版本登记
→ 顺序覆盖与未读范围
→ 人物 / 事件 / 地点 / 物件 / 规则提取
→ 原作事实、角色认知与分析解释分层
→ 改编不变量 / 可选项 / 未决项
→ Project Direction
```

短想法和短文本不强制经过 Stage 00。Source Intake 证明“原作写了什么”，Research Pack 证明“外部世界有什么依据”，两者不得互相替代。

## Where images and prompts belong

### Character turnarounds and scene images

人物身份锚点、头部角度、全身六视图、表情状态、独立服装/妆发、组合定妆、场景/环境、材质细节和道具参考图属于 Stage 08 `film-asset-designer`。它们必须建立在已批准的 Character System、Screenplay 和 Visual Bible 上；在此之前可以做明确标注为 Exploration 的低成本视觉实验，但不能冒充锁定资产。

### Image and video prompts

- **概念资产提示词：** Stage 08 内部可生成模型无关的资产意图，并由资产执行器生成参考图。
- **镜头图片提示词：** Stage 13 根据已批准的 Shot List、Storyboard、Keyframes 和资产身份规则编译。
- **视频提示词：** Stage 13 根据镜头起止状态、动作、摄影机、环境运动、时长和连续性要求编译。
- **共享提示词库：** `skills/film-prompt-adapter/references/` 按资产、单帧、视频、材质/空气和返工分模块复用；十三项覆盖表负责查漏，模块模板负责表达，二者都不能替代上游批准合同。
- **空气质感辅助合同：** 显著或连续性敏感的空气介质先由 `film-atmosphere-designer` 定义来源、分布、驱动、受光、人物/材料响应和变化触发，再由提示词库压缩表达；不得从 Prompt 反向发明雾、烟或粒子状态。
- **生成学习案例：** Prompt Adapter 可以引用符合当前模型边界的公共 Pattern ID；Generation 只记录实际尝试和改变变量，QC 只提供真实证据，`film-generation-pattern-curator` 决定案例等级和是否提升。未经 QC 的结果不能进入公共模式。
- **模型路由：** Seedance、MiniMax/Hailuo、Kling、Veo 等平台差异只在 Prompt Adapter / Generation 阶段处理，不反向污染故事和剧本主版本；新模型或关键能力未经真实样片验证时不得直接承担整片量产。

## Core handoff contracts

### Creative master chain

```text
[Source Intake（仅原作驱动项目）]
→ Project Brief
→ Research Pack
→ Story Blueprint
→ Character System
→ Treatment
→ Screenplay Master
```

### Visual-directing chain

```text
Screenplay Master
→ World & Visual Bible
→ Approved Reference Assets
→ Scene Design Pack
→ Shot List
→ Storyboard / Keyframes
→ Motion Specification
```

贯穿这条链的状态最少包括：实体 ID、数量、所有者、世界位置、可见性、开合/损坏等物理状态、动作阶段、角色知情状态、`Narrative Look Arc ID`、`Scene Look & Light State ID`、`Atmospheric Medium State` 与 `Rhythm Role / Required Hold`。表演状态使用姿态/重心、视线、呼吸/声音、手与道具、服装/头发响应以及进入—变化—退出链表达。每次状态变化记录 `Pre-state → Event → Planned Post-state → Actual Observation`；没有真实画面时不得填写 Actual Observation。

### Generation chain

```text
Approved Creative + Visual Masters
→ Model-specific Prompt Packages
→ Technical Pilot Takes（高风险项目）
→ Pilot QC / 最早责任层返工
→ Production Takes + Generation Log
→ Sequence Continuity QC
→ Post-production
→ Delivery Masters
```

## Risk-first execution order

批准版本仍按 Stage Map 形成，但实际生成批次按风险而非镜号顺序执行：

1. 从 Shot List 选择能覆盖最高风险的最小样片集合；每个 Pilot 先写一个可证伪的 `Failure Hypothesis` 和主要 `Changed Variable`。同一测试镜头可以覆盖多个观察维度，但不要为了“完整”扩大范围。
2. 在同一组内容内先制作会改变物件所有权、人物位置、知识、身体或动作阶段的关键状态镜头；相依镜头等待该状态经画面审核确认。
3. 先完成这些镜头的静态帧、Motion Spec、Prompt、真实 Take 和 QC，再将实际观察结果传给依赖镜头。
4. 失败时返回最早责任层；每次尝试写明验证假设，并优先只改变一个独立变量。若同时改变多个变量，必须标明 Confound，不能声称得出单变量结论。已经批准的非受影响内容保持冻结。
5. 核心风险通过后才建立 Production Batch；普通镜头可以按场景、资产复用或剪辑依赖分组生产。
6. 单镜通过后仍需做跨镜顺序播放；声音与后期不能掩盖身份、空间、动作或因果错误。

## Universal return routes

下游发现问题时只返回最早失效的阶段：

- 事实、文化、科学、授权依据不足 → `Research Return`
- 核心因果、主题或结局失效 → `Story Blueprint Revision`
- 人物行动、能动性或关系边界失效 → `Character Revision`
- 完整过程失效 → `Treatment Revision`
- 场景、对白或可见行动失效 → `Screenplay Revision`
- 视觉规则或身份不稳定 → `Visual Bible / Asset Revision`
- 镜头无法表达场景目的 → `Scene / Shot Revision`
- 模型执行失败但上游清楚 → `Prompt / Generation Revision`

## Current implementation order

V1.9 保留 17 个核心阶段及一个可选 Source Intake 前置阶段，不扩展阶段数量。开放式 Method Overlay 与上述四项专项工序按触发条件接入；具体项目仍以批准的主合同、真实媒体审核和现有 Gate 为准。

下一步不再增加新阶段，进入真实项目纵向联调：选择一个短片，从 Project Brief 连续运行到交付；在实际图片、视频、声音和平台工具可用时补足像素审核、完整播放、费用/权限和导出验证。文本/计划测试通过不等于实际媒体质量已经验证。

后续继续采用：真实案例执行 → 记录失败 → 返回最早责任层 → 做最小规则修订 → 全链路回归。
