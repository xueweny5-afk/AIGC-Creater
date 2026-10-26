# Post-production Contract

## States

- `POST PLAN`
- `ASSEMBLY PENDING REVIEW`
- `PICTURE LOCK CANDIDATE`
- `PICTURE_LOCKED`
- `RETURN`：Return Layer 记 QC / Generation / Creative / Post

这些状态在 Post Plan 与 Picture Lock Manifest 一致。未渲染保持 POST PLAN，已有组接待审用 ASSEMBLY PENDING REVIEW，候选用 PICTURE LOCK CANDIDATE；只有真实最终文件通过本阶段全部门才 PICTURE_LOCKED。旧报告保留原记录，不仅为统一标签改写历史证据。

## Picture-lock evidence

- exact render path
- exact render checksum / candidate version
- file exists/readable
- media probe summary
- timeline/project version
- source Take IDs and checksums
- render settings
- full playback pass 1/2 completion and dates
- Post Review result（PASS / REVISE / NOT_EVALUATED）/ tool / audio listened / reviewed range / pending checks
- open issue count by severity
- rights status
- decision authority / user acceptance if required

没有实际候选和完整声画审核证据不能 PICTURE_LOCKED。两项完整审核绑定同一最终文件版本/校验值；修复输出新候选后，最终文件须完成两项全片审核，不能沿用旧候选结果。已有源 Take 的 USER-APPROVED 不替代成片组合审阅，也不要求重做已批准源图 QC。

仅内容计划可交 POST PLAN、计划 EDL、声音/艺术/VFX 方案及待补素材/审核清单；不虚构文件、源时间码或播放。实际 EDIT/锁片需当前可追溯 QC-selected 或人工批准的素材及用途；计划完整不表示实际成片通过。

## EDL minimum

| Event | Scene / Shot | Selected Take | Source In / Out | Timeline In / Out | Video | Audio | Transition / Cut Motive | Notes |

时间单位保持一致，并说明帧率。剪辑软件项目不是唯一事实源；EDL/manifest 必须能独立追溯素材。

每 Event 另记 Source Take Version/Path、Source Frame Rate-Timebase、Audio Source/Offset、Speed Mapping、Crop-Stabilize-Reframe、Change Reason/Source Permission 与 Protected Intent/Review。源素材和时间线时间基分开，变速后的时间映射须闭合；实际引用不得超素材范围。附表按 Event ID 引用，不重复改写事实。计划值标 PLANNED，待补素材无实际入出点时写待确认。

## Sound layers

- Dialogue / sync
- Performance detail / breath
- Foley
- Environment / room tone
- Effects
- Music
- Silence

每层记录来源、授权、进入/退出、同步和混音状态。

声音职责包括注意引导、空间延续/断开、动作同步、关系/情绪与有意静默；按批准规则，不默认音乐铺满。真实音轨、计划音轨和无音轨/静默区分，不声称未听取的声音通过。

## Artistic inheritance and repair

记录 Viewing Stance / Information Alignment、Must Read/Withhold、Required Hold 与 Presentation Mode / Artistic Rule IDs-Version / Look-Light State / Approved Changes-HOLD。物理错误与非物理艺术层分开，匹配不抹掉批准曝光、色偏、绘画空间或时期差异；VFX 不更改身份、道具状态或世界承诺。

所有变速、裁切、稳定、调色、声音偏移和 VFX 变化记录 Event/Issue / Change-Reason / Source Permission / Protected Intent / Feasibility-Result / New Render / Verification Scope-Evidence / Closure。问题只在实际新版本复核后关闭，未解决 BLOCKER/MAJOR 返回原责任层，不以快切/音效掩盖。

