# Method Promotion Contract

## Method identity

Method 表示可跨内容复用的制作机制。分类开放，不使用固定类型枚举。命名优先描述动作或因果，例如“局部分层运动”“延迟反应喜剧”，避免只写“高级感”“某某风格”。

稳定 ID 使用 `MTH-<short-slug>`；Study 使用 `MST-YYYYMMDD-<short-slug>`。专项 Skill 使用 `film-method-<slug>`，名称小写、短横线、少于 64 字符。

## Compare and route

- 核心机制、受控字段、前提和 QC 相同 → 更新已有 Method。
- 共享核心但执行或适用条件不同 → 同一 Method 的可选模块。
- 一个项目需要多个独立机制 → 组合多个 Method ID。
- 核心因果、输入或验收不同 → 新 Method。
- 新证据反驳旧结论 → 缩小范围或 `REVIEW_REQUIRED`，不覆盖历史。

## Promotion states

- `STUDY_ONLY`: 只有案例观察。
- `CANDIDATE`: 已形成可迁移规则，但无完整验证。
- `PILOT_READY`: 风险假设、输入、执行和 QC 已可测试。
- `VALIDATED_FOR_SCOPE`: 代表性真实 Pilot 与 QC 支持限定范围。
- `REVIEW_REQUIRED`: 模型、入口、资产结构或相反证据需要复核。
- `RETIRED`: 已失效，不再默认推荐。

## Minimum for specialist Skill

必须同时满足：

1. Study 覆盖完整，或缺口不影响拟提升机制；
2. 用户看重的结果与系统推断分开并得到确认；
3. 作品独有内容和不可复制项已经剥离；
4. Method Pack 定义适用、不适用、控制字段、阶段覆盖、风险和专项 QC；
5. 至少一个代表性真实 Pilot 使用确切 Prompt、模型、参数和输入；
6. Continuity QC 完整播放，并对 Method 假设给出可见证据；
7. 没有未解释的 BLOCKER/MAJOR 副作用；
8. 已验证模型、入口、镜头类型和未验证范围明确。

通过后只标 `VALIDATED_FOR_SCOPE`。单项目验证允许跨项目作为候选复用，但新项目仍需根据新模型、资产结构和风险执行最小 Pilot。

## Specialist Skill contents

- precise discovery description and use/non-use cases;
- Method ID/version/status/evidence index;
- creative invariants and variable project fields;
- stage overlays and controlled fields;
- assets, references, shot, motion, sound and prompt modules when applicable;
- pilot hypotheses and model-independent QC;
- model-specific evidence only where verified;
- common failures, return routes and review triggers;
- no raw reference media or copied work-specific expression.

## Review and retirement

创作机制和模型执行证据分别版本化。模型升级只使相关执行模块 `REVIEW_REQUIRED`，不自动废弃叙事或视觉机制。新案例可以扩展、缩小、拆分或合并 Method；每次保留旧版本和变更理由。
