# Shot Image Prompt Patterns

镜头图片 Prompt 只表现一个可见时刻。它从 Shot/Frame Contract 投影构图与状态，不承担完整时间过程。

继承 Frame 的 Audience Read、Viewing Stance、Must Read/Withhold、Composition Relations 和批准的 Presentation Mode / Artistic Rule IDs；不强制动作高潮、三层空间、摄影写实或每帧都有微动作。只编译当前可见快照，不能用 Prompt 声称已验证呼吸时序、运动或首尾过渡。相邻帧参考锁状态，原始资产锁身份/服装/空间；构图图不迁移旧人物、光色或美术细节。缺必需参考的文字卡标 WAITING_DEPENDENCY，不虚构绑定路径或执行就绪。

## Compact order

```text
reference bindings
→ frame purpose and represented instant
→ subjects, positions and visible action snapshot
→ shot size / angle / depth / focus
→ inherited scene, look and light state
→ material and atmosphere evidence visible in this frame
→ continuity locks and exclusions
```

## Represented instant

用三句工作笔记确定时刻，但只把中间一句编入 Prompt：

- 刚刚发生：用于确认动作阶段，不一定写入。
- 现在可见：人物姿态、重心、视线、手与道具、表情张力。
- 下一刻将发生：用于防止画面越过节点，不写成运动过程。

例如不要写“她悲伤地转过头然后离开”；静态帧应写“她的身体仍朝门口，重心已经移向前脚，脸停在转头一半，视线落在桌上的信上，右手尚未离开椅背”。

## Composition language

优先写观众能观察的关系：主体占画面比例、眼平/俯仰、前中后景遮挡、负空间、人物间距离、视线落点、透视扩张或压缩。焦距数值只有在当前模型 Profile 已证明有用时才加入；否则不要用虚假精确代替空间关系。

## Reference bindings

每个输入只承担一个主职责：

```text
[Image 1] 只负责人物身份，不转移其服装、姿态和背景。
[Image 2] 负责当前服装结构与材料，不改变人物脸和年龄。
[Image 3] 负责场景拓扑与固定陈设，不复制其中偶然人物、文字或水印。
[Image 4] 仅借鉴低饱和关系和侧向自然光，不复制具体构图或对象。
```

## Static-frame exclusions

保留对当前帧真正重要的限制：人物数量、左右关系、持物手、道具状态、可见文字、轴线、时代元素、光向与不可越过的动作阶段。不要为每张图复制一份通用“低质量、模糊、最差质量”词表。
