---
name: film-shot-director
description: 将状态为 READY FOR SHOT DESIGN 的 Scene Design Pack 与已批准资产转化为完整 Shot List 和镜头连续性账本，设计景别、机位、构图关系、轴线、镜头运动、焦点、时长、声音与切点。用于场景调度已确定后的摄影设计；不用于生成分镜图、关键帧、图片/视频提示词或实际视频。
---

# Film Shot Director

把已经成立的场景调度投影成有叙事功能的镜头链。先固定世界状态，再选择摄影机；摄影术语必须解释观众为何这样看见行动。

## Required inputs

1. `Scene Design Pack`，状态为 `READY FOR SHOT DESIGN`
2. `screenplay.fountain`
3. `world-visual-bible.md`
4. `asset-manifest.md` 与当前范围所需的 APPROVED 资产
5. 用户锁定的时长、画幅、镜头或平台限制（如有）

继承上游确切版本、本次范围和交付边界。`DRAFT_ASSET_PENDING`、RETURN 或缺少当前用途批准证据时不得创建生产级 Shot List；仅内容交付可用 `SHOT EXPLORATION` 完整交付镜头文字稿，注明待验证依赖，不要求先回传媒体。文本完整不等于生产就绪；上游事实冲突须返回责任阶段，不能在草稿中静默修补。

## Load resources

- 设计镜头前读取 `references/shot-design-guide.md`。
- 创建或检查交付物时读取 `references/shot-list-contract.md`。
- 使用 `assets/shot-list-template.md` 与 `assets/shot-continuity-template.md`。

## Outputs

默认保存：

```text
AIGC Creater/projects/<project-id>/direction/
├── shot-list.md
└── shot-continuity-ledger.md
```

## Workflow

