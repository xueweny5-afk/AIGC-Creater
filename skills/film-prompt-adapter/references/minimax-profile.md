# MiniMax Video Prompt Profile

- **Last reviewed：** 2026-09-28
- **Official sources：** MiniMax-AI GitHub organization
- **Dynamic profile：** `MiniMax-H3` 与 `MiniMax-Hailuo-*` 是不同模型族，时长、分辨率、输入模式和 Prompt 控制不得混写。

## Verified sources

- MiniMax H3 skill repository: https://github.com/MiniMax-AI/MiniMax-H3
- MiniMax skills repository: https://github.com/MiniMax-AI/skills
- Hailuo guide: https://github.com/MiniMax-AI/skills/blob/main/skills/frontend-dev/references/minimax-video-guide.md

## Route by model family

### MiniMax-H3

官方工具资料展示了 `T2V`、首尾帧和多模态参考等模式。执行 Profile 必须记录当前入口的真实参数。已核实的官方 CLI 工作流曾列出：4–15 秒、2K、最多 9 张参考图、3 个参考视频、3 个参考音频、混合参考总数 12；这些属于版本化能力，不得在未复核时永久写死到项目合同。

Prompt 顺序：

```text
output goal
→ subjects and reference roles
→ chronological action timeline
→ scene / time / light / weather
→ shot size / angle / camera / focus / cuts
→ look / color / texture / pacing
→ dialogue / ambience / SFX / music
→ hard continuity locks
→ negative constraints
```

每个 Shot 必须能回答：起始状态、主体动作、镜头事件、微时间线、结束状态和下一镜交接。

### MiniMax-Hailuo

官方 `MiniMax-AI/skills` 示例使用方括号摄影机命令，例如 `[Push in]`、`[Pull out]`、`[Pan left]`、`[Tracking shot]`、`[Static shot]`。只有当前 Model Profile 明确支持时才使用；不要把这些控制标记带入 H3 或其他模型。

已公开的 Hailuo-2.3 示例曾列出 6/10 秒与 768P/1080P 的组合限制。执行前必须重新核对当前模型和账户入口。

## Reference input map

每个 Unit 必须区分：

- `FIRST FRAME`：精确开场构图和状态；
- `LAST FRAME`：精确终点；
- `REFERENCE IMAGE`：身份、服装、场景或道具；
- `REFERENCE VIDEO`：动作、运镜、节奏或转场；
- `REFERENCE AUDIO`：音色、节奏、对白或环境声。

为每个输入写明 `Allowed Influence` 与 `Must Not Override`。首尾帧模式和多参考模式是否可混用，以当前 API/UI 为准；未核实则标 `UNKNOWN`。

## Camera discipline

- 一个简单镜头只设一个主运镜；复杂运镜需要已批准参考视频或拆 Clip。
- 区分 dolly、zoom、pan、truck、pedestal 和 handheld，不使用“镜头动起来”之类模糊指令。
- 静止镜头同时写正向 `static/locked` 与禁止漂移约束。
- 动作交接按因果顺序写：初始持有人/位置 → 释放或触发 → 转移 → 新持有人/位置 → 终态。

## Preflight

- Model Family 与 Prompt 语法一致。
- 时长、分辨率、画幅、参考数量和输入模式来自当前官方 Profile。
- 引用文件存在，版本与批准范围明确。
- Prompt 没有重复首帧画面，而是描述首帧之后的变化。
- 摄影机控制不会遮挡关键动作或与参考视频冲突。
- Hailuo 方括号命令未误用于 H3。
