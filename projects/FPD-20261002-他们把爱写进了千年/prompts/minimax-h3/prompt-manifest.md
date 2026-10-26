# MiniMax-H3 图生视频适配清单｜2026-10-02

> **G2 修订后内容已过期。** 原“无角色对白”的音频设定与 `../../screenplay/screenplay.fountain` v3 冲突；仅保留旧版技术调研记录，待 G3/G4 后重新编译。

**Package status：** CREATIVE INPUT RETURN / BLOCKED BY G3–G4。旧包先于 G2 v3 剧本、独立资产和正式分镜关口编写，须在上游通过后重新编译；当前账户提交能力和真实效果也未验证。用户本次只要求视频生成前工作，任何镜头均为 `NOT SUBMITTED`。最新关口见 `../../qc/workflow-gate-audit.md`。

## 1. Model Profile Receipt

| 项 | 当前记录 |
|---|---|
| Provider / Model | MiniMax / `MiniMax-H3`，视频生成 V2 接口 |
| Access date / sources | 2026-10-02；[官方 V2 创建任务文档](https://platform.minimax.cn/docs/api-reference/video-generation-v2-create)、[MiniMax 官方 H3 仓库](https://github.com/MiniMax-AI/MiniMax-H3)；本机 `mmx-cli video generate --help` 仅作入口交叉核对 |
| Profile status | VERIFIED（仅官方公开规格）；账户提交与真实画质 UNTESTED |
| Task / input mode | I2V 首帧：一个非空 text + 一张 `image_url` 且 `role=first_frame`；不与多模态参考输入混用 |
| Image limits | PNG 可用；单张 ≤30 MB，宽高各 256–5760 px，宽高比 0.4–2.5。八张 P0 均为 1080×1920、1.05–1.83 MB，符合文档范围 |
| Duration | H3 整数 4–15 秒；本片每镜目标约 3 秒，先计划生成 4 秒，再选稳定的约 3 秒用于后期 |
| Ratio | 图生视频由首帧决定，API 的 `ratio` 为 `adaptive`；八张首帧本身是 9:16。不把 `9:16` 作为图生视频强制生效参数 |
| Resolution | H3 支持 `768P` / `2K`；技术试镜采用 `768P`，后续规格待真实 QC 与预算决定 |
| Last frame / references | 本片每镜只用一张首帧。S02 等“落寞镜”是独立镜头，绝不可误作前镜的尾帧 |
| Audio | **STALE：** 旧“无角色对白”规划已被 G2 v3 四句短对白替代；对白/口型能力、后期配音方案须随新模型 Profile 和 Motion Spec 重新确定 |
| Text / negative | 官方创建任务 schema 未列独立负向提示词或可靠画面文字控制；风险排除压缩在主提示词末尾，正式字幕后期加入 |
| Async / result | 创建任务返回 `task_id`，后续查询结果；本阶段不创建任务 |
| Account / region | 本机 CLI 有已配置凭证，但套餐查询返回“no active token plan subscription”；这不能证明按量付费可用。fal 连接需重新登录。实际提交能力、余额和费用均为 UNKNOWN |

## 2. Source Version Lock

- `CURRENT`：`../../screenplay/screenplay-master.md`、`../../screenplay/screenplay-register.md`、`../../direction/shot-list.md`、`../../direction/shot-continuity-ledger.md`、`../../storyboard/frame-manifest.md`、`../../motion/motion-spec.md`、`../../visual-development/world-visual-bible.md`、`../../assets/asset-manifest.md`。
- 八张首帧是 2026-10-02 用户认可的当前 P0；目标文件逐镜列在 `prompt-package.md`。每镜一张 `FIRST FRAME`，由专用输入槽承担身份、构图、服装、场景和开始状态。
- `STALE` 触发：上述任何人物、动作、首帧或镜头时长发生实质修改。变化后先改对应源合同，再重新编译本包。

## 3. 参数与输入路由

| 字段 | 计划值 | 来源 | 注意 |
|---|---|---|---|
| `model` | `MiniMax-H3` | OFFICIAL_PROFILE / ADAPTER_CHOICE | 不与 Hailuo-2.3 的语法混用 |
| `content.text` | `prompt-package.md` 中对应镜头全文 | CURRENT_CREATIVE_SOURCE | 每次请求必须非空 |
| `content.image_url(role=first_frame)` | 该镜批准的 PNG | USER_APPROVED_ASSET | 本地文件如何交给入口，提交前核实；当前不上传 |
| `duration` | 4 | OFFICIAL_PROFILE / ADAPTER_DEFAULT | 后期只取稳定约 3 秒，模型内精确剪点不保证 |
| `resolution` | `768P` | OFFICIAL_PROFILE / ADAPTER_DEFAULT | 技术试镜先验证一致性 |
| `ratio` | `adaptive` | OFFICIAL_PROFILE | 图生视频按首帧比例，不能靠文本改画幅 |
| 费用 / 提交批次 | OPEN | ACCOUNT_UNKNOWN | 不执行任何付费任务 |

**上传顺序与槽位：** 每次只选择一个 Unit：① 对应 Sxx PNG 上传至官方 `first_frame` 槽；② 将该 Unit 的“直接复制｜主提示词”填入 text；③ 设模型、4 秒、768P、adaptive。逻辑 `@START_Sxx` 只是本文档别名，不要把本地路径或别名直接粘进模型文字。首帧允许影响画面 0 秒的全部可见状态；只允许按运动规格添加微动作，不允许重写人物身份、服装、空间或物件。

## 4. 十三项覆盖回执

以下映射逐一适用于 S01–S08；每镜独有的主体、动作、场景和风险在 `prompt-package.md` 对应卡片展开。状态只表示信息被编译或明确外移，不表示生成效果验证。

| 项 | 状态 | 来源 → 执行落点 |
|---|---|---|
| 1 参考锚定 | MAPPED | Frame Manifest → 每镜专用 first_frame 槽 |
| 2 叙事命题 | MAPPED | Brief / Screenplay → 每镜主任务与成对硬切关系 |
| 3 动态 | MAPPED | Motion Spec → 主提示词动作链 |
| 4 画面质感 | MAPPED | 已批准首帧 → first_frame；文字不重复重画 |
| 5 镜头语言 | MAPPED | Shot List → 各镜固定机位、无模型内转场 |
| 6 场景 | MAPPED | Visual Bible / 首帧 → first_frame |
| 7 色彩风格 | MAPPED | L-WARM-v1 / L-LONELY-v1 → 首帧，不在单镜内强行变色 |
| 8 光影 | MAPPED | Visual Bible → 保留既有灯/窗光，仅允许微动 |
| 9 构图层次 | MAPPED | 八张首帧 → 9:16 输入；深色留白保留 |
| 10 可观察表演 | MAPPED | Motion Spec → 指尖、侧目、步伐、托腮等逐镜动作 |
| 11 时间衔接 | MAPPED | Screenplay / Rhythm Map → 4 秒生成、约 3 秒选段；硬切在后期 |
| 12 声音 | MAPPED → POST | Screenplay / Rhythm Map → 后期音效和切点静默；不把模型音频当交付 |
| 13 连续性排除 | MAPPED | Continuity Ledger → 每镜主提示词末尾与生成后验收 |

**各 Unit 差异：** S01–S02 锁碑拓与李清照；S03–S04 锁书页与苏轼；S05–S06 锁石径、月洞门与陆游；S07–S08 锁饭桌、双碗与沈复。后镜中的缺席者不得重现。八镜均无未解决的创作冲突；模型对 4 秒、留白、人物稳定的实际表现须未来试镜验证。

## 5. Compatibility, reverse-check and order

- **Compatibility：** 现有 PNG 的格式、尺寸、比例、大小与官方输入约束匹配。4 秒最低生成时长与 3 秒镜头计划不一致，已明确降级为“4 秒输出中取约 3 秒”；若不足稳定时长，返回镜头节奏或换模型，不偷改剧本。
- **Reverse-check：** 每卡均能读出人物、首帧、一个主动作、固定机位、结束状态、主要物件和不可出现项；四次“人少了一个”的硬切只发生在两条独立视频之间。
- **TECHNICAL_PILOT 顺序：** 未来先 S07/S08，再 S01/S02、S03/S04、S05/S06。没有真实 Take 前，所有 PRODUCTION Unit 均不放行量产。
- **Decision register：** 用户认可八镜视觉；字幕逐字仍为执行提案；目标模型选 H3 作为当前首选技术路由，非最终质量承诺；账户、费用、真实效果和分辨率升级均待后续验证。
- **Next stage：** 保持 PLAN_ONLY。用户当前只授权生成前工作，G5 不通过，不提交任务。
