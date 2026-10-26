# AIGC Creater Skill Audit｜GitHub Best Practices

## Review Scope

- `film-project-director`
- `film-researcher`
- `film-story-developer`
- `film-character-developer`

## Primary References

- OpenAI Skill Creator: https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md
- Agent Skills Specification: https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
- Agent Skills Best Practices: https://github.com/agentskills/agentskills/blob/main/docs/skill-creation/best-practices.mdx
- OpenAI Notion Research example: https://github.com/openai/skills/blob/main/skills/.curated/notion-research-documentation/SKILL.md
- ComfyUI reusable workflow model: https://github.com/Comfy-Org/ComfyUI

## Findings

### Already aligned

- 所有 Skill 使用清晰的 `name + description` 前置元数据，目录名一致。
- `SKILL.md` 均远低于 500 行，只保留核心工作流；schema、guide 与模板分别进入 `references/` 和 `assets/`。
- 引用文件均由 `SKILL.md` 直接链接，没有深层引用链。
- 没有无用 README、安装文档、空目录或未验证脚本。
- 每个阶段都有实际案例、硬失败条件和行为评测，不只依赖结构校验。
- Research 已区分证据、推断、争议与创作参考，符合来源可追溯和不夸大证据的做法。

### Gaps found

1. `Release Format / Series Architecture` 只存在于 Project Brief，下游没有强制消费。
2. 原型输出容易被措辞成“第一集”，把开放的发布结构偷偷锁定为剧集。
3. 人物连续性只描述跨段一致，没有区分原型专用、单元角色和跨集常驻。
4. Research 没有明确区分当前单元研究、共享世界底座和连续剧集研究债务。

## Changes Applied

- 优化四个 Skill 的 description，使触发范围包含单支、原型和剧集。
- Research 新增 `Research Scope Unit / Expansion Boundary`。
- Story 新增 `Blueprint Scope / Scope Promise / Carryover Boundary`。
- Character 新增 `Character Scope / Continuity Class / Accumulation Boundary`。
- Release Format 为 `OPEN` 时，统一降级为 `Prototype Unit` 和 `Prototype-only`，不得出现首集、季弧或跨集固定角色承诺。
- 更新模板、rubric、案例、UI 默认提示和现有《宗门志》产物。

## Deliberately Not Added

- 未增加数据库、JSON、版本注册中心或自动迁移脚本。
- 未把模型、平台或 GitHub 仓库写成强依赖。
- 未把 Treatment、视觉设计或 Prompt 规则提前塞进现有 Skill。
- 未复制第三方 Skill 的文字或提示词，只采用可迁移的接口与渐进披露原则。
