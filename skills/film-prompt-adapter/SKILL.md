---
name: film-prompt-adapter
description: 将已批准的资产、分镜、镜头和 Motion Spec 编译为特定图像或视频模型可直接执行的 Prompt Package，并提供人物、服装、场景、材质、关键帧、表演、镜头时间线和返工提示词的可复用写法。用于 AIGC 电影图片/视频提示词编写、审查及 Seedance、MiniMax/Hailuo、Kling、Veo 等模型适配；不用于重新创作故事、镜头或运动，不调用生成，也不声称模型执行成功。
---

# Film Prompt Adapter

把稳定的创作主合同翻译成目标模型当前可执行的语法与输入组合。Prompt 是编译产物，不是新的创作主版本。

## Required inputs

1. `motion-spec.md`，状态 `READY FOR PROMPT ADAPTATION`（视频）
2. Storyboard/Frame Manifest，状态 READY 或 USER-APPROVED
3. `shot-list.md` 与 continuity ledger
4. APPROVED 资产合同与准确文件路径
5. 目标模型/版本、任务类型和可核实的当前 Model Profile
6. 用户锁定的分辨率、画幅、时长、音频、预算或平台限制
7. `atmosphere-state-register.md`（项目存在独立空气状态合同时）
8. `direction/method-adoption.md` 与对应 `film-method-*`（项目采用 Method 且 Prompt 在 Affected Stages 时）
9. `storyboard/lighting/lighting-pass.md` 与 lighting continuity ledger（项目执行过分镜光影 Pass 时）

图片任务可以从批准的 Frame Contract + 资产合同进入；视频任务不能跳过 Motion Spec。

上述批准条件用于生产执行包。仅内容交付可依据 MOTION EXPLORATION 与已有上游合同编译“内容草稿｜待验证”，列出缺失参考、用途批准和模型能力；不要求先回传媒体。草稿不是 READY FOR GENERATION，不编造实际文件、平台参数或审核证据；不能提交生成，也不能将冲突或过期事实冒充批准内容。此入口只放宽文字交付，不替代下文生产审核门。

内容草稿使用 Package Status `CONTENT DRAFT`；单元卡 Execution Status 保持 NOT_READY，缺真实依赖另记 WAITING_DEPENDENCY。草稿可有完整可复制正文，但须在正文外注明待验证条件，不把占位别名当实际输入。只有完成当前范围批准、Profile、反向审核和依赖/Pilot 条件的单元才执行放行。

## Load resources

- 开始适配前读取 `references/prompt-compilation-guide.md`。
- 编写长篇电影视频提示词、检查完整性或用户要求“固定框架”时读取 `references/cinematic-video-prompt-framework.md`；十三项只作为工作台与回执，不能机械拼成十三段 Prompt。
- 按任务类型从 `references/prompt-library-router.md` 只加载需要的提示词模块；不要为了“完整”一次加载或拼接全部模板。
- 创建或验收包时读取 `references/prompt-package-contract.md`。
- 目标为 Seedance 时读取 `references/seedance-profile.md`；目标为 MiniMax-H3 或 Hailuo 时读取 `references/minimax-profile.md`。
- 若 `pipeline/knowledge/generation-pattern-catalog.md` 存在，只读取与当前模型版本、入口、输入模式和风险类型匹配的 ACTIVE Pattern；记录 Pattern ID 与证据状态。公共模式是候选写法，不能覆盖当前 Profile、Creative Master 或 Pilot 要求。
- 需要先整理信息再压缩 Prompt 时使用 `assets/prompt-authoring-workbench-template.md`；正式结构化交付使用 `assets/prompt-package-template.md` 与 `assets/prompt-manifest-template.md`。面向用户或生成执行者的逐镜整合视图使用 `assets/production-unit-card-template.md`，它只能从批准源合同编译。

## Model profile gate

模型能力会变化。每次实际适配都优先查阅目标平台官方文档或官方模型卡，并记录：

