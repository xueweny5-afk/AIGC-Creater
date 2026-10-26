---
name: film-continuity-qc
description: 对实际生成的图片或视频 Take 进行完整播放、关键帧与边界帧检查，核对故事、身份、空间、轴线、动作、物理、道具、光线、时长、声音和跨镜连续性，并输出 QC 报告、问题账本、Take 选择与最早返工路径。没有真实媒体或未实际检查时不得判定通过。
---

# Film Continuity QC

用真实媒体证据判断 Take 是否忠实、连续、可剪辑。文件存在、平台成功和漂亮静帧都不能替代完整播放审核。

## Required inputs

1. `generation-manifest.md` 与实际 Take 文件
2. Prompt Package、Motion Spec、Storyboard/Frames
3. Shot List、continuity ledger、Scene Design
4. APPROVED 资产合同与 Visual Bible
5. Screenplay 与用户验收标准
6. `atmosphere-state-register.md`（存在独立空气状态合同时）与 Animatic Rhythm Map
7. 对应 Production Unit Card、源版本与 Source Freshness
8. 项目采用 Method 时的 Adoption Receipt、Method Version、专项验收与验证边界

继承本次范围和交付边界。没有实际媒体/可用查看工具时可交审核计划、验收点与缺口，保持 NOT_EVALUATED；不得从提示词、日志或缩略图补造播放、画面或音频结论，也不要求先回传媒体才交付文字计划。

## Load resources

- 审核前读取 `references/continuity-qc-guide.md`。
- 创建报告和问题账本时读取 `references/qc-contract.md`。
- 使用 `assets/qc-report-template.md`、`assets/issue-ledger-template.md` 与 `assets/take-selection-template.md`。

## Outputs

```text
AIGC Creater/projects/<project-id>/qc/
├── qc-report.md
├── issue-ledger.md
└── take-selection.md
```

## Workflow

**用户人工放行分支：** 用户对可识别的 Take 明确说“审核通过 / 就用这版”时，只核对真实文件、Unit/Take ID 和版本，登记 `USER-APPROVED`、批准范围与时间并写入 `take-selection.md`；跳过下列 Codex 画面/声音 QC，不创建虚假的 `QC_PASS`、播放证据或问题结论。用户只批准单个 Take 时，不推定整段顺序或其他 Take 已通过；用户明确批准整段时按该范围记录。后续可使用人工批准的 Take。

1. **Verify media identity.** 精确解析 Take 路径、Unit/Shot/Take ID、文件大小、容器、时长、画幅、帧率和音轨；确认审核的就是 manifest 指向的文件。
2. **Check evidence and change impact.** 文件缺失/损坏标 MISSING_MEDIA，文件可读但缺检查能力的维度标 NOT_EVALUATED；不可从日志推断通过。源或卡片 STALE/BLOCKED/RECOMPILE 时先核对 Changed Fields / Affected Scope / Dependency Match，不仅因版本号变化重生成。无关变更经责任上游确认等价、更新引用/派生视图并恢复 CURRENT 后可复用原 Take；受影响内容返回对应层，状态未解决不得 PASS。
3. **Inspect according to media type.** 视频正常速度从头到尾播放，音频完整听取适用区间，图片查看独立原图整体及必要细节，Playback 记 NOT_APPLICABLE。记录实际检查对象、版本、范围和工具。静帧/抽帧不替代视频播放；无音轨或未检查声音不得凭画面推断声音通过。
4. **Inspect boundaries and frames.** 检查首帧、尾帧、运动转折、接触、遮挡、转面和疑似闪烁区间；必要时逐帧或高密度抽帧。
5. **Check correctness and expression.** 正确性核对 start/continuation or trigger/action-HOLD/end、摄影机、身份、实体守恒、空间、光线、声音与时长；表达核对 Viewing Stance / Information Alignment、MAIN/SUPPORT/HOLD、构图的 Must Read/Withhold、关系/感知、必要停顿和结束作用。两类分别记 QC 结果与可观察证据，不以无穿帮代替表达成立，也不凭主观不喜欢否定符合合同的选择。
6. **Check cross-shot continuity, atmosphere, rhythm and dependencies.** 比较前 Take 结束与后 Take 开始的人物位置、朝向、持物、可观察表演链、Narrative Look Arc、Scene Look/Light State、Atmospheric Medium、材料响应、环境和动作相位；有场景方位卡时按 Card ID / Version 核对人物所在区域、行动方向和机位轴线，不从画面左右倒推世界地标。无触发的灯光/材质/空气密度漂移不得因画面更漂亮而通过；无来源粒子、雾气和持续飘动属于可诊断问题。按顺序播放时核对 Rhythm Map 的压力变化、必要反应/静默与能量转折，不让无动机快切或拖长通过。状态变化 Take 记录 `Actual Observation`，与 Planned Post-state 比较，并列出需要重检的 `Affected Dependents`。
7. **Check adopted Method outcomes.** 在 Adoption Scope 内检查核心机制、MAIN/HOLD、类型节奏或转换、声音职责、典型失败和目标观众体验。通用 QC 或 Method-specific QC 任一出现 BLOCKER/MAJOR 都不能通过；“画面好看”不能替代方法目标。
8. **Separate symptom from cause.** Issue 记录视频时间码/图片区域、Expected Contract & Version、Actual Evidence、Audience or Edit Impact、严重度、责任层/依据与不确定性。原因未证实写 HYPOTHESIS，列 Confidence / Basis / Next Diagnostic Check，不直接将所有问题归为模型失败。学习候选仍用相同维度比较改善/保持/恶化/未评估及副作用，不把相关性写成通用因果。
9. **Select within reviewed scope.** 无 BLOCKER/MAJOR 且所需维度已检查的 Take 可 QC_SELECTED；Take、相邻边界、整段顺序分别记 Scope / File-Version Set / Result / Evidence / Pending Checks。单镜通过不推出跨镜/整段通过，尚未检查保持 NOT_EVALUATED。人工批准继续 USER-APPROVED 路径，冻结对应版本，不伪造 QC 结果。
10. **Route and recheck targeted repairs.** 返回有证据的最早责任层；不确定先诊断，不静默改合同。Post Fix 写 Proposed Fix / Protected Intent / Feasibility Evidence / Residual Risk / Verification Scope，不能证明保留构图、主动作和必要停顿则不承诺后期可救。重生成或修复后以确切新版本、原 Issue ID 和原维度复核，记录关闭证据并只重检受影响依赖；未复核不关闭。能力伪支持返回 Prompt/Model Verification。
11. **Route learning candidates.** 跨阶段 Method 机制和专项验收证据交 `film-video-method-curator`；具体 Prompt、参数、模型和参考职责的真实 Baseline/Candidate 交 `film-generation-pattern-curator`。缺媒体、缺对照或多个变量混改时仍可记录观察/Confound，但不能提升规律。
12. **Resolve the pilot gate.** 对 `TECHNICAL_PILOT` 逐项回答风险假设是否被真实媒体证据支持，并核对 Changed Variable、Held Constant、Confounds 与适用边界。全部核心假设通过才标 `PILOT_VALIDATED` 并允许对应范围的 Production；失败时输出最早返工层和下次最小验证范围，不把样片通过写成全片通过。

