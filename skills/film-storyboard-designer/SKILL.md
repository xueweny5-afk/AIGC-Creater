---
name: film-storyboard-designer
description: 将状态为 READY FOR STORYBOARD 的剧本映射、Shot List、连续性账本和已批准资产转化为剧本—镜头—画面覆盖表、可审核分镜板、Hero Frame 候选与必要的起止关键帧，并维护逐帧状态与审核清单。用于剧本拆分镜、覆盖检查、静态画面预演、构图验证和关键状态锁定；不用于重新设计镜头、编写最终模型视频提示词或生成视频。
---

# Film Storyboard Designer

把镜头设计变成可见、可排序、可审核的静态画面状态。分镜证明构图、动作节点和连续性，不代替运动设计或最终视频生成。

## Required inputs

1. `shot-list.md`，状态 `READY FOR STORYBOARD`
2. `shot-continuity-ledger.md`
3. `asset-manifest.md` 与所需 APPROVED 资产
4. `world-visual-bible.md`、Scene Design Pack 与 Screenplay
5. 目标画幅和用户锁定的视觉决定

## Modes

- `PLAN_ONLY`: 输出 Board/Frame 计划和模型无关 Frame Brief，不调用图像工具。
- `HANDOFF`: 输出按 Scene/Shot/Frame ID 编号、带依赖顺序与目标文件名的分镜生图提示词包，由用户在外部网页或统一模型会话中生成；收到图片后转入 `REVIEW`。
- `GENERATE`: 用户要求实际生成时，使用可用图像工具创建最小必要帧并逐张审核。
- `REVIEW`: 审核已有分镜、Hero Frame 或关键帧并更新状态。

未要求实际图片时默认 PLAN_ONLY。没有真实图片不能声称分镜图已完成或批准。

继承上游版本、本次范围和交付边界。仅内容交付可完成 Frame Brief、提示词与顺序/Animatic 计划，媒体依赖写待补参考或 WAITING_DEPENDENCY；不要求先回传图片才能交付文本。生产级生成和放行仍须所需资产具体用途、构图及画面审核证据，不把内容包当成已通过的执行包。

## Load resources

- 开始工作前读取 `references/storyboard-design-guide.md`。
- 创建或审核时读取 `references/storyboard-contract.md`。
- 在 `HANDOFF / GENERATE` 模式编写分镜、Hero Frame 或 Keyframe 图片提示词时，读取 `../film-prompt-adapter/references/shot-image-prompt-patterns.md`；涉及材质/空气时按需读 `../film-prompt-adapter/references/material-atmosphere-patterns.md`，返工时读 `../film-prompt-adapter/references/repair-and-exclusion-patterns.md`。共享库只帮助表达单帧合同，不允许本阶段越界编写视频运动 Prompt。
- 使用 `assets/storyboard-plan-template.md`、`assets/storyboard-sheet-template.md`、`assets/frame-contract-template.md`、`assets/sequence-review-template.md` 与 `assets/animatic-plan-template.md`。
- 构图/状态已批准后需要逐镜补全、改写或审核光影时，使用 `film-storyboard-lighting-designer`；它只能投影已批准 Look/Light State，灯光编辑产生新的 Frame 版本并返回本 Skill 复审。

## Outputs

```text
AIGC Creater/projects/<project-id>/storyboard/
├── storyboard-plan.md
├── storyboard-sheet.md           # 剧本—镜头—画面的可读总表；需要时输出
├── composition-guides/
│   └── <composition-guide-id>/   # 构图参考图、合同与版本；不是正式 Frame 或资产
├── frame-manifest.md
├── sequence-review.md
├── animatic/animatic-plan.md
├── animatic/preview.<ext>        # 实际创建时
├── frames/<frame-id>/frame-contract.md
└── generation-log.md              # 仅实际生成时
```

## Workflow