- Model / version / access date
- Provider / Platform / Task Entry / API or UI Route / Account-Region Scope；同名模型的不同入口分别核实
- Task type: T2I / I2I / T2V / I2V / reference-to-video 等
- Input modes and required conditioning: text / image / start-end / multi-reference / edit / extend / audio-driven
- Duration, aspect ratio, resolution, frame/reference limits
- Start/end frame、参考角色语义、角色/场景绑定、音频/对白/口型、可见文字、负向提示词与镜头控制支持情况
- Required prompt schema、参数位置、异步任务方式和结果形态
- 当前限制、地区/账户差异和不确定项

无法从可靠当前来源确认时标 `UNVERIFIED`，不得猜测参数。用户提供的 profile 可以使用，但标记来源。

## Outputs

```text
AIGC Creater/projects/<project-id>/prompts/<target-model>/
├── prompt-manifest.md
├── prompt-package.md
└── production-unit-cards.md      # 逐镜整合执行视图；需要时输出
```

## Workflow

1. **Verify creative masters and freshness.** 生产包所有输入须批准且版本匹配；核对 Source Version 与 CURRENT / STALE / BLOCKED / RECOMPILE。STALE/BLOCKED 返回正确上游，RECOMPILE 从新源重建，不在旧 Prompt 上补丁。内容草稿可按上述入口交付，保留依赖和阻断状态，不提升为执行就绪；事实冲突不得静默编入。缺失生产依赖返回 Storyboard/Motion/Asset。
2. **Resolve target profile.** 优先使用用户指定模型；未指定时依据输入模式、连续性需求和已核实能力给出一个首选路由，不把价格或能力当作永恒事实。
   - 可参考由 `film-generation-pattern-curator` 提升的匹配 Pattern，但模型版本/入口不一致、状态为 Review/Retired 或适用范围不符时不得采用。
3. **Map inputs, upload order and prompt bindings.** 为每个 Prompt Unit 精确登记 Shot/Clip/Frame、资产文件、首尾帧、音频和参数来源；每个参考文件标 `IDENTITY / WARDROBE / POSE / TOPOLOGY / STYLE / STATE / START FRAME / MID FRAME / END FRAME / MOTION / AUDIO`，并写清上传顺序、平台槽位、Prompt 绑定句、批准范围、允许影响与不可覆盖字段。STYLE 参考不能覆盖当前状态，旧生成帧不能替代原始身份/风格锚点。
4. **Preserve intent before compression.** 将主体、Viewing Stance / Information Alignment、Must Read/Withhold、构图关系、MAIN/SUPPORT/HOLD、必要停顿、状态与结束点列为 Intent Preservation Map，映射到实际输入、Prompt、外部控制或明确待验证/不支持项。不是每项都重写进正文，图像已承载的内容可由图像承担；压缩不得丢失创作核心。无法执行的字段列 incompatibility，不靠加强语气假装保证。
   - 存在批准 Lighting Pass 时，同时锁定世界光源、画面投影、人物/环境共同受光、曝光/色彩关系与允许变化触发；不得把它压缩成“电影光影”或另加无来源轮廓光、光束和雾。
5. **Calibrate meaning, classify creative authority, then compile compactly from the current instant.** 先确认上游描述的类别是否足够具体，例如不是泛泛的“旧屋夜景”，而是某个地点、节日/事件、人物关系和正在发生的生活状态；具体性不足时返回上游，不靠追加材质词掩盖。再把字段标为 `LOCKED / DERIVED / CREATIVE / PROPOSAL`：保留锁定事实，注明推导依据，主动使用上游已批准的 Creative Choice；用户明确要求提示词创意探索时，可以另给大胆但连贯的 `CREATIVE VARIANT`，但凡会改变已批准镜头、动机、空间、主动作或结局，都必须作为 Proposal 返回责任上游，不能悄悄混入生产 Prompt。内部工作底稿可以完整，交付模型的 Prompt 再按目标语法压缩。视频 Prompt 描述输入帧之后发生什么；MID/END 帧不得重新播放已完成动作。继承 Narrative Look Arc、Scene Look & Light State、Atmospheric Medium State 与 Rhythm Role/Required Hold，并把姿态/重心、视线、呼吸/声音、手部和必要的服装/头发响应编译成有动机的表演链。空气介质只编译有来源和驱动力的可见响应；不得删除为反应或静默保留的关键停顿。删除重复和互相冲突的形容词；平台不支持的字段不能伪装成自然语言保证。
   - 资产图片使用 `asset-prompt-patterns.md`；身份、服装、妆发、场景、道具和组合定妆分别编译，不能用一张合体图取代源资产。
   - 分镜/关键帧图片使用 `shot-image-prompt-patterns.md`；每条只描述一个可见时刻，不加入动作过程。
   - 视频使用 `video-prompt-patterns.md`；把抽象情绪转译为触发后可观察的表演与动作链。
   - 需要材质和空间厚度时使用 `material-atmosphere-patterns.md`；存在 Atmosphere State Register 时只编译对应 State ID，空气介质必须保留物理来源、空间分布和运动驱动，不默认添加雾和颗粒。
