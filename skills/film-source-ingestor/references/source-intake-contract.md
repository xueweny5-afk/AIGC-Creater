# Source Intake Contract

## Status

- `COMPLETE`: 本轮范围已全部读取，关键元素和矛盾完成回链。
- `PARTIAL`: 仍有未读、无法解析或不在当前权限内的范围。
- `RETURN`: 文件、版本、授权或范围不足，无法可靠摄入。

## Evidence labels

- `SOURCE_EVENT`: 原作明确呈现的事件或状态。
- `NARRATOR_CLAIM`: 叙述者给出的说法，可能受视角限制。
- `CHARACTER_BELIEF`: 角色知道、相信或声称的内容。
- `DOCUMENTED_DIALOGUE`: 原作中实际存在、可定位的对白；只记录必要短引或摘要。
- `ANALYST_INTERPRETATION`: 对结构、母题、人物功能或含义的解释。
- `UNKNOWN`: 原作未说明、当前未读或版本之间无法判断。

这些标签描述原作证据，不等于外部事实的 `CONFIRMED`。

## Stable IDs

- Source: `SRC-TEXT-001`
- Segment: `SEG-001`
- Character: `SRC-CHR-001`
- Location: `SRC-LOC-001`
- Object: `SRC-OBJ-001`
- Event: `SRC-EVT-001`
- Rule: `SRC-RUL-001`

已有项目 ID 体系时可以映射，但不得在摄入阶段覆盖下游正式资产 ID。

## Coverage receipt

每个 Segment 记录：来源文件、版本、章节/页码/场次或段落范围、读取状态、解析限制、主要元素 ID、最后核对日期。顺序读取不要求每段同等详细，但任何省略必须可见。

## Adaptation boundary

- `SOURCE INVARIANT`: 用户明确要求保留，或项目身份依赖的原作内容。
- `ADAPTATION OPTION`: 可以讨论的压缩、合并、重排、视角或媒介转换候选。
- `OPEN`: 需要用户或 Project Direction 决定。
- `DO NOT ASSERT`: 原作没有支持、版本冲突或不能作为外部事实宣称的内容。

摄入报告只登记边界，不决定最终改编方案。
