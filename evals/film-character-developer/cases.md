# Film Character Developer Evaluation Cases

## Case 1｜修仙宗门与代价公开

- **Input：** 《山门内外》Story Blueprint，四个人物功能，结局行动保持 OPEN。
- **Expected：** 精简人物数量；正道维护者和越禁救助者都有合理逻辑；受影响者拥有独立选择权；不锁死结局；不复制参考小说人物。

## Case 2｜八王之乱真实人物

- **Input：** 历史瞬间蓝图，涉及有史料记录的真实人物，但心理资料不足。
- **Expected：** 使用 `EVIDENCE_LIMITED`；区分可核实行为与创作推断；心理字段可保持 `UNKNOWN`；不虚构内心、私密对白或关键行为；必要时返回 Research Return。

## Case 3｜老菜市场观察短片

- **Input：** Observational 蓝图，没有传统英雄主角。
- **Expected：** 使用 `OBSERVATIONAL`；可使用观察主体或小型共同体；以日常选择和拒绝边界表达 agency；不强造创伤、反派和成长弧；保留人物尊严与独立生活。

## Case 4｜最后一名气象观测员

- **Input：** 科幻蓝图，科学规则已研究，但世界结局开放。
- **Expected：** 分开科学条件、角色知识和角色信念；人物选择不由技术说明自动推出；不锁死世界结局。

## Case 5｜角色功能过多

- **Input：** Story Blueprint 有七个功能，但短片只允许少量稳定角色。
- **Expected：** 通过 KEEP / MERGE / COMMUNITY / REMOVE 收敛；说明因果与制作影响，不为每个功能强建人物。

## Case 6｜故事蓝图尚未成立

- **Input：** 主角位置与核心冲突互相矛盾，人物无法产生既定 Story Movement。
- **Expected：** 返回 Story Blueprint Revision，指出最小阻塞项，不用人物小传掩盖结构问题。

## Case 7｜原型人物不得自动常驻

- **Input：** Blueprint Scope 为 `Prototype Unit`，Release Format 为 `OPEN`，但人物具有明显复用潜力。
- **Expected：** Continuity Class 使用 `Prototype-only` 或 `OPEN`；不因 AIGC 资产复用方便就设为固定主角或常驻角色；跨集状态保持未定义。
