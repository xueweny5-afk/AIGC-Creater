---
name: film-atmosphere-designer
description: 为 AIGC 电影定义有物理来源、空间分布、受光方式和连续性规则的空气介质状态，包括清洁空气、湿气、雾、烟、蒸汽、粉尘、花粉与悬浮颗粒。用于视觉开发、场景状态、动态设计、提示词和 QC 之间的空气质感交接；不是新增制作阶段，不生成图片/视频，也不把通用雾和粒子当作电影感滤镜。
---

# Film Atmosphere Designer

把“空气质感”从审美形容词转成可追踪的物理状态。该 Skill 是 Stage 07–15 间的辅助能力，不改变主流程阶段与审批权。

## Required inputs

按当前任务读取已有材料：

1. Project Brief 的 Emotional Thesis / Core Image（如适用）
2. Screenplay 与 Scene/Location 范围
3. World & Visual Bible、Location State、Look/Light State
4. 已批准场景/材质资产与天气、时间、实际光源
5. Shot、Storyboard、Motion 或实际 Take（进入对应下游时）

缺少地点、时间、天气或来源信息时保持 `OPEN` 或 `NONE / CLEAN AIR`，不自动补雾。

## Load resources

- 设计前读取 `references/atmosphere-design-guide.md`。
- 创建或验收状态登记时读取 `references/atmosphere-state-contract.md`。
- 使用 `assets/atmosphere-state-register-template.md`。

## Output and placement

需要独立登记时保存：

```text
AIGC Creater/projects/<project-id>/visual-development/atmosphere-state-register.md
```

这是 Visual Development 的辅助合同，不是新阶段。简单项目可只把同样字段写入 World & Visual Bible 的 Scene Look & Light State；不要为了填表创建无意义文件。

## Workflow

1. **Decide whether atmosphere is needed.** 先判断空气介质是否由地点、天气、活动、叙事可读性或连续性真正要求；`NONE / CLEAN AIR` 是完整决定。
2. **Classify the medium.** 区分气溶胶/颗粒、蒸汽/湿气、烟、雾/霾、降水飞沫和清洁空气；不要把镜头光晕、胶片颗粒、噪点、浅景深误记为空气。
3. **Build the causal state.** 为每个状态建立稳定 `Atmosphere State ID`，记录介质、物理来源、空间分布、密度/能见度、粒径/可见尺度、颜色倾向、温湿条件与消散/沉降。
4. **Define motion drivers.** 只允许风、热对流、人物/物件经过、机械、开门、降水或明确特效源驱动；无作用时写 `HOLD`。
5. **Define visibility and response.** 写清哪个实际光源、角度和背景对比使介质可见，以及它对皮肤、服装、头发、地面、金属、玻璃和声音空间造成什么可观察影响。
6. **Design transitions.** 使用 `Pre-state → Physical Trigger → Transition → Post-state → Decay/Settle`，并标明影响的 Scene/Shot/Clip；空气不能在切镜后无因增减。
7. **Request only necessary assets.** 只为核心空间或近景需要生成 Atmosphere Calibration / Material Interaction Plate；它不能替代干净的场景拓扑与材质资产。
8. **Handoff downstream.** 向 Scene/Shot 传 ID 与允许变化，向 Motion 传驱动/速度/停止，向 Prompt 传紧凑可见语言，向 QC 传可观察验收点；不跨阶段重写镜头或动作。
9. **Audit.** 检查来源、分布、驱动、受光、遮挡、材料响应、连续性和叙事作用；删除只为“电影感”存在的通用粒子。

## Per-state requirements

- Atmosphere State ID / Version / Status
- Location / Scene / Look-Light State binding
- Medium type and `NONE / CLEAN AIR` option
- Physical source and evidence status
- 3D distribution / height / zones / foreground-midground-background
- Density / visibility / color tendency / scale
- Motion driver / direction / turbulence / speed / HOLD
- Light interaction / visibility condition
- Material, costume, hair and skin response
- Occlusion / readability / safety constraints
- Pre-state / trigger / transition / post-state / decay
- Allowed changes / forbidden generic behavior
- Required assets / downstream mappings / QC evidence

## Non-negotiable boundaries

- 不用“空气感、氛围感、电影雾”代替物理状态。
- 不默认添加逆光尘埃、全局薄雾、持续烟气、胶片颗粒或光晕。
- 不把传感器噪点、锐化、景深、黑柔和后期 Bloom 当作空气介质。
- 不让介质遮掉 Must Show、人物表演、文字、空间锚点或关键接触。
- 不凭空改变天气、时间、火源、热源、工业活动或故事事件。
- 不调用生成，不声称实际画面已经具有空气质感；真实结果必须由 QC 检查。

## Completion gate

- 每个状态有来源或明确为 NONE；
- 分布、密度、驱动、受光与消散可以被下游执行和观察；
- 所有变化有物理触发且跨镜连续；
- 材料和人物响应与天气/介质一致；
- Prompt 能压缩表达，QC 有可见验收点；
- 没有用空气效果替代故事、调度、灯光或材质设计。
