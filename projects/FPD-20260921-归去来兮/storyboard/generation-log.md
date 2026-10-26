# STORYBOARD GENERATION LOG

## PROJECT

- **Project ID：** FPD-20260921-归去来兮
- **Generation Policy：** CONFIRM PER BATCH
- **Current Batch Mode：** USER_GENERATE
- **Review States：** PASS / REWORK / REJECT
- **Approval Rule：** SELF-REVIEWED 不等于 USER-APPROVED

## RECORDS

| Record ID | Date | Frame ID | Action | Result | Evidence / Note |
|---|---|---|---|---|---|
| GEN-SB001 | 2026-09-24 | S001-SH01-F01 | CREATE NEW | PASS — SELF-REVIEWED | 人物、官服、官署与秋风信息可读；纸面文字仅作功能纹理。 |
| GEN-SB002 | 2026-09-24 | S001-SH02-F01 | CREATE NEW | PASS — SELF-REVIEWED WITH CAVEAT | 官牒平放、双手松开；生成笔迹不可作为准确文字展示。 |
| GEN-SB003 | 2026-09-24 | S001-SH03-F01 | CREATE NEW | PASS — SELF-REVIEWED | 单一官印、四手边界和交接前间距成立；指定为 F02 编辑母图。 |
| GEN-SB004 | 2026-09-24 | S001-SH04-F01 | CREATE NEW → REWORK | REJECTED INITIAL | 初版误保留官冠和红色官袍，不符合离任后的服装状态，未归档为正式帧。 |
| GEN-SB005 | 2026-09-24 | S001-SH04-F01 | CREATE NEW — CORRECTED | PASS — SELF-REVIEWED | 修正版为灰褐离任状态，张翰向右离开、属吏在左侧持印。 |
| GEN-SB006 | 2026-09-24 | S001-SH03-F02 | EDIT FROM S001-SH03-F01 | NO OUTPUT | 自动精确编辑超时终止，无文件归档。 |
| GEN-SB007 | 2026-09-24 | Batch 01 remainder | MODE DECISION | USER_GENERATE | 后续提示词先交付用户，由用户统一生成；项目负责回传核查、返工意见和归档。 |
| GEN-SB008 | 2026-09-24 | Future batches | POLICY UPDATE | CONFIRM PER BATCH | 保留 AUTO_GENERATE；每个新批次展示提示词后重新由用户选择，Batch 01 当前选择不自动继承。 |
| GEN-SB009 | 2026-09-25 | S001-SH03-F02 | USER GENERATION — CANDIDATE 1 | REWORK | 官印已经完全转移到属吏手中，张翰撤手；画面更接近 F03，未作为 F02 归档。 |
| GEN-SB010 | 2026-09-25 | S001-SH03-F02 | USER GENERATION — CORRECTED | PASS — CODEX VISUAL REVIEW | 单一官印由双方共同承重，手部、身份、机位与光线连续；已归档并指定为 F03 编辑母图。 |
| GEN-SB011 | 2026-09-25 | S001-SH03-F03 | USER GENERATION | PASS — CODEX VISUAL REVIEW | 属吏独立双手持印，张翰完全撤手但尚未离场；交接结束状态成立并已归档。 |

## ACTIVE HANDOFF

- **Prompt Pack：** `storyboard/prompts/storyboard-batch-01-zhang-han.md`
- **User Generation Order：** S002-SH01-F01 → S002-SH02-F01 → S002-SH03-F01
- **Return Naming：** 文件名必须使用完整 Frame ID；若平台自动改名，上传时必须明确原文件对应哪个 Frame ID。
