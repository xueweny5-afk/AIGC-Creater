# SPECIALIST METHOD SKILL BLUEPRINT

> 仅在 Method Pack 达到 `VALIDATED_FOR_SCOPE` 后使用。创建时通过 `skill-creator` 转换为真实 Skill；删除不适用章节，不保留占位符。

## Required package

```text
skills/film-method-<slug>/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── method-contract.md
    ├── stage-overlays.md
    └── pilot-qc.md
```

只在确有复用价值时增加 prompt、asset 或 post 模块；不复制母 Skill 的通用说明。

## SKILL.md content contract

- YAML name / discriminating description;
- Method ID, version, status and evidence boundary;
- use / do-not-use routing;
- required project contracts and Adoption Receipt;
- concise workflow applying approved stage overlays;
- pilot requirement and specialist QC;
- return routes and review triggers;
- precedence: user/project contracts over Method;
- no raw reference media or work-specific expression.

## UI metadata

`allow_implicit_invocation: true`，同时提供包含 `$film-method-<slug>` 的短 default prompt。描述必须能区分相邻 Method，避免用“专业视频”“高级风格”等宽泛措辞。

## Promotion receipt

记录 Study IDs、Method Pack 版本、Pilot Take/QC、Validated For、Not Validated For、Known Failures 和 Last Verified。专项 Skill 不得声称超出这些范围。
