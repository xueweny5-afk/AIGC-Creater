# Seedance Prompt Profile

- **Last reviewed：** 2026-09-28
- **Evidence priority：** ByteDance official product/API material → ByteDance official GitHub samples → current product UI → community field notes
- **Dynamic profile：** Model version、入口、输入上限、时长、分辨率、引用标签和音频能力必须在每个项目中重新核实。

## Verified sources

- ByteDance Seedance 2.0 launch: https://seed.bytedance.com/en/blog/seedance-2-0-official-launch
- ByteDance Seedance 2.5 launch: https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5
- ByteDance AgentKit sample: https://github.com/bytedance/agentkit-samples/tree/main/skills/byted-seedance-video-generate

## Input-mode routing

- `T2V`: 文字承担主体、动作、场景、镜头和结束状态；不得声称身份由参考图锁定。
- `I2V / FIRST_FRAME`: 首帧承担身份、构图和初始状态；Prompt 重点写之后发生的动作、镜头、环境变化、声音与终点。
- `START_END`: 首尾帧必须属于可物理连接的同一动作；每帧角色和文件必须由当前入口核实。
- `MULTI_REFERENCE / R2V`: 图片、视频、音频分别声明唯一职责；角色、服装、场景、道具和运动参考不得相互覆盖。
- `EDIT / EXTEND`: 明确 `Change / Preserve / Constraints` 和衔接状态，不改写成新生成任务。

不得把不同入口的写法混用。官方样例同时出现有序媒体数组、`[图1]` 和 `@Image 1` 等表面形式；最终标签必须保持当前界面/API 的原样拼写。

## Reference map

先输出上传顺序，再输出 Prompt。每个输入至少记录：

| Slot / Label | File / Version | Role | Allowed Influence | Must Not Transfer | Required |
|---|---|---|---|---|---|
| Image 1 | approved frame | START / COMPOSITION | 开场构图、姿态、光线 | 不把分镜标注或拼图边框带入视频 | Yes |
| Image 2 | character canon | IDENTITY | 脸、年龄、体态、发型 | 不覆盖当前姿态和构图 | Yes |
| Image 3 | costume/look | WARDROBE | 服装结构、材质、配饰 | 不覆盖人物身份 | As needed |
| Image 4 | location/prop | TOPOLOGY / PROP | 空间、道具几何与材料 | 不覆盖镜头动作 | As needed |

Prompt 开头用一句话说明每个标签负责什么；必要时同时写明“不负责什么”。引用数量是上限而不是目标，优先保留少量、职责清楚、已批准的输入。

## Prompt structure

```text
Reference declaration
→ one-line visible intention
→ Shot/beat sequence in chronological order
→ subject performance and physical action
→ one motivated camera event per shot
→ light/environment/secondary motion
→ sound intent
→ observable final state
→ global continuity locks and exclusions
```

单动作短镜头不强制时间码；多阶段动作、剪辑、对白或声音同步才使用时间段。时间码是目标，不是假装逐帧确定性。

## Film-language rules

- 每个 Shot 明确景别、主体位置、主要动作、摄影机起止和可见终点。
- 情绪改写为可见行为，例如视线断开、呼吸延迟、手停在接触前，而不是只写“悲伤”。
- 参考图已经锁定的静态外观不重复长篇描述；只补充参考图无法携带的当前状态。
- 多镜头必须写清切换或过渡；不要让一个镜头同时承担多个互相冲突的运镜。
- 结束状态要能作为下一镜的 `Continuity In` 或明确完成本段。

## Preflight

- 当前 Model/Version/入口已记录并为 `VERIFIED`。
- 上传顺序、Prompt 标签和文件路径一致。
- 每个引用只有清晰职责，没有身份/服装/构图冲突。
- Shot 的时间、动作和声音无缺口或重叠。
- 人物、服装、道具、空间方位和终点均可观察。
- 无未经请求的字幕、Logo、额外人物或风格迁移。
