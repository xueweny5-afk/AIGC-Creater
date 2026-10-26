# DELIVERY SPEC

## PROJECT / SOURCE

- **Project ID：** TEST-EMOTION-OLD-MARKET
- **Picture Lock ID / Path / Checksum：** None；只有 POST PLAN，无真实 Picture Lock。
- **Mode：** PLAN_ONLY
- **Status：** DELIVERY PLAN

## SPEC SOURCE

- 用户型测试请求：归档横版、分发横版、条件式 9:16、中文字幕。
- 未指定真实平台；不使用任何平台当前限制、响度或编码参数。
- 在真实导出前，需要用户锁定交付规格或核实目标平台官方文档与访问日期。

## DELIVERABLES

| Deliverable ID | Purpose | Container / Codec | Resolution / Aspect | Frame Rate | Color | Audio | Subtitles | Naming | Verification |
|---|---|---|---|---|---|---|---|---|---|
| DEL-ARCH-169 | Archival / mezzanine | OPEN | source-preserving 16:9 | preserve Picture Lock | preserve managed source | stems/final mix OPEN | separate subtitle package | `<project>_master_arch_v###` | actual probe + checksum + full playback |
| DEL-DIST-169 | Distribution | OPEN pending target | 16:9, resolution OPEN | target/source compatible | target spec OPEN | target spec OPEN | separate + optional burned review | `<project>_dist_169_v###` | probe + playback + subtitle/audio review |
| DEL-SOC-916 | Social variant | OPEN pending platform | 9:16 only after shot review | target/source compatible | target spec OPEN | target spec OPEN | safe-zone reauthored | `<project>_social_916_v###` | per-shot reframe + full playback |
| DEL-REVIEW-SUB | Review copy | OPEN | follow selected review frame | preserve | review conversion OPEN | readable stereo target OPEN | burned Chinese review subtitles | `<project>_review_zh_v###` | subtitle/text/full playback |

## REFRAME PLAN

- 9:16 不是自动中心裁切。逐镜核对两摊关系、扫帚分界、小筐、半量夹子和人物画面左右。
- 若 S005 双人全景无法在 9:16 同时保留两人、分界与共享通道，则停止该变体，返回 Post-production 制作专门重构或补充镜头。
- 中文字幕需为 9:16 单独确定安全区，不能复用横版烧录位置。

## RIGHTS / CREDITS / TEXT

- 字体、音乐、声音、人物肖像、生成平台条款和演职员署名均无真实证据，保持 OPEN。
- No upload or publication authorized。

## NEXT STAGE

- **Primary Recommendation：** Return to Post-production
- **Reason：** 没有实际 PICTURE_LOCKED 文件、probe、checksum 或完整播放证据；本文件只是交付计划。

