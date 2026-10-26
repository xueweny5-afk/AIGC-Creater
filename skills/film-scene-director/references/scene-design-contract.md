# Scene Design Contract

## Status

- `DRAFT_ASSET_PENDING`: 场景文字设计的当前所需 P0 用途尚未覆盖；可内容交付，不可进入生产级 Shot Design。设计审核另记，不能用此状态代替审核结论。
- `READY FOR SHOT DESIGN`: 请求范围场景覆盖完整、Scene Review PASS、无阻断项，所需 P0 文件/版本/用途/视图/状态在 Approval Scope 内，可供摄影设计。
- `RETURN`: 上游剧本、人物、研究或视觉合同失效。

## Pack sections

1. `Scene Direction Identity`
2. `Coverage & Status`
3. `Director Thesis`
4. `Continuity Contract`
5. `Spatial Evidence Map`
6. `Scene Orientation Cards`（空间或动作连续性敏感时）
7. `Scene Designs`
8. `Cross-scene State Chain`
9. `Performance Continuity Ledger`
10. `Scene Rhythm Map`
11. `Sound Intent & Bridge Map`
12. `Asset & Production Dependencies`
13. `Decision Register`
14. `Next Stage`

另设 `Scene Review` 汇总审核结论；Identity 绑定上游版本、场景范围和内容/生产交付边界。设计局部修订使用 Scene Review 的 REVISE 保留问题，READY 前消除阻断项。

## Spatial evidence map

每个影响调度的空间锚点记录：`Anchor ID / Evidence Level / Evidence Source / Confidence / World Coordinates / Axis / Scale / Unknown Boundary`。

- `VISIBLE`：参考资产或已批准画面中直接可见；
- `INFERRED`：可合理推断，必须写依据与置信度；
- `UNKNOWN`：当前材料无法证明，不能静默填充。

## Scene orientation card

门内外、两岸、多出入口、追逐、传物等场景至少一张。卡片按 Scene ID 引用 Spatial Evidence Map 的 Anchor ID，画固定地标和区域边界，标人物/道具的进入位置、行动路径与未知范围，并列出每次位置或持物变化的触发。方向只表示世界中的相对关系；不写机位、屏幕左右或未经证实的罗盘朝向。普通单点场景写 `NOT_NEEDED` 及理由即可。镜头阶段只能在这张图上叠加摄影机与轴线，不得重排地标。

## Scene design fields

- `Scene ID / Source Range`
- `Direct Cause`
- `Scene Function`
- `Entry State`
- `Character Objectives`
- `Obstacle / Pressure`
- `Initial Tactics`
- `Shift Trigger / New Tactics`
- `Performance Actions`
- `Scene Beat Chain: Beat ID / Event or Sustained State / Perception / Action & Response / Effect or HOLD / Handoff`
- `Performance Continuity: Entry Posture/Weight, Gaze, Breath/Voice, Hand-Prop, Costume/Hair Response → Triggered Beat Changes → Exit Carryover`
- `Blocking & Spatial Power`
- `Spatial Evidence Used / Unknown Boundary`
- `Scene Look & Light State ID / Version`
- `Narrative Look Arc / Atmospheric Medium State / physical change trigger or HOLD`
- `Look / Light Deviation & Trigger`
- `Presentation Mode / Artistic Rule IDs & Versions / Artistic Layer / Trigger / Preserved Features or HOLD`
- `Audience Beat`
- `Information Design`
- `Sound / Silence / Time`
- `Rhythm Intent: story pressure / action energy / sound energy / required hold or silence / release trigger`
- `Sound Cues / Bridges`
- `Required Assets / State Changes`
- `Must Show / Withhold / Avoid`
- `Turn / Exit State`
- `Next-scene Trigger`

## Blocking notation

使用世界空间与资产锚点，例如“老摊主保持在自己的工作面内”“扫帚在两摊分界处停止”。不得写“画面左侧”“镜头前景”或“摄影机推近”；这些属于 Shot Design。

关键位移或不动写明触发、路径/停留处、实际任务或关系理由、他人回应。陪伴、协作和共同注意可承担调度理由，无需制造权力对抗。行动段可持续同一行为或策略；不强制目标转折，不用随机身体动作填字段。

跨场状态至少追踪稳定实体 ID、数量、所有者、世界位置、可见性、物理状态、动作阶段与角色知情状态。交接动作必须同时证明给予者释放和接收者获得同一实体，不能出现复制品。

表演连续性不使用孤立的“更悲伤/更愤怒”。每个主要人物记录进入时的目标与策略、姿态/重心、视线与倾听对象、呼吸/声音/停顿、手与道具互动、服装/头发对动作或环境的响应、触发变化的事件以及带入下一场的退出状态。随机眨眼、无动机喘息和持续飘发不能作为生命感替代品。声音图只定义来源、触发、叙事作用、静默和跨场关系，不提前选曲或生成音频。

Scene Rhythm Map 只描述场景层的压力、行动和声音能量曲线，以及必须保留的停顿/反应与变化触发；不写镜号、逐镜秒数或平均镜长。快节奏必须有信息、行动或声音能量上升，慢节奏必须给人物变化、观察或余韵留下必要时间。

每场继承 Visual Bible 中确切的 `Narrative Look Arc / Scene Look & Light State ID / Atmospheric Medium State / Presentation Mode / Artistic Rule IDs`。没有变化时写 `HOLD`；偏差必须有已批准触发。真实空气变化须有物理触发；非物理艺术层分别记录作用层、触发与保持项，不强制物理解释，也不擅改身份、故事或空间承诺。

跨场记录 `From Scene / Exit → To Scene / Entry / Connection Basis / Discontinuity & Source`。直接延续核对实体和状态；省略、倒叙、并置按批准时间逻辑注明边界，可用声音、感知或意象承接，不能把所有退出强制解释为下一场剧情起因。

## Scene review and handoff

`Scene Review` 使用 PASS / REVISE / NOT_EVALUATED，记录 Covered Scenes、Evidence & Findings、Blocking Issues / Owner、Pending Media Validation。逐项检查行动衔接、表演可执行性、空间/艺术依据、信息/声音与跨场连续性；没有检查不得填 PASS。审核只证明文字设计范围，实际表演、画面和动态效果标待后续验证。

Asset & Production Dependencies 记录 Scene/Beat、Asset ID/Version、Required Use/View/State、Approval Scope Evidence、Gap/Impact、Validation Stage。新增用途超出批准范围时只补受影响依赖，不重做已批准部分。内容包可完成且媒体待验证；READY 必须同时满足文本审核和当前所需用途覆盖，不把未验证全片需求当成当前场景阻断项。

## Return routes

- 场景因果或对白失效 → `Screenplay Revision`
- 人物目标或拒绝权失效 → `Character Revision`
- 世界/资产身份不稳 → `Visual Bible / Asset Revision`
- 历史空间或行动依据不足 → `Research Return`
