# Method Workflow Integration Contract

## Precedence

```text
Current user instruction
> approved project contracts
> adopted Method overlays
> public pipeline defaults
> general model patterns
```

Method 只控制 Adoption Receipt 授权的字段。未列字段继续由原阶段决定；与项目事实或批准内容冲突时 Method 退让或返回用户决定。

## Adoption

项目只有在 `method-adoption.md` 锁定 Method ID、版本、范围和冲突规则后，才加载专项 Skill。可以不采用、全片采用、按段落/镜头采用或只采用单个模块。多个 Method 按 `PRIMARY / SECONDARY` 排序，但优先级不能代替字段级冲突裁决。

## Stage overlays

| Stage group | Method may contribute | Must not replace |
|---|---|---|
| Brief / Research | expected audience effect, method fit, research/rights questions | user intent, verified facts |
| Story / Character / Treatment / Screenplay | bounded information, reaction, reversal or rhythm mechanisms | premise, agency, causality, ending, factual truth |
| Visual / Asset | transformation rules, protected style identity, asset preparation, failure risks | approved identity, historical evidence, asset versions |
| Scene / Shot / Storyboard / Motion | shot role, MAIN/SUPPORT/HOLD, timing, trigger, movement and sound overlays | scene purpose, axis, continuity, approved states |
| Prompt / Generation | method prompt modules, exclusions, pilot hypotheses | model profile, source contracts, permissions |
| QC / Post / Delivery | method-specific acceptance, edit/sound/platform overlays | continuity gates, picture lock and delivery verification |

影响 Story 或 Screenplay 的方法必须在对应上游解决，不能在 Prompt 中补写。只影响执行表达的方法可以从 Visual、Shot、Motion 或 Prompt 接入，但必须说明采用起点。

## Conflict handling

每项冲突记录：`Field / Competing Method IDs / Project Contract / Decision / Owner / Affected Stages`。无法字段级裁决时标 `RETURN`，不让多个专项 Skill 同时控制同一内容。

Method 版本变化按 `CURRENT / STALE / BLOCKED / RECOMPILE` 传播：机制或受控字段变化为 `STALE`；只有表达或模板更新且事实等价时为 `RECOMPILE`；缺批准或证据为 `BLOCKED`。

## Pilot and QC

每个采用项目列出仍未验证的 Method 风险。已有专项 Skill 不能自动取消 Pilot；只有当前模型、入口、输入结构和镜头风险均落在证据范围内时才可标 `NOT_REQUIRED`。

QC 同时检查：

1. 公共故事、身份、空间、物理、连续性和可剪辑性；
2. Method Core Mechanism 是否可见；
3. Method 的 MAIN/HOLD、节奏、声音、转换和典型失败；
4. 结果是否只“好看”但没有实现目标体验；
5. 方法通过范围和未覆盖范围。

通用 QC 或 Method QC 任一失败，都不能进入正式后期。

## Feedback split

- 跨阶段创作、镜头、运动、声音和类型 QC 证据 → `film-video-method-curator`。
- 特定模型、参数、参考职责、Prompt 改动与 Take 对照 → `film-generation-pattern-curator`。

同一案例可以提供两类证据，但不得在两个目录复制原始媒体。
