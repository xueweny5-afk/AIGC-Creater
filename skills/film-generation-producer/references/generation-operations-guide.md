# Generation Operations Guide

## Preflight

- Prompt Package 与 manifest 版本一致。
- 目标模型 profile 仍为当前 VERIFIED。
- 所有本地文件真实存在且能读取。
- 文件用途与平台输入槽位对应。
- 输出目录可写且不会覆盖现有 Take。
- 用户明确了外部上传、付费、肖像/音频和重试权限。
- Attempt budget 与停止条件写入 manifest。
- Unit 依赖为 READY，批准来源为 QC 或明确人工批准；具体可见状态需媒体检查或用户明确描述的 Actual Observation 回执。

逐 Unit 拒绝 CONTENT DRAFT / NOT_READY / WAITING_DEPENDENCY；核对 Prompt Review PASS、Profile 的平台/版本/任务入口/输入模式、实际槽位、文件版本及用途批准。先前授权在当前范围内继续适用，不逐次重问。人工批准可替代对应范围的 QC 批准，但不能虚构 Actual Observation；依赖具体状态仍须媒体检查或用户明确描述。

## Budget ledger

Unit 与 Batch 分别记 Attempt Cap / Submitted Count / In-flight Requests、Authorized Cost Cap、Reported Actual Cost、In-flight Reservation & Basis、Unsettled/Unknown Charges、Remaining Safe Headroom。生成重提占新尝试，查询/下载不占生成次数；其独立费用仍计账。费用/积分统一口径，预留转结算后只计一次，退款仅凭平台证据更新。平台未返回实际费写 UNKNOWN，不把估算变结算；付费新请求必须能证明在已授权限额内，不能核实则停止提交并保留可独立完成的工作。

## Safe submission

平台支持异步任务时，提交后立即记录句柄。轮询只查询该句柄；超时、进程中断或客户端关闭后先恢复查询。只有权威状态为失败/不存在且重试在预算内时才重新提交。

提交前落盘本次 Unit/Take/Attempt、输入/Prompt 版本与预算预留，响应后立即保存 ID。响应丢失而 ID 未知时查平台历史或幂等回执，不能仅以本地无记录认定失败。恢复按 QUERY / RETRIEVE / NEW_SUBMISSION / NONE 记动作：已完成只下载，已有完整文件只交接；无法确认原任务状态则停该 Unit，不阻断其他无依赖就绪项。取回失败与生成失败分别分类。

## Integrity checks

图像：文件存在、非空、可解码、尺寸/格式可识别。  
视频：文件存在、非空、容器可探测、至少一个视频流、时长/画幅/帧率可读。  
音频：如请求包含，确认音轨存在；内容质量留给 QC。

使用 `ffprobe` 等只读工具时保存实际输出摘要。技术探测不能证明身份、动作或美学正确。

## Failure routing

- 上传/路径/格式错误 → Generation input fix
- 参数越界 → Profile/Parameter fix
- 服务错误/限流 → Platform retry or stop
- 主体、动作、摄影机或结束状态不符 → QC 记录后 Prompt Return
- 身份/资产漂移 → Asset/Prompt/QC route
- 上游镜头物理不可实现 → Motion/Shot Return

## Surgical rerun

重试前记 Failure Class / Authoritative Task Evidence / Diagnostic Hypothesis / Authorized Changed Fields / Stop-or-Return Basis。同类原因再次失败先复核假设；无新依据或可验证改变时停止，不为用完预算随机重生。Prompt/镜头/艺术问题返回责任阶段，Generation 不偷偷改意图。

失败后先确定可见症状、最早责任层和受影响依赖。只创建失败 Unit 的新 Take；已通过 Take 标记 `FROZEN_APPROVED`。若关键状态的实际结果改变，只使其 `Affected Dependents` 失效并重新检查，不扩大为全批次重生成。

## Cost and privacy

只记录平台实际返回的费用/额度；不可推测。输入包含私人、未发布、肖像或授权受限内容时，只上传到用户允许的平台和范围，不自动复制到备用服务。

实际费用与有来源的预算预留分列，后者只是额度控制，不作已结算声明。上传或费用超出现有授权范围才补授权；范围内的执行/诊断不重复询问。

## Pilot and manual handoff

Pilot 记录 Creative Intent / Observable Pass Criteria / Failure Hypothesis、批准艺术规则、模型入口和适用边界。QC 提供实际视觉/声音结论，Generation 只保存输入、任务和文件证据。PILOT_VALIDATED 或用户明确的 USER_ACCEPTED_RISK 才放行对应范围；批准单个样片外观不自动接受全部未验证风险。

USER_HANDOFF 按已有路线交卡，尚未返回的 Unit 保持 NOT_SUBMITTED。回传文件须能对应 Unit/Take/版本，无法确定时保留未匹配记录，不猜测归属；用户未知的模型、seed、费用写 UNKNOWN。用户批准按确切范围记录 USER-APPROVED，QC Status 仍 NOT_EVALUATED；只有具体实际状态有依据才解锁依赖，不把单 Take 批准扩大成序列通过。
