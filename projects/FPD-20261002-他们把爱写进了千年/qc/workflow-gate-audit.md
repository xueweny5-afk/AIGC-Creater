# 按项目流程复核｜2026-10-02

依据：仓库 `pipeline/film-production-pipeline.md` V1.9 的 Stage 01–14 与 G0–G5。用户本项目的范围是**视频生成前**，不得提交视频生成任务。此表纠正此前把静帧认可直接写成资产与分镜全关口通过的状态。

| Gate / 阶段 | 当前证据 | 严格结论 | 下一步 |
|---|---|---|---|
| G0 / Stage 01 项目定义 | `../project-brief.md` | 已有明确主题、四组人物、前后硬切及边界 | 保留 |
| G1 / Stage 02 研究 | `../research/research-pack.md`、`../research/source-index.md` | 可追溯；唐氏姓名与和词争议已标 | 保留 |
| Stage 03 故事蓝图 | `../story/story-blueprint.md` v2 | 已按 Story Blueprint 模板补全范围、事实/创作边界、人物功能及决策 | 已自审 |
| Stage 04 人物系统 | `../characters/character-system.md` v2 | 已登记八位真实人物的证据限制、关系与知识边界 | 已自审 |
| Stage 05 Treatment | `../treatment/treatment.md` v2 | 已加入短对白与动作回应的叙事原则；旧 `contrast-treatment-v2.md` 保留为早期场面探索 | READY / 修订后自审 |
| Stage 06 剧本 | `../screenplay/screenplay.fountain`、`../screenplay/screenplay-register.md` v3 | 八场 Fountain 主剧本新增每组一句短对白，后场以同动作无人回应；旧 `screenplay-master.md` 为过期执行摘要 | COMPLETE / 修订后自审 |
| G2 创作主版本 | Stage 03–06 | **2026-10-03 通过**。用户确认含短对白、互动与独处转场的 v3 剧本 | 进入 Stage 07；后续修改须回写主版本 |
| Stage 07 视觉世界 | `../visual-development/world-visual-bible.md` v3、`../visual-development/asset-requirements.md`、`../visual-development/reference-analysis.md` | 已按模板补全视觉主合同、八个 Look/Light 状态、参考语义与资产需求；READY FOR ASSET DESIGN | 进入 Stage 08 |
| Stage 08 视觉资产 | `../assets/asset-manifest.md` v3、24 项资产合同、`../assets/prompts/all-asset-prompts-v1.md` | USER_GENERATE / 全部独立资产生图词已合订；人物与场景多角度一致性列为核心验收；八张旧图仅是**分镜视觉方向**，独立 P0 原图仍未生成、未审核 | 等待首轮八张正脸与四张无人空间主视图，逐张像素审核后派生角度 |
| G3 视觉资产 | Stage 07–08 | **未通过**；先前写作 APPROVED P0 的说法过度 | 完成并审核本片实际需要的 P0 |
| Stage 09–12 场面、镜头、静态分镜、运动 | `../direction/scene-design-pack.md` v3；旧 Shot/Storyboard/Motion 与八张首帧 | Stage 09 已按 G2 v3 补成 DRAFT_ASSET_PENDING；旧镜头、静帧动作与运动为 STALE，画面方向保留；正式放行依赖 G3 | 先审资产，之后只重编受影响字段 |
| G4 静态分镜 | Stage 09–11 | **待上游**；用户认可画面不等于流程门通过 | G3 后复核 |
| Stage 13 提示词 | 旧模型中立、H3 与八镜总稿 | 均为旧无对白剧本的 **STALE / BLOCKED BY G3–G4**，不能称可执行包；Stage 08 独立资产提示词已按新版剧情交接 | 资产和正式 Shot/Storyboard/Motion 通过后重编 |
| Stage 14 生成 | `../generation/generation-manifest.md` | PLAN_ONLY；无真实 Take | 本次范围止于生成前 |

**执行顺序：** Stage 03–06 的 v3 剧本已过 G2；进入 07、08 和 G3。其后才复核 09–12 并正式编译 13。未经对应 Gate，不因文件已经存在就越级标记通过。
