# Qita Workflow Learning Optimization Audit

**Date:** 2026-09-23  
**Scope:** `AIGC Creater` 全流程的小步优化  
**Reference material:** `D:\project\qita` 中的流程视频、参考成片与《祸女》案例知识库

## Outcome

保留原有 17 阶段和职责边界，不新增强制 Skill。将学习到的有效方法落为两条跨阶段机制：

1. `Creative Reference Evidence Chain`：作品证据 → 作用解释 → 可迁移机制 → 本项目验证假设 → 不可复制项。
2. `Risk-first Production Gate`：静态分镜通过 → 最小技术样片 → 真实媒体 QC → 批量生产 → 跨镜审核。

## Changes

- Pipeline 从 V1.0 更新到 V1.1，增加 G0–G8 Gate、资产优先、静态优先、样片优先和基于证据的迭代原则。
- Film Researcher 不再只写“可迁移品质”，而是区分作品中实际可见内容、研究者解释、迁移机制与待验证假设。
- Shot Director 为每镜增加风险等级、风险类型、风险假设和 Pilot Priority，并要求一个 Clip 只有一个主要叙事任务和主要动作。
- Prompt Adapter 原样传递风险和 Pilot 顺序，不因模型适配改写导演判断。
- Generation Producer 区分 `TECHNICAL_PILOT / PRODUCTION`；Required Pilot 未通过时禁止批量生成；返工记录验证假设、实际变化和下一最小改动。
- Continuity QC 用真实 Take 解决 Pilot Gate，只验证被测试的风险，不把样片通过扩大成全片通过。

## Preserved boundaries

- 人物三视图、服装、场景和道具仍在 Asset Design，不前移到项目构思阶段。
- 图片 Prompt 与视频 Prompt 仍在 Prompt Adapter 编译；故事、剧本和导演主合同保持模型无关。
- 静态分镜不能替代 Motion Spec；生成成功不能替代 QC；声音和后期不能掩盖身份、空间、动作或因果错误。
- 参考作品不作为历史、现实或科学证据，不复制独特人物、情节链、体系、对白和可识别表达。

## Verification

- `quick_validate.py`：Film Researcher、Shot Director、Prompt Adapter、Generation Producer、Continuity QC 全部通过。
- Markdown table structure：Shot List、Prompt Manifest、Generation Manifest、QC Report 模板全部通过列结构检查。
- Trace check：`Risk Hypothesis / Pilot Priority` 已从 Shot List 贯通到 Prompt、Generation 和 QC。
- Evaluation coverage：Generation 新增高风险样片与最小变量返工案例；Research 新增证据、解释和验证假设分离要求。

## Next real-project test

选择一个 30–90 秒短片，先锁定剧本、P0 资产和静态分镜，再选择 2–4 个能覆盖人物身份、空间、关键动作与特殊效果的 Pilot Shots。只有 Pilot QC 返回 `PILOT_VALIDATED` 后才生成普通镜头。记录实际耗时、返工次数、费用、失败责任层和最终节省的无效生成量，用这些证据决定下一次最小修订。
