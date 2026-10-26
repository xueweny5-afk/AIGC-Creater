# Prompt Library Router

这套提示词库把上游创作合同编译成不同生产任务的执行语言。模板是决策辅助，不是需要逐栏填满的长 Prompt。

## Route by task

| 当前任务 | 必读模块 | 产出边界 |
|---|---|---|
| 人物身份、六视图、服装、妆发、场景、材质、道具 | `asset-prompt-patterns.md` | 静态资产意图；不加入镜头叙事 |
| Storyboard、Hero Frame、Start/End Keyframe | `shot-image-prompt-patterns.md` | 单一可见时刻；不描述完整运动 |
| T2V、I2V、首尾帧、多参考视频 | `video-prompt-patterns.md` | 从当前状态开始的时间过程 |
| 长篇电影视频 Prompt、固定框架、完整性复核 | `cinematic-video-prompt-framework.md` + 当前任务模块 | 先完成十三项工作台，再按 Model Profile 压缩；不机械输出十三段 |
| 环境质感、材料反应、空气厚度 | `material-atmosphere-patterns.md` | 有因果的材质与空气状态 |
| 已有结果局部失败、负向约束、返工 | `repair-and-exclusion-patterns.md` | 只改失败字段，保留已通过内容 |

随后读取目标模型 Profile。若 Profile 与通用模式冲突，以已核实的当前模型能力为执行边界，把不支持项标为 `UNSUPPORTED`，不能靠自然语言假装生效。

项目已批准采用中式诗意电影美学时，可读取 `pipeline/knowledge/style-prompt-library/chinese-poetic-cinema/README.md` 的整理版，提取构图可读性、局部光、色彩锚点和动态因果；`source-v3.1.md` 仅作来源参考。风格条目不能覆盖已批准的人物、时代、场景状态或镜头合同。

## Shared compilation layers

先在工作记录中检查六层，再压缩成模型原生 Prompt：

1. **Bindings：** 哪些参考负责身份、服装、拓扑、材质、构图、运动或声音，以及它们不得覆盖什么。
2. **Visible intent：** 这张图或这个 Clip 唯一需要让观众看见什么。
3. **State / action：** 静态图只写当前时刻；视频写起点、触发、变化、终点。
4. **Camera / composition：** 观看距离、角度、空间关系、摄影机事件及停止状态。
5. **World response：** 光、材料、天气、空气介质和必要的次级运动。
6. **Locks / exclusions：** 身份、数量、轴线、道具、文字、品牌、时代和模型常见失败。

这六层不是固定段落数。相同信息只出现一次；已由参考图可靠承载的内容不在正文重复绘制。

## Two-pass authoring

先写“完整执行合同”，再写“模型交付 Prompt”：

1. **Contract pass：** 保留故事语境、参考职责、状态、表演、镜头、声音、材质、空气与排除项，便于人审查缺口和冲突。
2. **Compile pass：** 根据当前模型 Profile 删除已由图片/参数承载的内容、无可观察作用的诗性总结、重复形容词和不支持能力，只保留模型需要执行的顺序。

教程中的长提示词适合当 Contract Pass 的好例子，但不能证明所有模型都更喜欢长 Prompt。最终长度由模型入口、任务风险和参考输入决定。

## Creative authority before wording

每项先标 `LOCKED / DERIVED / CREATIVE / PROPOSAL`。`CREATIVE` 字段允许主动做出大胆、具体且服务叙事的选择；`PROPOSAL` 必须先回责任上游。不要因为使用固定框架就把所有段落写成保守复述，也不要让风格词越权改写事实。

## Semantic calibration before detail

增加细节前先纠正“这到底是什么”：地点、时间/节日、人物关系、当前活动和唯一情感事件。`夜晚老屋`、`温馨家庭`、`农村青年`等宽泛类别必须被批准合同中的具体生活状态替换。类别错了，继续加入木纹、颗粒和光线只会把错误描述做得更精致。

## Evidence order

发生冲突时按以下顺序处理：用户锁定决定 → 已批准项目合同 → 当前状态资产/关键帧 → 已核实模型 Profile → 软参考方法 → 通用写法。外部风格参考不能覆盖人物身份、服装版本、空间事实或历史依据。

## Release test

发布前做三次快速检查：

- **正向复述：** Prompt 是否明确主体、当前状态、唯一任务和可见终点？
- **反向恢复：** 只看 Prompt 能否恢复关键身份、空间、动作阶段和禁止变化？
- **删词测试：** 删除一个词后若没有可观察差异，该词通常应删；“cinematic、masterpiece、8K、自然地”等不能替代具体决定。
