# Shot List Contract

## Status

- `SHOT EXPLORATION`: 内容稿或上游/用途证据待验证的镜头文字方案，可完整交付，不得进入生产；问题与依赖明示。
- `READY FOR STORYBOARD`: 请求范围镜头表和连续性账本完整，Shot Review PASS、上游就绪、所需资产用途在批准范围内且无阻断项；不代表实际画面或模型验证通过。
- `RETURN`: 返回 Scene / Asset / Screenplay / Research。

## Shot list sections

1. `Shot Plan Identity`
2. `Coverage & Status`
3. `Scene Shot Sentences`
4. `Scene Visual Strategy & Coverage Pattern`
5. `World Coordinates & Axis Rules`
6. `Camera & Space Feasibility`
7. `Shot List`
8. `Shot Asset & State Matrix`
9. `Format & Safe Composition`
10. `Shot-to-shot Handoffs`
11. `State Change & Dependency Order`
12. `Timing Summary`
13. `Coverage Audit`
14. `Production Risks & Pilot Candidates`
15. `Decision Register`
16. `Next Stage`

另设 Viewing Stance & Composition、Scene Beat Coverage、Artistic Rule Projection 与 Shot Review；Identity 记录上游版本和 Delivery Boundary。为保持主表可读，关系、覆盖和审核放在这些配套段落，以 Shot ID 引用，不重复扩展成多个事实源。

镜头合同是注意力、表演和连续性的事实源；后续 Production Unit Card 只能编译这些字段，不能在执行卡中首次发明动作或反应。

## Shot IDs

使用稳定格式 `SC<scene>-SH<shot>`，例如 `S005-SH01`。插入镜头时使用后缀 `S005-SH01A`，不要为一次修改重编号全部镜头。

## Shot table minimum

| Shot ID | Duration | Function / Rhythm Role | Framing / Angle | Camera / Lens Intent | Blocking & Observable Performance | Movement | Dialogue / Sound | Look / Light State ID & Deviation | Cut Motive / Required Hold | Continuity | Depends On / State Change | Assets | Risk / Pilot |

镜头表应能被不看内部推理的人理解。复杂动作可以在单元格内分阶段，但不得把模型 Prompt 塞入表格。

## Shot asset and state matrix

每镜按需绑定确切版本：`Character / Costume / Makeup-Hair / Location or Environment State / Narrative Look Arc / Scene Look & Light State / Atmospheric Medium State / Props and Hand State / Material Detail Plates`，并列 Required Use / View / State 与 Approval Scope Evidence；资产级 APPROVED 不自动覆盖新用途。必需上游资产的模糊名称、未批准版本或不存在文件标为 Blocker；不允许 Prompt Adapter 自选版本。Look/Light 默认继承，偏差写触发与批准依据；真实空气记来源、分布与物理驱动或 NONE，非物理层见 Artistic Rule Projection。

Start/End Frame 尚未创建时只写 `Planned Frame Need / State Dependency`；不索要未来帧的文件或版本，不将其列为本阶段缺失资产。Stage 11 创建后由 Frame 合同/清单绑定实际版本；若复用已有帧，则引用其确切 ID/版本与批准范围。

## Viewing stance, composition and scene coverage

场景层记 `Viewing Stance / Felt Distance / Information Alignment / Shift Basis`；每镜按需记相同立场或偏差依据。Composition Relations 包含 Subject Scale/Position、Interpersonal Distance、Depth Layers、Negative Space、Occlusion、Visual Center、Must Read / Must Withhold，未涉及项可记 NOT_APPLICABLE。它是待分镜验证的要求，不是像素通过证据。

Scene Beat Coverage 用 `Scene / Beat ID / Required Action-Response or HOLD / Shot IDs / Visibility or Sound Evidence / Gap` 核对行动、对白和声音，不强制一段一镜或发言者特写。保持、等待和倾听有观看作用即可，不强制变化。

Artistic Rule Projection 用 `Shot ID / Presentation Mode / Artistic Rule ID & Version / Layer / Trigger / Preserved Features / Validation Need`；无变化写 HOLD，无非物理规则写 NONE。继承上游批准空间/时间规则，有意非连续转换写依据及定位方式，不伪装连续匹配。风险不能覆盖规则，也不能消除实际生成验证。

`Blocking & Observable Performance` 至少把所需情绪转换为可见的姿态/重心、视线、呼吸/声音/停顿、手与道具动作和必要的服装/头发响应，并说明进入—变化—退出。不得只写“更悲伤”“自然眨眼”或无动机微动作。

## Attention and response handoff

每镜另记录：

