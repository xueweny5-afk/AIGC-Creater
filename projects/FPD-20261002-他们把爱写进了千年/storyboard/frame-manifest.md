# Frame Manifest｜v4｜Stage 11 八张关键帧已入库

**2026-10-12 当前版：** SH01–08 八张 `key-v2.png` 全部存在，用户明确认可其画面方向；SH07 已依实际图修订剧本为沈给陈夹菜。下文旧 `start-v1`、六张初审及 `NOT_RECEIVED/REPAIR` 标签均为历史过程，**不代表当前状态**。当前逐镜视觉评价见 `sequence-review.md`，门状态见 `../qc/g4-static-review-2026-10-12.md`。

| SH | 当前用户认可静帧 | 时间变化 / 空位 |
|---|---|---|
| 01 | `frames/F01-li-zhao/S01-key-v2.png` | 李赵共处书案 |
| 02 | `frames/F01-li-zhao/S02-key-v2.png` | 年长李与赵右空位 |
| 03 | `frames/F02-su-wang/S03-key-v2.png` | 苏王共读 |
| 04 | `frames/F02-su-wang/S04-key-v2.png` | 年长苏与王右空椅 |
| 05 | `frames/F03-lu-tang/S05-key-v2.png` | 陆唐园路共处 |
| 06 | `frames/F03-lu-tang/S06-key-v2.png` | 年长陆独自持信 |
| 07 | `frames/F04-shen-chen/S07-key-v2.png` | 沈给陈右碗递菜，陈回应 |
| 08 | `frames/F04-shen-chen/S08-key-v2.png` | 年长沈对陈右空碗停筷 |

八张无字幕的 1080×1920 首帧目前仅作已认可的**画面方向参考**；画面中部为横向叙事区，上下深色留白供最终版式使用。G2 通过的剧本 v3 新增按纸、指页、回身、夹菜及后场无人回应的动作链，旧帧的动作状态已过期，须在 Stage 11 按正式镜头与资产重编；当前不能直接作为图生视频输入。四张 `v1.png` 为最初的双画面探索图。

| 镜头 | 首帧（相对此文件） | 画面 | 状态 |
|---|---|---|---|
| S01 | `frames/F01-li-zhao/S01-start-v1.png` | 李赵共看碑拓 | VISUAL DIRECTION APPROVED · G4 PENDING |
| S02 | `frames/F01-li-zhao/S02-start-v1.png` | 李清照与空席 | VISUAL DIRECTION APPROVED · G4 PENDING |
| S03 | `frames/F02-su-wang/S03-start-v1.png` | 苏王共读 | VISUAL DIRECTION APPROVED · G4 PENDING |
| S04 | `frames/F02-su-wang/S04-start-v1.png` | 苏轼与空椅 | VISUAL DIRECTION APPROVED · G4 PENDING |
| S05 | `frames/F03-lu-tang/S05-start-v1.png` | 陆游与唐氏同行 | VISUAL DIRECTION APPROVED · G4 PENDING |
| S06 | `frames/F03-lu-tang/S06-start-v1.png` | 陆游独对园路 | VISUAL DIRECTION APPROVED · G4 PENDING |
| S07 | `frames/F04-shen-chen/S07-start-v1.png` | 沈陈共食 | VISUAL DIRECTION APPROVED · G4 PENDING |
| S08 | `frames/F04-shen-chen/S08-start-v1.png` | 沈复与空碗 | VISUAL DIRECTION APPROVED · G4 PENDING |

全序列联系表：`sequence-contact-v1.jpg`。对应的动作、切点和连续性要求分别见 `../motion/motion-spec.md`、`../direction/shot-list.md`、`../direction/shot-continuity-ledger.md`。

**审查结论：** 用户于 2026-10-02 回复“可以的”，认可当前八镜的画面方向与人物外观。这是分镜视觉反馈，不代替 Stage 08 独立资产审批，也不代表 G3/G4 已通过。正式分镜状态需在上游合同完成后复核；见 `../qc/workflow-gate-audit.md`。

## G2 v3 / Shot List v3 的新帧交接

> **2026-10-12 最新覆盖：** SH01–08 八张 `key-v2.png` 已全部入库并获用户画面认可；下方六张/缺两张的旧记录仅保留当时复核历史。当前门状态与逐镜差异以 `../qc/g4-static-review-2026-10-12.md` 为准：SH07 动作方向与剧本相反，G4 尚待闭合该故事决定。不要按下方旧 `NOT_RECEIVED` 标签判断文件是否存在。

> **2026-10-12 实图复核：** 已收到 SH01–06 六张 `key-v2`；SH07–08 尚未收到。六张均保留原文件，以下状态替代原先 `NOT_RECEIVED` 计划状态。后镜年龄状态照已入库，见 `../qc/later-age-state-review-2026-10-12.md`。具体修复交接见 `frame-repair-handoff-2026-10-12.md`。

构图合同见 `composition-guides-v3.md`；逐镜参考图角色、可复制主/负面提示词和回收核对见 `frame-handoff-v3.md`。旧八张 `start-v1` 仅供画幅方向参考，不能冒充以下动作关键帧，也不能当人物身份参考。生成顺序为每组先双人、审过后再用它作后镜构图底图。

| 镜头 | 新动作关键帧目标（相对此文件） | 决定性瞬间 | 当前状态 |
|---|---|---|---|
| SH01 | `frames/F01-li-zhao/S01-key-v2.png` | 李右手按纸，赵左手接同角 | RECEIVED / REPAIR：赵的手未到右上卷角，纸角不明显 |
| SH02 | `frames/F01-li-zhao/S02-key-v2.png` | 李独按同角，右侧赵位空 | RECEIVED / REPAIR：李仍是年轻脸，右手也未按右上角；空间匹配可保留 |
| SH03 | `frames/F02-su-wang/S03-key-v2.png` | 王左手指右页，苏回应 | RECEIVED / PROVISIONAL：指页与左右位清楚，作为 SH04 构图底图 |
| SH04 | `frames/F02-su-wang/S04-key-v2.png` | 苏右手指同列，王右椅空 | RECEIVED / REPAIR：机位景别与 SH03 明显不同，苏仍年轻；须从 SH03 重做后镜 |
| SH05 | `frames/F03-lu-tang/S05-key-v2.png` | 陆右手伸向唐，未接触 | RECEIVED / PROVISIONAL：动作与左右关系可读，作为 SH06 构图底图 |
| SH06 | `frames/F03-lu-tang/S06-key-v2.png` | 陆右手伸向空处，左手持折信 | RECEIVED / REPAIR：年长状态和手信方向可用，景别/叙事区边界与 SH05 不匹配 |
| SH07 | `frames/F04-shen-chen/S07-key-v2.png` | 陈送菜入沈左碗，两双筷 | NOT_RECEIVED |
| SH08 | `frames/F04-shen-chen/S08-key-v2.png` | 沈筷停在陈右空碗前 | NOT_RECEIVED / SH07 DEPENDENCY |

**Gate：** 八张实图、必要的动作终点帧、顺序审阅与节奏图仍待核对；G4 `PENDING`。