1. **Verify shot readiness and compile coverage.** Shot、资产、轴线和时长必须可追溯；缺失返回 Shot/Asset。先按剧本 Scene/Beat/Action/Dialogue/Sound Cue 顺序建立只读的 `Script → Shot → Frame Coverage`，继承每镜的景别/角度、构图关系、人物/道具动作阶段、镜头运动、声音与切点，并登记将由哪些 Frame 证明。表格只能暴露遗漏和冲突，不能在本阶段改写上游 Shot。
2. **Choose frame purpose, density and dependency order.** 为每镜选择最少画面：普通 Board、Hero Frame、Start Keyframe、End Keyframe 或必要的中间状态。按不可逆状态变化、复杂接触、空间重构和审批价值决定密度，不按固定宫格或“每镜两张”机械生成。先计划 `STATE-CHANGE CRITICAL` 帧，再安排依赖帧。
3. **Select the instant for its audience read.** 继承 Shot 的 Viewing Stance、Must Read/Withhold 和构图关系；说明前一状态、当前快照、后续承接及此刻为何最能表达镜头功能。可选察觉前、回应中、动作后果、等待或余韵，不强制动作高潮、压力或微表情变化。只锁一个时刻；Creative Delta 限于批准镜头事实内，不能借选瞬间改机位、构图目的或行动结果。
   - **Composition Guide gate:** 对多人、全身人物、复杂载具、显著遮挡、深度层次、特殊负空间或关键 Hero/Start/End Frame，先创建 `Composition Guide`；可复用无冲突旧分镜、已批准纯场景加灰盒主体，或新生成低细节构图图。它只锁 `camera / framing / subject scale / screen position / FG-MG-BG / negative space / occlusion / screen direction`，必须列 `Allowed Influence / Must Not Transfer`，不得锁脸、服装、美术细节、光色或道具版本。简单物件编辑可标 `NOT_NEEDED`。未获 `COMPOSITION_APPROVED` 或 `NOT_NEEDED` 的正式 Frame 不得生成。
4. **Project continuity and artistic rules.** 继承身份、服装、空间证据、坐标、轴线、视线、实体数量/所有权/可见性/动作阶段/知情状态、Look/Light、时间和画幅；无批准触发不改状态。继承 Presentation Mode / Artistic Rule IDs 及确切版本；真实空气遵循物理状态，非物理艺术层按批准的作用、触发和保持项表现，不强制写实或立体空间，也不容许随机身份漂移。首尾/中间帧记录同镜 State Pair Check，核对朝向、持物、接触、动作阶段与摄影机状态；静态状态可衔接不等于运动已验证。
5. **Write frame briefs, reference maps and the readable sheet.** 将主体占比/位置、人物间距、深度层或平面关系、留白、遮挡、视觉重心与 Must Read/Withhold 写成可检查要求；先让主要注意对象和必要关系可读，再增加材质细节，不强制三层空间。Dramatic Read 可表现关系、感知、保持或意象，表演仅记本帧真正可见的快照，不用静态图证明呼吸时序或完整倾听过程。Reference Map 分清身份、服装、空间、构图、状态与艺术规则的职责及禁迁移；计划阶段允许明确缺口，实际可执行卡才绑定已批准的真实路径。不写视频 Prompt；可读总表从 Shot 和 Frame 合同汇总，不另创事实源。
6. **Confirm generation mode.** 每个新批次先展示完整提示词，沿用 Project Brief 的分镜图片默认执行方式；只有该字段为 `OPEN`，或用户明确要求本批改选时才询问 `AUTO_GENERATE` / `USER_GENERATE`。记录单批覆盖；未确定方式或没有实际生成授权前不调用图像工具。
7. **Generate or receive independently.** 每个 Frame 生成独立源图，宫格仅作派生预览。先生成并审核关键状态帧；把画面中实际出现的状态记录为 `Actual Observation`，再编译依赖帧。`AUTO_GENERATE` 使用可用图像工具创建最小必要帧；`USER_GENERATE` 等待用户回传。
8. **Preserve approved calibrations.** 已批准帧默认冻结，不因相邻失败而重做；若它只批准为风格参考但状态已过期，只能提供 STYLE，不得覆盖当前人物、道具或动作状态。参考链定期回锚原始风格/身份资产，不能只沿上一张生成图传递。
9. **Inspect correctness and expression.** 对未获用户明确批准的图实际查看像素，分别记录 Frame Review 的 Correctness / Expression & Artistic Rule（PASS / REVISE / NOT_EVALUATED）：身份、空间、接触与数量是否正确；注意对象、构图、情绪/关系/意象是否可读且符合批准规则。艺术选择不自动算物理错误，装饰细节也不能掩盖叙事失败。用户批准按确切文件/版本/用途与范围登记 USER-APPROVED，不重复审核，不把未评估维度伪填 PASS。图片存在不等于通过。
10. **Sequence and coverage review.** 按顺序查看独立帧/派生预览，核对注意力承接、状态、反应/保持、冗余、缺口及批准的非连续转换。有方位卡时先不读解释检验可见空间关系，再核对同一 Card 的机位叠加；非写实空间按批准规则检验。先看纯视觉可读性，再按需要加入对白/声音检查完整含义；不要求静态图独自解释离画声音、全部心理或完整运动。回查剧本—Shot—Frame 覆盖及 Rhythm Role，不把无压力变化的安静积累误判为无效。Sequence Review 记录范围、结果、证据及责任层，单帧批准不外推整段。
   - 可生成多格 Contact Sheet 供整体审阅，但它只是派生预览；单帧合同和原始图片仍是生产主版本，宫格中的小图不能替代逐帧审核。
