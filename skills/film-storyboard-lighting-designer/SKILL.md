---
name: film-storyboard-lighting-designer
description: 在分镜构图和动作状态确定后，将已批准的 Narrative Look Arc、Scene Look & Light State、真实光源、时间天气与材质响应投影到逐镜画面，设计主光功能、环境反射、明暗关系、人物受光和跨镜连续性，并提供灯光返工提示词。用于分镜光影补全、逐帧灯光方案、光线连续性审核和已生成分镜的受控改光；不用于凭空重设全片影调、改变镜头构图、替代后期调色或生成视频。
---

# Film Storyboard Lighting Designer

把上游世界光线变成当前机位可见、可生成、可审核的逐镜光影。光影设计必须同时成立于人物、空间、材料、阴影和相邻镜头，不能只是给脸增加一束漂亮的光。

## Required inputs

1. Storyboard / Frame Manifest 与独立 Frame 图片，构图和动作状态至少已批准为 `COMPOSITION ONLY / STATE ONLY`；
2. Frame Contract、Shot List 与 Continuity Ledger；
3. World & Visual Bible 的 Narrative Look Arc 和准确 `Scene Look & Light State ID / Version`；
4. Scene Design、Location/Topology、时间、天气、可见与离画实际光源；
5. Character、Costume、Prop 与 Material 资产版本；
6. Atmosphere State（存在雾、烟、尘、雨、蒸汽等介质时）；
7. 用户锁定的影调、参考范围与交付画幅。

缺少时间、天气、光源位置或 Look/Light State 时，只能做 `LIGHTING EXPLORATION`，不能创建生产级 Lighting Pass。Storyboard 只有 Contact Sheet 而无独立原图时返回 Storyboard。

## Load resources

- 开始设计、改写或审核前读取 [storyboard-lighting-craft.md](references/storyboard-lighting-craft.md)。
- 创建交付物时使用 [lighting-pass-template.md](assets/lighting-pass-template.md)。

## Modes

- `PLAN_ONLY`：建立逐帧 Lighting Card 与连续性账本，不修改图片。
- `HANDOFF`：输出按 Frame ID 编号的可复制灯光编辑提示词包，由用户外部生成。
- `GENERATE`：用户明确要求实际改图且工具可用时，对独立 Frame 创建新版本并逐张审核。
- `REVIEW`：审核现有分镜的光源、曝光、人物受光、阴影、材质和跨镜连续性。
- `REPAIR`：使用 `Change / Preserve / Constraints` 只修光影失败字段。

未明确要求修改图片时默认 `PLAN_ONLY`。任何实际改图前先展示提示词、参考图职责与目标文件名，并让用户在当前批次选择 `AUTO_GENERATE` 或 `USER_GENERATE`。

## Workflow

1. **Verify the upstream light contract.** 锁定 Narrative Look Arc、Scene Look & Light State、时间天气、Atmosphere State 与世界坐标中的实际光源。若当前创意要求新增光源、改变日夜、方向、色彩逻辑或叙事光线弧，返回 Visual Development / Scene Design。
2. **Map sources in world space.** 登记每个光源的位置、方向、大小/距离关系、光质、遮挡、颜色关系与可影响区域；区分太阳/天空、窗光、火、灯具、招牌、反射面等实际来源。`Key / Fill / Rim` 是画面功能，不自动等于三盏灯。
3. **Project light into the camera view.** 对每个 Frame 同时记录世界方向和画面中的投影方向。摄影机反打、转轴或移动后，光源在世界中不能随画面左右标签跳位。
4. **Set frame hierarchy.** 确定观众先看哪里、主体与环境如何分离、哪些信息可落入暗部、哪些 Must Show 必须可读。光影强调必须服从 Shot 功能和表演，而不是给每帧做同一种英雄光。
5. **Design subject response.** 写清脸部与身体受光面、眼部可读性、肤色/年龄纹理、服装层次、手和道具是否需要看清；阴影可以保留，但不能无意遮掉关键表演或接触。
6. **Design environment response.** 补全墙地顶反射、负补光/遮挡、背景层次、实际灯具、投影方向、接触阴影、高光和材料响应。人物与环境必须处在同一套光线中。
7. **Control exposure, contrast and color relationships.** 定义主体与背景、亮部与暗部、实际光源之间的相对关系，保护皮肤、天空、火焰、灯具与反光材料。仅在设备或模型确实需要时写具体 Kelvin、照度或光比；否则使用可观察的相对关系。
8. **Integrate atmosphere physically.** 空气介质只按批准的来源、分布、密度和驱动受光；没有介质时保持 `NONE / CLEAN AIR`。不为显示光束而凭空加雾。
9. **Build the sequence lighting arc.** 相邻 Frame 检查光源方向、阴影几何、曝光、黑位、肤色、材料与介质。只有人物/摄影机进入新区域、开关灯、火势变化、天气/时间推进或其他批准触发时，光线才改变。
10. **Prepare a surgical edit.** 已有 Frame 使用 `Change / Preserve / Constraints`：只改光影，冻结身份、姿态、构图、镜头、场景拓扑、道具和文字。若需要改变这些字段，返回正确上游。
11. **Inspect actual pixels.** 实际查看每张结果，核对人物和环境是否共同受光、阴影是否附着、反射是否来自材料、暗部是否有层次、亮部是否溢出，以及相邻镜头是否连续。只检查文字方案不能标记通过。
12. **Version and route.** 灯光编辑结果保存为同一 Frame ID 下的新版本，更新 Frame Contract 与 Lighting Ledger，再返回 Storyboard Review。Lighting Pass 通过后，Motion Designer 继承静态光线与允许动态变化；Prompt Adapter 只编译，不重新设计。