1. **Verify scene readiness.** 确认场景范围、Scene Review、状态及当前所需资产文件/版本的 Approval Scope；保留锁定对白、行动段、调度、信息与 Must Show/Withhold。当前已批准用途不代表新增反向视图、接触或状态也已通过。
2. **Fix world coordinates, look and atmosphere state.** 继承场景的 `VISIBLE / INFERRED / UNKNOWN` 空间证据；有方位卡时在连续性账本中引用 Card ID，并在其上叠加主关系轴、允许摄影机区域、人物/道具位置、行动路径和每镜屏幕方向；同时继承 `Narrative Look Arc / Scene Look & Light State / Atmospheric Medium State` 与光源方向、空气来源/分布/驱动。空间敏感场景缺方位卡则返回 Scene；世界不为画面左右标签移动；需要超出证据的大幅反拍、绕拍或穿越时先返回 Scene/Asset 补证。无叙事或物理触发不改变光线、材料或空气响应。
3. **Set the viewing stance and shot sentence.** 先明确跟随谁的感受或采用何种观察立场、与人物的感受距离、观众相对人物的信息先后，以及何时改变立场。再说明整场镜头链如何引导注意并抵达 Exit State；进入、发展/保持、揭示/反应和退出按场景实际需要安排，不强制升级或权力转移。关键选择有实质分歧时比较覆盖方案，记录 Creative Intent / Audience Effect / Continuity Cost / Generation Risk，不为每场机械凑“常规/大胆”配额。
4. **Choose coverage by function, contrast and rhythm role.** 每个镜头必须承担新动作、信息、关系、反应、空间或节奏功能；从 Scene Rhythm Map 继承它是建立、加压、延迟、反应、释放还是余韵，并说明所需停留。删除重复覆盖；相邻镜头检查景别、角度、焦点、运动方向和视觉重量是否形成有动机的变化，允许有意重复，不机械轮换。
5. **Choose projection and composition relations.** 根据观看立场选择景别、角度、机位、焦点和透视；以主体占比/位置、人物间距、前中后景、负空间、遮挡与视觉重心说明 Must Read / Must Withhold 如何成立。按需描述，不设数值配额，不强制三层空间或浅景深。只有格式已知且数值有用时才写焦距，否则用 Lens Intent；构图意图供下一阶段验证，不冒称像素已通过。
6. **Design stillness or movement.** 运动写起点、启动依据、路径/主体关系、阶段、终点和停止理由；依据可来自动作、声音、感知或批准的艺术规则，不强制新增剧情事件。静止镜头写等待/观察对象和保留时间的作用。区分人物、摄影机、焦距与焦点变化；观念性漂移仍须说明注意力或感受如何组织，不用“电影感”替代路径。
7. **Design cuts, handoffs and sound.** 每个切点说明由动作、信息、反应、声音或时间变化触发；为相邻镜头记录前镜结束状态、后镜进入状态与匹配锚点。声音跨镜只在有叙事理由时使用。
8. **Bind assets, scene beats and formats.** 为每镜绑定所需资产/视觉状态的确切版本与用途批准证据，并回指 Scene Beat ID；将场景的察觉、回应、等待或延续投影成当前景别可读的行为，不添加微动作。一个行动段可跨镜，一镜也可承载连续段落；对白换人不自动切镜。关键帧尚未创建时仅登记 Planned Frame Need / State Dependency，不要求文件或版本；Stage 11 创建后由对应 Frame 合同绑定实际版本。登记主画幅、安全区域与变体策略。
9. **Close timing.** 镜头时长总和与请求范围目标一致；对白、动作与停顿必须放得下。未知总时长时给估算和假设，不伪装精确。
10. **Build state and dependency ledgers.** 登记轴线、屏幕方向、视线、表演状态、声音交接、实体数量/所有者/位置/可见性/物理状态/动作阶段/知情状态，并为每镜写 `Depends On / State Changes / Affected Dependents`。状态变化镜头先于依赖镜头进入分镜与生成。
11. **Write camera feasibility cards.** 对空间敏感镜头记录摄影机起点、朝向、机高、距离、轴线侧、必须可见锚点、遮挡、可达性和证据风险；单张参考图不能为未知反向空间提供保证。
12. **Classify risk without erasing intent.** 按现有风险分类标 LOW / MEDIUM / HIGH，保留创作意图，必要时比较切点/动作分段/替代覆盖及表达代价。HIGH 写风险假设并选择覆盖核心风险的最小 PILOT CANDIDATE 集合；高风险本身不等于文本设计不通过，也不要求本阶段先生成样片。
13. **Review and route.** Shot Review（PASS / REVISE / NOT_EVALUATED）检查观看立场、构图可读性、Scene Beat 覆盖、镜头衔接、时间与资产用途。PASS、当前范围上游就绪且无阻断项才标 READY FOR STORYBOARD；局部设计问题 REVISE，上游冲突 RETURN。内容稿标 SHOT EXPLORATION 并带待验证依赖交付；文字审阅、后续构图/画面验证和 Pilot 结论分开，不冒称已生成成功。

## Method overlay（采用时）

将已采用 Method 的镜头角色、`MAIN / SUPPORT / HOLD`、节奏、声音落点和风险假设写入指定 Shot；不得用类型镜头语法替代场景目的、轴线、状态交接和叙事因果。未验证 Method 风险必须进入 Pilot Candidates。

## Per-shot requirements

- Shot ID / Source Scene & Beat
- Duration Estimate
- Narrative Function
- Framing / Angle / Camera Position
- Lens Intent or justified focal length
- Focus / Depth relationship
- Viewing Stance / Information Alignment; Composition Relations / Must Read / Must Withhold
- Character & Prop Blocking
- Visible Action in phases
- Camera Movement: start / trigger / path / end
- Stillness Purpose or Movement Basis / Subject Relation / Stop Reason
- Dialogue / Sound
- Rhythm Role / Required Hold / Energy Shift Trigger
- Cut In / Cut Out motive
- Previous End / Current Start / Next Handoff
- Continuity In / Out
- Depends On / State Changes / Affected Dependents
- Camera Feasibility: start / aim / height / distance / axis side / anchors / occlusion / reachability
- Required Asset IDs
- Scene Look & Light State ID / Version and approved deviation/trigger
- Narrative Look Arc / Atmospheric Medium State and approved physical change trigger or HOLD
- Presentation Mode / Artistic Rule IDs & Versions / Layer / Trigger / Preserved Features or HOLD
- Observable Performance: entry posture/weight, gaze, breath/pause, hand-prop, necessary costume/hair response, exit
- Exact Character / Costume / Makeup-Hair / Location-State / Prop / Material Versions
- Primary Aspect / Safe Region / Delivery Variant Strategy
- Production Risk / Risk Hypothesis / Pilot Priority
- Creative Choice / Intent / Audience Effect / Continuity Cost / Generation Risk
- Planned Frame Need / State Dependency（尚无实际帧时不绑定虚构版本）

