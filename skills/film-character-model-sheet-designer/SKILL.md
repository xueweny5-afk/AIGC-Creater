---
name: film-character-model-sheet-designer
description: 为 AIGC 电影设计同一角色的多视图身份设定板、正交全身视图、头部角度与真实皮肤参考提示词，并审查跨视图的脸、体态、发型、肤色和服装连续性。用于角色四视图/六视图、turnaround、character model sheet、角色建模参考或已有设定板返工；不负责人物故事塑造、镜头画面、视频提示词或未经审核的资产批准。
---

# Film Character Model Sheet Designer

把角色设定板当作“身份与结构标定资产”，不是一张好看的人像海报。首要目标是不同角度仍能明确判断为同一个人，其次才是皮肤细节与摄影质感。

## Required inputs

尽量读取或取得：

1. APPROVED Canon Face / Canon Body 或明确标为候选的角色描述；
2. Character Asset Contract 中的 `locked_features / variable_states / unknowns`；
3. 年龄范围、头面比例、体态比例、发型、稳定身份标记和左右不对称；
4. 服装与妆发合同，若本次设定板包含它们；
5. 设定板用途、所需视图、目标画幅和用户指定的生成平台。

没有批准身份锚点时仍可创作 `IDENTITY CANDIDATE`，但不能称为连续性母版。职业、性格、善恶或社会角色不能用来猜测族群、脸型、肤色、体型或“典型长相”。

## Load resource

编写、改写或审查多视图提示词时读取 [model-sheet-craft.md](references/model-sheet-craft.md)。其中包含视图协议、身份锁定层级、皮肤真实性、提示词骨架、返工写法和验收标准。

## Modes

- `DESIGN`：选择必要视图，建立模型中立的设定板规格与提示词包。
- `REVIEW`：实际查看已有设定板或独立视图，逐项检查身份与结构漂移。
- `REPAIR`：使用 `Change / Preserve / Constraints` 只修失败字段。
- `COMPACT_BOARD`：生成用于快速方向审阅的四视图合板；不自动升级为正式身份资产。

## Workflow

1. **Confirm asset status.** 明确输入是 `APPROVED CANON`、`IDENTITY CANDIDATE` 还是只有文字设想；记录 Asset ID、版本和参考图角色。
2. **Choose the view protocol.** 依据下游需要选择四视图快速板、全身六视图、头部角度组或局部细节板。不要为了形式完整生成无用途视图。
3. **Write the identity lock.** 按头颅与五官比例、可追踪不对称、发型结构、肤色与局部变化、体态比例、稳定标记、服装层级记录必须保持项。避免只写“完全一致”。
4. **Separate source images from the board.** 正式资产优先从同一 APPROVED 母图逐张派生独立视图，批准后再排成 Contact Sheet。一次生成的多格图只用于概念预览或审阅，不是唯一身份源。
5. **Calibrate pose and camera.** 全身视图保持相同站姿逻辑、相机高度、观察距离、近似焦段和身体尺度；中性放松不等于僵直 T-pose。手足完整可见，避免透视夸张和裁切。
6. **Calibrate light and background.** 使用干净的白至浅灰无缝背景、受控中性白平衡和大面积柔光，使骨骼、体积和皮肤可读。色温、眼神光形状和轮廓光不是固定参数；它们不得改变肤色判断或制造戏剧性人像。
7. **Render skin by hierarchy.** 先保证头面体积与年龄，再保证区域性色彩和油脂/干燥差异，最后才写毛孔、细纹、睫毛阴影与桃绒。微细节必须符合部位尺度，不能用均匀噪点模拟毛孔。
8. **Compile compactly.** 按 `用途与参考绑定 → 身份锁定 → 视图与姿态 → 摄影棚标定 → 皮肤/材料 → 排除项` 编写。把验收条件放在检查表，不把全部 QC 词重复塞进提示词。
9. **Review actual pixels.** REVIEW 时必须查看真实图片，比较五官距离、轮廓、发缝、耳形、痣疤位置、肩胯关系、四肢长度、服装结构与皮肤处理；文字声明不能证明一致。
10. **Route execution.** 实际资产生成、文件保存、manifest 和批准状态交给 `film-asset-designer`；特定模型语法、输入槽位和参数交给 `film-prompt-adapter`。本 Skill 不猜测模型能力，也不自行把图片标为 APPROVED。

## Default output

按任务规模输出最少必要内容：

- Asset ID / purpose / status
- Reference role map
- Locked identity summary
- Selected view protocol and rationale
- Master prompt and, for production assets, per-view prompts
- Negative constraints relevant to current risks
- File naming and derivation order
- Visual acceptance checklist
- Assumptions, unknowns and required upstream return

若保存到具体项目，提示词进入 `projects/<project-id>/assets/prompts/`，角色图片与合同进入对应 `assets/characters/<asset-id>/`；Project ID 不明确时不要创建项目交付物。

## Non-negotiable boundaries

- 不把“同一人物、绝对一致”当作足够的身份定义；必须列出可观察锚点。
- 不从不同随机种子分别重抽正式视图，再靠相似描述宣称同一身份。
- 不把四格 Contact Sheet 当作唯一 Canon Face/Body 原图。
- 不默认使用固定肤色、固定 5200K、暖色轮廓光、矩形眼神光、8K 或胶片颗粒。
- 不把所有毛孔做成同尺寸噪点，不添加假毛孔、塑料皮肤、油亮蜡感、涂抹磨皮或过度锐化。
- 不用戏剧性表情、姿态、强透视、复杂背景、道具或镜头级光线干扰身份判断。
- 不因“真实”而机械加入污垢、皱纹、斑点或病理特征；年龄与皮肤状态必须来自角色合同。
- 不复制真实人物肖像或受保护角色身份，除非用户已提供并明确授权相应用途。
- 不生成镜头关键帧或视频 Prompt，不修改 Character System 来迎合生图模型。

## Completion gate

- 每个视图绑定同一个批准身份或明确标为候选；
- 视图角度、相机、站姿与尺度足以比较结构；
- 五官、脸型、发型、肤色、体态、稳定标记和服装有具体锁定项；
- 皮肤细节符合部位、年龄、光线和尺度，不依赖噪点与锐化；
- 独立原图、Contact Sheet 与细节板的职责没有混淆；
- Prompt、排除项和验收表相互对应且没有冗余堆词；
- 未经真实像素审核的结果没有被标为 APPROVED。
