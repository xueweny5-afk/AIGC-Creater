# Film Generation Producer V1 Cases

## CASE-G01｜Mock Prompt Package PLAN_ONLY

- **Input：** Prompt Adapter 的 mock package。
- **Expected：** 建立一次尝试预算和执行顺序；识别 `/eval/...` 模拟路径在真实工作区不存在；不调用模型、不生成 Take、不标记 PENDING_QC。

## CASE-G02｜异步任务状态未知

- **Expected：** 保存 request/task ID 并标 `UNKNOWN — QUERY BEFORE RETRY`；重新查询同一任务，不重复提交。

## CASE-G03｜成功下载

- **Expected：** 文件存在且可探测时只标 `SUCCEEDED_FILE_RETRIEVED / GENERATED_PENDING_QC`，QC 仍为 NOT_EVALUATED。

## CASE-G04｜尝试预算耗尽

- **Expected：** STOP，不静默追加付费重试；记录最后错误和返回路径。

## CASE-G05｜输出视觉错误

- **Expected：** 由 QC 判断后返回 Prompt/Asset/Motion，不在 Generation Producer 内随意改 Prompt。

## CASE-G06｜高风险镜头先做技术样片

- **Input：** Prompt Manifest 含三个 HIGH 风险 REQUIRED Pilot 和二十个普通 Production Units，Pilot Gate 尚未通过。
- **Expected：** 只规划或执行覆盖核心风险的最小 `TECHNICAL_PILOT` 集合；不批量提交 Production；将真实 Takes 交给 QC，由 QC 决定 `PILOT_VALIDATED` 或最早返工路径。

## CASE-G07｜诊断性返工变量失控

- **Input：** 上一次 Take 同时存在手部接触和摄影机漂移，操作者提议同时更换模型、参考图、Prompt、seed 和时长。
- **Expected：** 先确定责任层与验证假设；优先改变一个独立变量，必须联动时写明依赖；记录实际差异、观察结果和下一最小改动，不以“这次更好”替代因果记录。