## Non-negotiable boundaries

- 不改写场景调度来迁就想要的镜头；无法拍清则返回 Scene Design。
- 不为“丰富”机械轮换景别、角度、焦段或运镜。
- 不因担心出错而默认最普通的覆盖；未锁定字段属于创作空间，但每个大胆决定都必须服务叙事、可拍清、可连续并可说明代价。
- 不把推镜等同于变焦，不把横移等同于摇摄，不用“环绕”隐藏未定义路径。
- 不越过关系轴；如必须越轴，设计可见的轴线重建或过渡。
- 不把所有对白自动拆成正反打，也不为了覆盖率重复同一信息。
- 不生成 Storyboard 图、Hero Frame、Keyframe、图片 Prompt、视频 Prompt 或模型参数。
- 不声称 Shot List 已经被模型成功执行。

## AIGC-aware constraints

继承 Scene 的 PHYSICAL / STYLIZED / MIXED 与确切艺术规则。真实空气须有物理来源/驱动或 NONE；非物理艺术层按批准的作用、触发和保持项设计，不强制摄影写实，不借艺术模式改动身份、地标、故事或时间逻辑。空间证据与轴线按批准的空间规则检查，刻意非连续转换明确依据和观众定位方式，不误记为连续匹配。

- 记录单镜头内人物数量、身份转面、手部/道具交互、文字、反射、遮挡、复杂运动与时长风险。
- 风险高时比较镜头边界、动作阶段或切点方案及表达代价；不自动采用最保守覆盖，不能牺牲锁定故事和人物决定。
- 一个后续生成 Clip 应有清楚的进入状态、可见触发、主要动作和结束状态；不要在一个镜头里暗藏多个无法连续生成的剪辑。
- 一个 Clip 只设一个 Primary Narrative Job 和 Primary Action；次级动作只能支持主动作。无法保持该层级时优先拆镜或返回 Scene Design。
- 这些是制作约束，不是模型 Prompt。

## Completion gate

- 请求范围内所有场景动作、对白和 Must Show 均被覆盖；
- 每个镜头有独立功能且镜头链构成完整句子；
- 场景的视觉策略、覆盖节奏与相邻镜头交接明确；
- 观看立场、构图关系、Must Read/Withhold 与 Scene Beat 映射可供分镜验证；
- 镜头节奏角色和停留理由继承 Scene Rhythm Map，不按固定时长或景别公式切分；
- 每镜继承确切 Look/Light State，表演是可观察链而非抽象情绪；
- 每镜继承 Narrative Look Arc、物理空气状态与独立艺术规则，变化有对应依据；
- 每镜使用的资产与环境状态均绑定到确切版本；主画幅和已知交付变体的安全构图风险已处理；
- 时长总和闭合或明确为估算；
- 轴线、屏幕方向、视线、光源和物件状态连续；
- 空间敏感场景的机位与屏幕方向可在同一场景方位卡上复核，未偷偷改动地标或未知区域；
- 状态变化、镜头依赖和相依制作顺序明确；空间敏感机位有证据边界；
- 运动有触发与终点；切点有动机；
- 资产 ID 与版本可追溯；
- Shot Review PASS、当前所需用途有批准证据且无阻断项才生产放行；计划关键帧不是缺失资产，不要求提前创建；
- 没有分镜图、关键帧或 Prompt 泄漏。
