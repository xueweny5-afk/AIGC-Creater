# 《他们把爱，写进了千年》｜视频生成前工作流逐步核对

**范围与版本：** 2026-10-02；只核对 Stage 01–13，Stage 14 仅保留计划。用户已认可八张独立首帧、人物外观和前后硬切；未授权制作新视频。各阶段以本项目当前文件为证，不把早期 v1/v2 节奏预演当真实生成镜头。

| 步骤 | 本步解决的问题 | 当前成果 | 核对结论 |
|---|---|---|---|
| 01 项目定义 | 拍什么、给谁看、约束是什么 | `../project-brief.md` | 爱情单题、四组人物、24 秒八镜、温馨突切空位已明确；发布平台仍 OPEN，不影响前期方案 |
| 02 史料研究 | 哪些能当事实，哪些是影像重构 | `../research/research-pack.md`、`../research/source-index.md` | 四组文本线索及出处可追溯；唐氏本名、和词与相遇年份的争议已限定 |
| 03 故事结构 | 四组为什么按这个顺序出现 | `../story/story-blueprint.md` | 共做事 → 有人记得 → 错过 → 日常空位；结尾停在空碗 |
| 04 人物系统 | 谁在场、谁缺席、每人承担什么功能 | `../characters/character-system.md` | 八人及前后连续性清楚；唐氏表述与研究一致 |
| 05 Treatment | 让观众如何经历四次骤变 | `../treatment/contrast-treatment-v2.md` | 四段各 6 秒；具体动作已与现有静帧对齐 |
| 06 剧本 | 镜头里发生什么、文字哪些是原文 | `../screenplay/screenplay-master.md`、`../screenplay/screenplay-register.md` | 八镜时间闭合；引文、意译和创作文案分开登记；逐字字幕尚可微调 |
| 07 视觉世界 | 光色、地点、空气和时代边界 | `../visual-development/world-visual-bible.md` | 暖转冷、四个地点和清洁空气/少量花瓣已定义；只声称影像重构 |
| 08 资产 | 当前镜头依赖哪些人物、场景和道具 | `../assets/asset-manifest.md`、`../storyboard/frame-manifest.md` | S01–S08 的八张首帧为用户认可的 P0；新增角度或特写需另审 |
| 09 场面设计 | 每组从共同动作转到哪一种缺席 | `../direction/scene-design-pack.md` | 四组触发、反应和声音交接清楚 |
| 10 镜头设计 | 每镜唯一主任务和切点是什么 | `../direction/shot-list.md`、`../direction/shot-continuity-ledger.md` | MAIN/HOLD、时间、物件和风险明确；现有首帧不承诺严格动作匹配 |
| 11 静态分镜 | 不依赖视频，能否读懂四次变化 | `../storyboard/frame-manifest.md`、`../storyboard/sequence-contact-v1.jpg`、`../storyboard/sequence-review.md`、`../storyboard/animatic/rhythm-map.md` | 八张 1080×1920 首帧存在，用户已认可当前视觉；既有预演仅看节奏 |
| 12 运动规格 | 模型实际要让什么动、什么不能动 | `../motion/motion-spec.md` | 每镜一个主动作，锁定各自首帧；硬切由剪辑完成 |
| 13 提示词适配 | 把创作合同变成逐镜输入 | `../prompts/pre-video-prompt-package.md`、`../prompts/minimax-h3/prompt-manifest.md`、`../prompts/minimax-h3/prompt-package.md`、`../generation/production-unit-cards.md` | 八镜模型中立与 H3 适配包完成；官方规格已核，账户提交能力和真实效果仍待未来验证 |
| 14 生成计划 | 真正提交前如何试镜、验收、回退 | `../generation/generation-manifest.md` | PLAN_ONLY；首个未来技术试镜为 S07/S08。没有提交视频生成任务 |

## 逐步检查的结论

1. **G0–G2：** 项目范围、研究和创作主稿已形成；具体字幕仍是执行提案，不能把静帧认可推断为逐字批准。
2. **G3–G4：** 仅就当前八镜，用户认可的 P0 和静态分镜可作为后续技术试镜输入；历史服饰和面容不声称复原。
3. **G5：** 尚未进入。H3 公开输入规格已核，但账户提交能力与真实 Take 的 QC 没有验证；用户目前要求停止在生成前。

## 交接顺序

先读 `../project-brief.md` 和 `../research/research-pack.md`，再看 `../screenplay/screenplay-master.md` 与八镜联系表；确认画面后读 `../motion/motion-spec.md`、逐镜提示词和 Unit Cards。未来若启动视频制作，再从模型兼容性核验与 S07/S08 技术试镜开始，不越过当前的“无视频生成”边界。
