# Atmosphere State Contract

## Status

- `OPEN`
- `DEFINED`
- `READY FOR VISUAL / MOTION HANDOFF`
- `RETURN TO WORLD / RESEARCH`
- `ACTUAL MEDIA PENDING QC`

## Stable ID

使用 `ATM-<location>-<time/state>-V<n>`，例如 `ATM-KITCHEN-WINTER-NIGHT-V1`。同一状态的镜头只引用 ID；密度、来源或驱动发生叙事变化时创建新版本或明确的 Transition，不静默改写。

## Required state fields

- `Atmosphere State ID / Version / Status`
- `Bound Location / Scene / Narrative Look Arc / Look-Light State`
- `Medium Family / Composition`
- `Physical Source / Evidence Status`
- `Spatial Distribution / Height / Depth Layers`
- `Density / Visibility / Color / Particle or Droplet Scale`
- `Temperature / Humidity Context`（适用时）
- `Motion Driver / Direction / Speed / Turbulence / HOLD`
- `Light Source / Angle / Visibility Condition`
- `Material / Costume / Hair / Skin Response`
- `Subject Readability / Occlusion Limit`
- `Pre-state / Trigger / Transition / Post-state / Decay`
- `Allowed Variation / Forbidden Generic Behavior`
- `Asset Requirement / Prompt Mapping / QC Evidence`

## Evidence status

- `DOCUMENTED`
- `RESEARCH-INFERRED`
- `CREATIVE`
- `ASSUMED`
- `OPEN / UNKNOWN`

视觉参考中的雾、烟和尘只能成为 Soft Reference；除非项目合同与地点物理共同支持，否则不能直接成为硬锚点。

## Handoff map

- **Visual Bible：** State ID、来源、分布、受光、材料响应、允许变化。
- **Asset Design：** 干净场景底图与 Atmosphere Calibration/Interaction Plate 分开；空气图不能成为唯一拓扑依据。
- **Scene/Shot：** 当前状态、调度可能触发的变化、可见区域和遮挡上限。
- **Storyboard：** 单帧中的实际可见程度，不把运动过程画进静帧。
- **Motion：** 驱动、方向、速度、湍流、停止/沉降和人物互动。
- **Prompt：** 压缩为来源 + 局部分布 + 可见条件 + 驱动 + 禁止全局化。
- **QC：** 在时间码和相邻镜头中检查来源、空间关系、运动和密度连续。

## Completion rule

`READY FOR VISUAL / MOTION HANDOFF` 要求来源或 NONE 已决定，所有可见变化可由物理事件解释，且不遮挡叙事信息。实际生成之前不得填写通过结论；生成后由 Continuity QC 记录 Actual Observation。