11. **Build the animatic and rhythm check.** 多镜场景按计划时长排列已审核帧，加入临时对白、必要环境声/静默和声音 Bridge；建立 Rhythm Map，逐段记录故事压力、行动/信息密度、视觉能量、声音能量、必须停留的反应/静默及变化触发。Animatic 只验证镜头顺序、时长、反应空间和声画节奏，不冒充 Motion Design 或最终剪辑；无法实际创建预览时保留 `animatic-plan.md` 并标 `NOT_RENDERED`。
12. **Check format variants.** 在主画幅上确认构图，并按 Shot List 的交付变体检查主体/文字安全区、允许裁切和必须重新构图的 Frame；不以最终交付阶段的强裁切代替设计。
13. **Set status and route.** 生产放行须当前所需独立帧在对应批准范围内、Sequence Review 通过（多镜时），并通过适用 Animatic Gate。Animatic 计划审阅与实际预览审核分开：多镜段落须有实际预览完整播放审核或用户对确切预览明确批准；NOT_RENDERED 不算通过。单镜无需多镜顺序/Animatic 验证时写 NOT_APPLICABLE 及理由，不强建空预览。PLAN_ONLY 或仅内容 HANDOFF 保持 PLANNED；批准文字/单帧不等于批准序列/预览。只修改失败字段、创建新版本并复核受影响依赖。

## Method overlay（采用时）

在 Adoption Scope 内检查 Method 的静态可读性、关键帧职责、顺序节奏、反应/反转和声音落点；如果类型效果在 Contact Sheet/Animatic 层仍无法表达，返回 Shot/Scene，而不是交给视频模型猜测。

## Centralized user-generation handoff

用户希望在网页端或同一模型会话中集中生成时，使用 `HANDOFF`，按场景交付可复制提示词包。每帧必须标明：Frame ID、Source Shot、帧类型、目标文件名、参考图编号与准确路径、每张图的角色与 Prompt 绑定句、正向提示词、负面约束、连续性输入、验收点。

每个场景组在 Frame 卡片前一并放入已批准的 Scene Orientation Card（人物站位/路径）、Shot Camera/Axis Overlay（机位、朝向和关系轴）以及该 Frame 的 Composition Guide（或 `NOT_NEEDED` 理由），标明各自 ID、版本、适用 Shot 与未知空间边界；构图图与纯场景底图在无限画布中紧邻正式生成卡。这里只汇总，不重新设计站位或机位。

面向无限画布时，每帧是一张独立卡片，按依赖顺序排列；分开写操作、`直接复制｜主提示词`、`直接复制｜负向提示词`、`不要复制｜验收与回传`。提示词正文不夹入文件路径、说明或验收清单；依赖帧未批准前标 `WAITING_DEPENDENCY`。
场景组首页先列可并行帧与需等待前置 Frame 审核的顺序；每张帧卡按编号写 `核对站位/机位图与前置帧 → 选新建/编辑入口 → 按序上传参考图 → 设置已核实参数 → 复制提示词 → 生成独立原图并按 Frame ID 保存 → 回传；用户可同时注明“审核通过”，否则进入像素审核`。具体平台语法未核实时标待确认，不让用户自行猜测 `@` 绑定。

- 普通单人或空间帧可在同一批次独立生成。
- 同一连续动作的手部传物、拥抱、托举等高风险帧，先批准 Start，再按姿态/状态依赖编辑派生；参考链同时回锚原始身份、服装与空间，不只复制前帧。若首尾机位差异过大、跨年龄或艺术变化需要不同母版，按批准规则列参考职责与验证方案，不能强行从不适用 Start 编辑，也不能独立随机生成后冒称连续。
- 用户回传时以 Frame ID 命名，或明确说明每张图对应的 Frame ID；无法对应的文件不进入 manifest。
- 收到未获用户明确批准的图片后逐张像素审核和顺序审核；用户明确批准的 Frame 直接按其范围入库，若只批准单帧，不推定整个序列或 Animatic 已通过。
- 提示词包得到所需授权前不生成。Project Brief 中已选方式作为默认路线，不重复询问；只有 `OPEN` 或用户明确改选的批次才选择方式，并记录覆盖。连续动作的一组依赖帧视为同一批。

