# RUN｜Unknown Task Recovery

- **Case：** CASE-G02
- **Fixture：** `../fixtures/unknown-task-receipt.md`
- **Output：** `../outputs/unknown-task-resume.md`
- **Result：** PASS
- **Observed：** 观察超时保持 UNKNOWN，复用现有 task/idempotency ID 查询，没有重复提交。
- **Score：** 20/20
- **Hard Failure：** None

