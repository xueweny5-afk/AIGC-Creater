# QC Contract

## Evidence receipt

每次审核记录：

- exact file path
- file size / modified time or checksum
- media probe summary
- inspection method/tool
- full playback completed: yes/no
- playback date
- boundary/key frame timestamps inspected
- audio listened: yes/no/not applicable

另记 Media Type / Reviewed Range / Evidence Limit。图片用整体原图与细节区域、Playback NOT_APPLICABLE；视频/音频保留完整播放/听取证据。可读但无检查工具记 NOT_EVALUATED，文件缺失/损坏记 MISSING_MEDIA；没有媒体可完成审核计划与缺口说明，不做结果判定。

没有这份证据不能 QC_PASS。

审核前核对 Unit Card 与 Source Freshness。STALE/BLOCKED/RECOMPILE 不得通过；先记 Changed Fields / Affected Scope / Dependency Match / Owner Confirmation / Required Update。若变化不影响该 Take，经责任上游确认等价、更新引用/派生视图并恢复 CURRENT 后复用原媒体；只有受影响内容才返工，不仅因版本号变化重生成。QC 不擅自刷新上游状态。

项目采用 Method 时还要核对 Adoption Receipt、Method ID/Version、采用范围和专项验收。通用 QC 与 Method-specific QC 并列：任一存在 BLOCKER/MAJOR 都不能选择 Take。跨阶段方法证据路由 `film-video-method-curator`，具体模型/Prompt/参数对照路由 `film-generation-pattern-curator`。

## Issue fields

- Issue ID
- Unit/Take/Shot
- Timecode range
- Image Region / Coordinates（静态图替代时间码）
- Severity
- Dimension
- Visible evidence
- Expected contract
- Expected Contract Version / Audience or Edit Impact
- Earliest responsible stage
- Cause Status: CONFIRMED / HYPOTHESIS；Confidence / Basis / Next Diagnostic Check
- Recommended action
- Actual observation / affected dependents / re-review scope
- Can post fix? yes/no/conditional
- Post Fix Proposal / Protected Intent / Feasibility Evidence / Residual Risk / Verification Scope
- Status
- Recheck Take-Version / Original Issue ID / Closure Evidence / Remaining Impact

严重度使用 `BLOCKER / MAJOR / MINOR / ACCEPTABLE_VARIATION`。`ACCEPTABLE_VARIATION` 只用于合同允许的自然微差；身份、所有权、动作结果、关键材质或环境状态错误不能降级为可接受变化。

## Routing

- Missing/corrupt output, transient generation glitch → Generation Retry
- Prompt omitted/misencoded approved field → Prompt Adaptation
- Prompt claims unsupported audio, negative prompt, reference or control capability → Prompt Adaptation / Model Verification
- Motion phases physically unclear → Motion Revision
- Shot/axis/coverage wrong → Shot Revision
- Identity/reference contract wrong → Asset Revision
- Story/blocking wrong → Scene/Screenplay upstream
- Minor timing, stabilization, crop, cleanup, sound balance → Post-production candidate

## Take selection

正确性与 Expression & Artistic Rule 分开记结果/证据，使用现有 QC 状态。表达检查 Viewing Stance / Information Alignment、MAIN/SUPPORT/HOLD、Must Read/Withhold、必要停顿、关系或意象；按 Presentation Mode / Artistic Rule IDs-Version 区分真实物理承诺与批准的形变、绘画空间或非连续转换，不强制写实，也不接受无依据漂移。

Take、Boundary、Sequence 各自记录 Scope / Exact File-Version Set / Result / Evidence / Pending Checks；只在所需维度实际检查且无阻断/重大问题时通过。单 Take QC_SELECTED 不代表 Boundary/Sequence PASS，人工批准也只覆盖列明范围。整段尚未审阅可交选片与未评估项，不能冒称全段通过。

