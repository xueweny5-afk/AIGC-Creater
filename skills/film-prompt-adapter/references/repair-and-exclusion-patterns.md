# Repair and Exclusion Patterns

排除项用于保护已批准事实，返工 Prompt 用于改变可见失败。它们都不是越长越好。

## Exclusion priority

按当前 Unit 风险选择：

1. **Identity / count：** 年龄、脸、体态、人物数量、额外肢体或主体。
2. **State / continuity：** 服装版本、持物手、道具开合/损坏、人物方向、动作阶段。
3. **Space / camera：** 轴线、拓扑、景别、机位、固定镜头漂移。
4. **World / rights：** 错误时代元素、品牌、Logo、水印、字幕和未授权形象。
5. **Material / rendering：** 塑料皮肤、均匀磨损、无来源反光、鱼鳞状纹理、过锐化或 CG 表面。
6. **Performance：** 偶像剧式夸张、无动机笑/哭、重复动作、随机眨眼喘息。

平台不支持独立 negative prompt 时，把最关键限制改写为简短的正向锁定和末尾 exclusions，并在 Coverage Receipt 标明能力边界。

优先使用“正向锁定 + 镜像排除”：先说明需要的年龄、方向、动作阶段、表演强度和摄影机状态，再只排除最可能破坏这些目标的相反结果。教程中“年轻状态 ↔ 不要老年皱纹”“固定机位 ↔ 不推拉摇移/漂浮”“克制微笑 ↔ 不大笑/不偶像剧式表演”属于有效结构。若负向词没有对应的正向合同，应先检查它是否真的需要。

## Surgical repair

先从真实结果写 `Observed failure`，再使用：

```text
CHANGE
- 只改变可见失败及必要关联字段。

PRESERVE
- 列出已通过的身份、构图、光线、服装、空间和动作状态。

CONSTRAINTS
- 防止修复引入新的主体、状态、文字、机位或风格变化。
```

示例：

```text
CHANGE：把人物右手从杯子后方移到杯柄上，五指形成可见且物理合理的握持。
PRESERVE：人物脸、年龄、坐姿、左手位置、服装、杯子尺寸、桌面构图和窗侧光完全不变。
CONSTRAINTS：不改变持物手，不增加手指、首饰、文字或新的桌面物件；不重新生成背景。
```

## Failure ownership

- Prompt 漏掉批准字段或表达歧义 → Prompt Revision。
- Prompt 正确但模型反复忽略 → Model/Profile/Pilot 或换路由。
- 身份、空间、动作或终点在上游本身矛盾 → 返回 Asset/Shot/Motion，不能靠负向词解决。
- 只有结果风格不喜欢但没有批准标准 → 先返回 Visual Decision，不无限抽卡。

每轮返工优先只改变一个独立变量，并保存 Prompt、参数和实际变化；“增加更多细节词”不是失败诊断。