6. **Add constraints.** 只在平台支持时使用 negative prompt / exclusions；始终保留身份、轴线、道具、文字和额外主体等关键禁止项。
   - 返工时读取 `repair-and-exclusion-patterns.md`，优先使用 `Change / Preserve / Constraints` 只修失败字段，不把全部正向词重复加重。
7. **Apply adopted Method modules.** 只编译 Adoption Receipt 授权的 Method 字段、专项排除和 Pilot 假设；Method 不能覆盖 Creative Master、Model Profile 或项目保护字段。多个 Method 的同字段冲突未裁决时标 `CONFLICT`。
8. **Plan fallbacks with expression cost.** 按实际能力比较输入模式、批准参考、拆 Clip、次级运动简化或模型路由，记录 Unsupported Field / Alternative / Expression Cost / Source Permission / Pending Validation。只执行上游已授权且不改变意义的降级；改变镜头、表演、艺术规则或结束状态的方案返回责任上游，影响方向且未获授权时才集中交用户决定，不把最省事方案当默认。
9. **Complete the coverage receipt.** 对十三项内容逐一记录 `MAPPED / NOT_APPLICABLE / UNSUPPORTED / CONFLICT / RETURN`、来源合同与目标落点。回执不拼入 Prompt；Conflict/Return 未解决时不得执行，Unsupported 必须给出降级去向。
10. **Review the whole compiled input.** 从 Prompt + 实际参考及角色/顺序 + 已核实输入槽/控制项反查意图，不能只读文本而误判图像承载内容缺失。Prompt Review（PASS / REVISE / NOT_EVALUATED）记录范围、证据、语义保留、绑定对应、角色/时长、艺术规则、支持边界、阻断项与待 Pilot 验证；草稿只审核可检查部分，缺失输入不填实测通过。
11. **Separate prompt from controls.** 模型名、版本、时长、画幅、分辨率、seed、参考权重和API字段默认进入参数清单，不塞入Prompt正文；只有目标模型已核实的Prompt schema明确要求时才写入正文。
12. **Preserve production order and dependencies.** 从 Shot List 继承 `Risk Level / Risk Hypothesis / Pilot Priority / Depends On / State Changes`，先编译最小 Pilot 和关键状态 Unit；依赖 Unit 只有在上游实际状态经审核确认后才能标为可执行。不得因适配方便擅自改写风险判断。
13. **Route by scope and evidence.** 当前所需源版本 CURRENT、具体用途获准、必需文件/依赖就绪、Profile VERIFIED、Prompt Review PASS、回执无未解决 Conflict/Return 且 Unsupported 有合规去向，才将对应 Unit 标生成就绪；Pilot 仍按批次关口执行。草稿 CONTENT DRAFT 可完成文字交付，列待验证项；不从包整体状态外推所有 Unit 就绪，不把文本审核称为模型效果通过。
14. **Compile the production unit card.** 对实际交付的每个 Unit 汇总镜头任务、`MAIN / SUPPORT / HOLD`、反应交接链、源版本、资产/状态、参考绑定、直接复制 Prompt、不可复制验收和风险假设。卡片不得新增源合同中不存在的创作事实；若需要新动作、反应或状态，返回上游后再编译。
   - 沿用 Project Brief 的镜头视频默认执行方式；`USER_GENERATE` 时按依赖顺序输出可直接放入无限画布的逐镜卡片。每张卡独立包含 Unit/Shot ID、目标文件名、参考图上传顺序与用途、平台参数、独立的主/负向提示词正文、验收和回传要求；操作说明、路径和 QC 项不混入可复制 Prompt。`OPEN` 到生成执行前再确定，单批改选记录在执行卡中。