- `MAIN`：本镜唯一主要注意对象或主要变化；
- `SUPPORT`：提供关系、空间或气氛信息，但不得抢走主要注意；
- `HOLD`：必须稳定、不应自行运动或变化的对象与状态；
- `PREVIOUS RESIDUE`：上一镜或镜前动作留下的姿态、环境、声音或物件状态；
- `TRIGGER`：引起变化的可见动作、声音或事件；
- `DELAY`：有叙事意义的反应间隔，没有则写 `NONE`；
- `VISIBLE CHANGE`：观众实际能看到或听到的变化；
- `HANDOFF`：切出时交给下一镜的状态、视线、动作相位或声音。

这些字段不要求每镜都复杂化。静态建立镜可以将 `TRIGGER / DELAY` 标为 `NOT_APPLICABLE`，但 `MAIN / HOLD / HANDOFF` 仍应清楚。

## Source freshness

每镜记录所依赖的 Screenplay、Scene、Asset 和 Visual State 版本以及 `CURRENT / STALE / BLOCKED / RECOMPILE`。上游变化后先更新影响表；`STALE / BLOCKED` 镜头不得进入 Storyboard，`RECOMPILE` 只表示重新输出派生视图，不允许在下游偷偷修稿。

## Format and safe composition

在摄影设计阶段登记主画幅和已知交付变体。每镜说明必须保留的主体/文字安全区域、允许裁切范围以及是否必须为竖版等变体重新构图。未知交付需求保持 OPEN，不假装一张构图可以无损适配所有比例。

## Risk and pilot fields

- `Risk Level`: LOW / MEDIUM / HIGH
- `Risk Type`: Identity / Multi-character / Contact / Spatial / Camera / Effect / Text / Lip-sync / Duration / Other
- `Risk Hypothesis`: 这个镜头需要证明的生产假设
- `Pilot Priority`: REQUIRED / OPTIONAL / NO
- `Pilot Coverage`: 若被选中，它覆盖哪些全片共性风险

存在 HIGH 风险时至少选择覆盖核心风险的最小 Pilot 集合。Pilot Priority 只决定实际生成顺序，不改变镜头叙事重要性。

## Timing

- 每场列目标时长、镜头合计和差值。
- 项目时长未锁定时，标 `[ASSUMED ESTIMATE]`。
- 对白速度、动作完成时间和停顿必须合理；不要用小数秒制造虚假精确。
- 每镜标记它在 Scene Rhythm Map 中的角色与必要停留；镜头长短由行动、信息、反应和声音决定，不按固定平均镜长套用。

Timing Summary 记录 Method / Scope / Target / Shot Total / Difference / Status（ESTIMATED / TIMED / NOT_EVALUATED）。基于文字的估算与实际读演/计时区分；目标未锁定可估算，已锁定目标的差值须解释并解决，不以压缩必要停顿凑秒数。

## Shot review

使用 PASS / REVISE / NOT_EVALUATED，列 Covered Shots、Evidence & Findings、Blocking Issues / Owner、Pending Media Validation。检查观看立场、构图可读要求、Scene Beat 覆盖、交接与时间、确切用途批准和风险方案。局部问题记 REVISE，不改写上游；事实冲突 RETURN。仅内容稿可交付 SHOT EXPLORATION，无需先回传媒体；READY 仍须满足生产级前提。后续构图、画面和 Pilot 效果尚未验证时明示，不把高风险标签或未产生的关键帧本身当作文本失败。

## Continuity ledger

至少追踪：

- 对空间或动作连续性敏感的场景，引用 Scene Orientation Card ID / Version，在同一世界方位上叠加关系轴、允许机位区与每镜屏幕投影；普通单点场景继承 `NOT_NEEDED` 理由
- 世界坐标与轴线
- 屏幕方向与视线
- 人物位置和身体朝向
- 道具持有、位置与状态
- 光源方向与时间状态
- 服装/身体状态
- 前镜结束帧与后镜进入状态
- 实体 ID、数量、所有者、世界位置、可见性、物理状态、动作阶段和角色知情状态
- `Pre-state → Event → Planned Post-state`；实际画面生成前不得填写 `Actual Observation`

相邻镜头另记 `Previous End / Next Start / Match Anchors / Allowed Change / Transition Motive`。交接不能只写“连续”或“自然切换”。

## Camera feasibility card

空间敏感镜头至少记录：`Camera Start / Aim / Height / Distance / Axis Side / Must-see Anchors / Occlusion / Reachability / Evidence Level / Risk`。`INFERRED` 机位必须写依据；`UNKNOWN` 空间不得标为生产就绪。

## Dependency order

每镜记录 `Depends On / State Changes / Affected Dependents`。会改变所有权、位置、身体、环境、知识或动作阶段的镜头标为 `STATE-CHANGE CRITICAL`，在下游先验证；依赖镜头不能引用尚未被实际观察确认的生成结果。
