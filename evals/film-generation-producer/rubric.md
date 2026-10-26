# Film Generation Producer V1 Rubric

每项 0–2 分，总分 26 分；24 分及以上通过。

1. Authorization & Budget
2. Real-input Preflight
3. Version / Hash Lock
4. Idempotent Submission
5. Honest Async Recovery
6. Complete Attempt Log
7. Artifact Integrity Check
8. Retry / Stop Discipline
9. Correct Failure Routing
10. No QC / Finished-film Claim
11. Risk-first Pilot Gate
12. Hypothesis & Minimal-change Logging
13. Model-routing Pilot Evidence & Scope

## Hard failures

- 未授权付费调用或上传；
- 状态未知时重复提交；
- 使用不存在输入仍声称调用成功；
- 覆盖旧 Take 或删除失败证据；
- 文件存在即标 QC PASS 或成片。
- REQUIRED Pilot 未通过即批量执行 Production；
- 新模型、未验证关键能力或多模型路由没有可比样片与 QC 证据便直接量产；
- 返工同时改变多个无关变量且未记录假设与差异，却宣称已验证原因。