## Prompt unit requirements

编译时区分 Input Frame Role（START/MID/END/REFERENCE）与 Input Use（CURRENT START / TARGET END / REFERENCE ONLY）。MID/END 作当前起点时从可见阶段后继续；END 作目标时约束结束，不当开场重播。图片只编译代表瞬间，视频编译变化或持续/HOLD；不强制新触发、微动作或转折。继承 Presentation Mode / Artistic Rule IDs 与版本，真实空气按物理依据，非物理层按批准作用/变化/保持项，不强制写实。未核实的中间帧控制不得伪装成有效输入。

- Unit ID / Task Type / Target Model & Version
- Creative Authority Map：LOCKED / DERIVED / CREATIVE / PROPOSAL；Creative Intent / Audience Effect / Continuity Cost / Generation Risk
- Intent Preservation Map / Viewing Stance / Must Read-Withhold / Composition Relations
- Applied Pattern IDs / Evidence Status / Applicability Check（如有）
- Source IDs and versions
- Source freshness: CURRENT / STALE / BLOCKED / RECOMPILE
- Input files and roles
- Input mode / reference-role map
- Reference upload order / platform slots / prompt binding text
- Copy-ready prompt
- Negative prompt / exclusions（如支持）
- Risk level / hypothesis / pilot priority
- Parameters
- Input Frame Role / Planned Duration / Generation Duration
- Input Use / Presentation Mode / Artistic Rule IDs & Versions / Layer / Change or HOLD
- Expected current state / continuation / end
- MAIN / SUPPORT / HOLD and Previous Residue / Trigger / Delay / Visible Change / Handoff
- Narrative Look Arc / Scene Look-Light / Atmospheric Medium / Rhythm Role inheritance
- Continuity anchors
- Unsupported / degraded fields
- Thirteen-item Prompt Coverage Receipt and source/target mapping
- Fallback plan
- Verification checklist
- Prompt Review / Evidence / Blocking Issues / Pending Pilot Validation

## Non-negotiable boundaries

- 不调用生成工具，不产生 Take，不声称 Prompt 有效或视频成功。
- 不修改 Screenplay、Shot、Storyboard、资产身份或 Motion Master 来迎合模型。
- 不把未经核实的模型能力、时长、分辨率、费用或参数写成事实。
- 不堆砌“cinematic、masterpiece、8K”等无功能词替代具体视觉与运动信息。
- 不把整个 Visual Bible 和 Motion Spec 原样复制进每条 Prompt。
- 生产输入不使用未登记路径、不存在文件或未批准用途；草稿可明确待补，不能伪装成已上传或可执行。
- 不把平台负向词支持、音频能力或起止帧能力想当然。
- 不把教程示例、影片名称、镜头构图或某个模型的营销描述固化为跨项目模板。
- 不把“忠于来源”误解为只能写最安全的普通覆盖；已获授权的创作字段应做出明确选择，但大胆不等于无动机运镜、参数堆砌或擅改锁定事实。
- 不把灰尘、雾、蒸汽、胶片颗粒和浅景深当作统一的“去 AI 感”配方；每项必须服务地点、材料或叙事。
- 不把只检查过文本的 Prompt 称为运动已验证，不让上一张生成图成为唯一风格锚点。

## Completion gate

下列为生产放行条件；CONTENT DRAFT 的完成标准是文字与来源映射可审、待补/冲突/能力不确定项明确，不要求先获得媒体，不借草稿绕过生产门。

- 每个需要生成的 Frame/Clip 都有唯一 Prompt Unit；
- Model Profile 的来源、版本和访问日期明确；
- 输入文件真实存在且版本批准；
- Prompt 保留主合同的 start/trigger/action/end、摄影机和连续性；
- Prompt 保留必要反应/停顿，并且空气介质的来源、分布与驱动没有被改写成通用粒子效果；
- 参数符合已核实 profile；
- 不兼容与降级项显式且不改变创作核心；
- 每个 Unit 的十三项覆盖回执完整，Conflict/Return 已解决；
- Reverse-check 通过；
- Prompt Review PASS，意图映射、输入角色/用途、艺术规则和平台入口范围对应；实际模型效果仍待生成/Pilot；
- 没有生成成功声明。
