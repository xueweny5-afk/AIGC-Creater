# Film Prompt Adapter V1 Rubric

每项 0–2 分，总分 24 分；22 分及以上通过。

1. Model Profile Verification
2. Source Version Lock
3. Real Input Path Mapping
4. Creative Fidelity
5. Prompt Compactness
6. Start / Trigger / Action / End Coverage
7. Parameter Provenance
8. Compatibility & Fallback
9. Reverse-check
10. No Generation Claim
11. Thirteen-item Coverage Receipt
12. Observable Performance & Look-state Preservation

## Hard failures

- 编造当前模型能力、参数或费用；
- 使用不存在或未批准的参考文件；
- 为适配模型改变故事、镜头、身份或结束状态；
- 把不支持字段写进 Prompt 后宣称会生效；
- 调用生成或声称结果成功。
- 十三项回执存在 Conflict/Return 仍标 READY，或把回执机械拼成冗长 Prompt；
- 用自然语言伪装目标模型不支持的声音、负向提示、参考或控制能力。