## Frame selection rules

满足 Workflow 第 13 步全部生产放行条件时，Board 状态明确记 READY FOR MOTION DESIGN，供下一阶段读取；未满足则保持 PLANNED / GENERATED_PENDING_REVIEW / REWORK，不以单帧 USER-APPROVED 代替整段就绪。

- **Storyboard Panel:** 证明一个镜头的主要构图与动作节点。
- **Hero Frame:** 只为最能代表场景主题、转折或审批方向的少量画面；不是每镜美化图。
- **Start Keyframe:** 运动开始前必须稳定的状态。
- **End Keyframe:** 运动完成后必须抵达、并供下一镜继承的状态。
- **Intermediate State:** 只有复杂接触、转面、变形、动作阶段或摄影机路径无法由首尾推断时才增加。

## Composition Guide rules

- ID 使用 `S005-SH01-CG01`，与 Frame ID 分离。
- 类型：`EXISTING_SOFT_REFERENCE / CLEAN_SCENE_BLOCKING / GRAYSCALE_LAYOUT / NOT_NEEDED`。
- 状态：`PLANNED / GENERATED_PENDING_REVIEW / COMPOSITION_APPROVED / REWORK / NOT_NEEDED`。
- 正式 Frame 必须引用 Guide ID / Version / Path，并声明允许影响与禁止迁移。
- 构图图可以低细节、灰盒或使用旧人物，但旧身份、服装、道具、背景、天气和光色只能标为禁止迁移。
- Composition Guide 不是可复用视觉资产，不进入 `assets/`；不是正式 Frame，不进入 Animatic 或视频首帧。

## Non-negotiable boundaries

- 不改写 Shot List 的景别、机位、轴线、动作或时长；发现不可视化问题返回 Shot Design。
- 不把 Coverage Table 当成新的 Shot List；表内摘要与上游不一致时标 `CONFLICT / RETURN_SHOT`，不得就地修正。
- 不把一张漂亮图当作完整 Storyboard。
- 不把分镜降成 Shot List 的保守插图；允许在已批准机位、轴线、动作和状态范围内做大胆构图，但不得借“创作”越权改写镜头事实。
- 不生成视频，不写最终视频 Prompt、模型参数或运动语句包。
- 不把运动模糊、速度线或姿态夸张当成 Motion Design 的替代。
- 不用文字标签、箭头或长说明掩盖错误构图；需要注释时与画面分离。
- 不把 PLAN_ONLY、GENERATED_PENDING_REVIEW 或 SELF-REVIEWED 误报为 USER-APPROVED。
- 不把首尾静态通过等同于中间运动可生成，不把未播放的 Animatic 计划写成节奏实测通过。
- 不覆盖已批准原图，不让旧状态参考覆盖当前状态，不把 Contact Sheet 当作图生视频首帧。

## Completion gate

- 所有 Shot ID 均有必要且不过量的 Frame；
- 剧本 Scene/Beat/Action/Dialogue/Sound Cue 到 Shot、Shot 到 Frame 的覆盖关系完整，缺口和不需要静态画面的理由明确；
- 代表时刻与 Shot 功能一致；
- 相邻帧的身份、空间、视线、道具、光线与状态连续；
- 每帧继承确切 Look/Light State，表演以可观察快照而非抽象情绪呈现；
- 多镜段落完成顺序审阅；Animatic 计划仅审文字安排，生产放行须实际预览的完整播放审核证据或用户对确切预览批准，不能以 NOT_RENDERED 代替；
- Rhythm Map 能解释快慢变化与必要停留，节奏不依赖无动机快切、音乐铺满或镜头拖延；
- 主画幅和已知交付变体的安全区、裁切或重构图决定明确；
- 生产级所需参考图真实存在且用途已批准；内容计划的待补路径与验证条件明确，引用职责和禁止影响清楚；
- 每个复杂／关键 Frame 已映射到 `COMPOSITION_APPROVED` 的 Composition Guide；简单帧有具体 `NOT_NEEDED` 理由；
- 关键状态帧先于依赖帧验证，实际观察、依赖范围与批准帧冻结状态明确；
- Hero/Start/End 类型使用有明确理由；
- Viewing Stance、构图要求、艺术规则与注意力可读性得到逐帧继承/检查，同镜关键状态对有静态依据及待运动验证项；
- 实际图片已逐张及顺序审核，或用户对对应帧/序列明确批准并登记范围，或明确保持 PLANNED；
- 没有越界进入完整运动、最终 Prompt 或视频生成。