## QC dimensions

继承 Presentation Mode / Artistic Rule IDs & Versions / Layer / Change-HOLD / Preserved Features。真实物理层按作用力与连续性检查；梦境、形变、绘画空间或刻意非连续按批准规则和观众定位方式判断。随机身份/物件/地标漂移仍是错误，不用艺术模式豁免；持续动作、等待和感知积累不强制新触发或情绪转折。第 6 步的空气物理要求仅适用于真实空气，不将象征艺术层误判为无来源雾气。

- Story and shot fidelity
- Viewing stance, attention, composition read, emotional/relational purpose and approved artistic rules
- Character / location / prop identity
- Anatomy, geometry, contact, weight and occlusion
- Blocking, world coordinates, axis, gaze and screen direction
- Motion phase, speed, acceleration and stop behavior
- Camera path vs zoom/pan/subject motion
- Light, weather, texture, exposure and temporal consistency
- Atmospheric medium source, distribution, motion driver and cross-shot continuity
- Rhythm Map, required reaction/hold/silence and motivated energy change
- Text, logos, watermarks and unwanted subjects
- Duration, edit handles and cutability
- Dialogue, lip-sync, audio presence, noise and sound continuity
- Cross-shot entrance/exit state
- Entity quantity, ownership, release/acquisition, visibility and knowledge state
- Planned post-state vs actual observation and dependent-shot impact
- Learning candidate comparison: baseline / changed variable / same QC dimensions / new side effects / confounds

## Status and severity

- `NOT_EVALUATED`
- `QC_PASS`
- `QC_PASS_WITH_NOTES`
- `QC_FAIL_REWORK`
- `MISSING_MEDIA`

Severity:

- `BLOCKER`: 故事、身份、主要动作、连续性、权限或文件不可用。
- `MAJOR`: 明显影响可信度或剪辑，通常需重生成/上游修改。
- `MINOR`: 可在后期局部修复或经记录后接受，不改变核心。
- `ACCEPTABLE_VARIATION`: 与合同不冲突、不会破坏身份/状态/剪辑的自然微差；记录观察即可，不创建返工任务。

## Non-negotiable boundaries

- 不在未查看完整媒体时判 PASS。
- 不以单张漂亮帧、自动探测、平台成功或时长匹配判 PASS。
- 不把不同文件的检查结果套到当前 Take。
- 不用模糊形容词替代时间码和可见证据。
- 不在 QC 中静默修改 Prompt、镜头或资产；只路由。
- 不把需要重生成的身份、肢体、物理或动作错误推给后期遮盖。
- 不删除失败 Take，不发布或交付媒体。
- 不因局部失败要求整批重生成；只路由失败 Unit 与其确实受影响的依赖。

## Completion gate

以下逐项播放与 QC 证据要求仅适用于 Codex QC 路径；`USER-APPROVED` 路径以确切文件、ID/版本和人工批准记录完成选片，未检项目保持 `NOT_EVALUATED`。

- 每个候选 Take 有准确路径、与媒体类型相符的检查证据和逐项结果；
- 图片以原图整体/细节检查，视频/音频以实际完整播放/听取记录；不适用项注明，不假造播放；
- 所有问题有时间码、严重度、责任层和建议动作；
- 跨镜边界得到比较；
- 单镜、边界和整段结论各有范围与证据，未评估项不外推为通过；
- 表演状态、服装/环境材质、声音 Bridge 和交付画幅安全构图得到相应检查；
- Look/Light State 与材料响应连续，Prompt 能力回执不存在伪支持；
- Narrative Look Arc、Atmospheric Medium 与 Rhythm Map 得到顺序核对，无动机空气变化和必要停留缺失已被发现；
- 状态变化有 Actual Observation，实体守恒与受影响依赖得到核对；
- 选择结果只来自通过 Take；
- 没有通过 Take 时明确返回，不勉强选择；
- 下一阶段唯一为 Post-production 或最早返工层。
- Technical Pilot 还必须给出 `PILOT_VALIDATED / PILOT_FAILED_RETURN`，并明确它覆盖和未覆盖的风险。
- 返工问题只在新版本复核后关闭；未完成媒体检查的计划只交缺口和待验证项。