## Outputs

```text
AIGC Creater/projects/<project-id>/storyboard/lighting/
├── lighting-pass.md
├── lighting-continuity-ledger.md
└── lighting-edit-prompts.md          # HANDOFF / GENERATE 时
```

实际修改后的 Frame 放在原 `storyboard/frames/<frame-id>/` 中，以新版本保存，不覆盖批准原图。Project ID 不明确时不要创建项目文件。

## Per-frame requirements

- Frame / Shot / Scene IDs and source versions
- Narrative Look Arc / Scene Look & Light State / Atmosphere State
- Story function / visual priority / Must Show
- World-space sources / position / direction / occlusion
- Camera-view projection
- Key function / ambient-fill-bounce / negative fill / practicals / optional separation
- Source color relationship / exposure / contrast / black and highlight protection
- Character face, body, eye, skin, costume, hand and prop response
- Environment, material, shadow, reflection and atmosphere response
- Continuity In / Out / change trigger
- Change / Preserve / Constraints
- Target file / version / review evidence / result

## Non-negotiable boundaries

- 不在分镜完成后才凭空发明全片影调；上游没有光线合同就返回 Visual Development。
- 不用“温暖、冷峻、电影感、史诗光”替代光源、方向、光质、遮挡和受光结果。
- 不为每个镜头分别创造不相容的漂亮主光、轮廓光或色温。
- 不默认增加逆光、窗缝光、顶光、眼神光、轮廓光、体积光或高反差侧光。
- 不让光源跟随画面左右变化；必须同时保持世界坐标和摄影机投影正确。
- 不只重打人物脸而忽略墙面、地面、衣物、道具、阴影与反射。
- 不用蓝色覆盖表示夜晚，不压死黑位，不炸白皮肤、天空、灯具或火焰。
- 不凭空加雾、尘或烟来显示光束，不把 Bloom、黑柔、颗粒当作场景光线。
- 不修改身份、姿态、表演、构图、机位、空间拓扑、道具状态、文字或故事动作。
- 不把 Lighting Pass 当后期调色；Post 只能匹配和精修，不能修复错误光向或不存在的真实光源。
- 不生成视频，不声称灯光方案已被模型或最终成片验证。

## Completion gate

- 每帧继承准确的 Look/Light 与 Atmosphere State；
- 所有主光、环境光、反射、遮挡和分离光都有物理来源或明确返回；
- 世界方向与画面投影同时记录，反打和相邻镜头没有光向跳变；
- 人物、环境、材料、阴影和空气响应属于同一光场；
- 主体可读性、暗部层次、亮部保护和色彩关系可观察；
- 光线变化有批准触发并与相邻 Frame 连续；
- 改图只改变授权光影字段，批准原图未被覆盖；
- 实际结果经过逐帧与顺序像素审核，或明确保持 PLAN_ONLY。