`QC_SELECTED` requires no BLOCKER or MAJOR issue. `QC_PASS_WITH_NOTES` may include documented MINOR issues compatible with post-production. User preference can choose among passing Takes but cannot promote a failing Take without recording explicit acceptance and risk.

用户对确切 Take/批次明确说审核通过时，可独立选择为 `USER-APPROVED`：核对文件、ID、版本后记录批准人、时间和覆盖范围，未执行的 QC 项保持 `NOT_EVALUATED`；直接归档并供后期使用，不要求另做 Codex QC，也不标 `QC_SELECTED / QC_PASS`。单 Take 的人工批准不自动代表跨镜或整段通过；明确批准整段时按整段范围登记。若此前有已知失败，仅记录用户决定与原有问题，不要求再次确认。

选定 Take 记录 `Approval Scope` 与冻结版本。局部返工默认只重做失败 Unit；当关键状态变化时，只使明确列出的 dependents 进入 re-review。

问题关闭必须有新媒体/修复版本、原 Issue ID、同维度复核证据和剩余影响；编辑文档或提出修复计划不算关闭。Post 修复是否可行按构图、动作、运镜、必要停顿和艺术规则的保护条件检查，无法证明时保留 conditional/返回上游。

## Technical pilot receipt

Pilot QC 额外记录：

- source risk hypothesis;
- exact Take evidence supporting or refuting it;
- risks covered / not covered;
- pilot gate: `PILOT_VALIDATED / PILOT_FAILED_RETURN`;
- earliest return stage or Production unlock;
- next smallest validation scope when failed.
- failure hypothesis / changed variable / held constant / known confounds;
- applicability boundary：实际证明的模型版本、入口、输入模式、镜头类型与风险，不得外推未测试范围。

只有生成日志成功、静帧好看或单项风险通过，均不能自动解锁整个 Production Batch。

## Learning case evidence

对 Generation 标记的候选使用同一组验收维度比较 Baseline 与 Candidate，记录真实路径、时间码/区域、`Improved / Same / Worse / Not Evaluated`、新增副作用和 Confounds。QC 不负责把相关性写成因果，也不决定公共模式等级；证据交给 `film-generation-pattern-curator`。缺少 Baseline、Candidate、确切模型版本或可对应媒体时标 `NON_EVALUABLE`。

## V1.9 continuity and Method checks

- `Scene Look & Light State ID` 必须能从 Visual Bible 追到 Shot、Frame、Motion、Prompt 与 Take；无叙事触发的光向、冷暖、曝光关系或材料响应漂移属于返工项。
- `Narrative Look Arc / Atmospheric Medium State` 必须贯穿相同链路；介质来源、分布、驱动力或密度无因变化，以及无来源粒子/雾/蒸汽属于返工项。
- `Rhythm Role / Required Hold` 必须能从 Scene/Shot/Animatic 追到 Motion、Prompt、Take 和顺序审核；关键反应、静默或释放点被无因压缩时不得通过。
- 表演按姿态/重心、视线、呼吸/声音/停顿、手与道具、服装/头发响应和进入—变化—退出链审核；抽象标签或随机微动作不能证明表演连续。
- Prompt Coverage Receipt 中的 `UNSUPPORTED` 必须有真实降级；若成品或执行包暗示模型具备未核实能力，按 phantom support 退回 Prompt/Model Verification。
- `MAIN / SUPPORT / HOLD` 与 `PREVIOUS RESIDUE → TRIGGER → DELAY → VISIBLE CHANGE → HANDOFF` 必须能从 Shot/Storyboard 追到 Motion、Production Unit Card 与 Take；主体注意力被次级运动夺走、HOLD 对象无因变化或关键延迟反应丢失时不得通过。
- Production Unit Card 必须能追到当前批准源版本。源 freshness 不是 `CURRENT` 时，先处理版本失效；不能因旧 Take 画面质量较高而沿用已经过期的动作、资产或状态。
