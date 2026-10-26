# Material and Atmosphere Prompt Patterns

“去 AI 感”不是追加真实、8K、胶片和雾，而是让材料、使用痕迹、空气和光线具有可解释的局部差异。

项目存在 `atmosphere-state-register.md` 时，本模块只负责把对应 Atmosphere State ID 压缩成模型语言，不重新决定介质、天气或状态变化。没有独立登记时，仍须从批准的 Scene Look & Light State 读取同等字段。

## Material sentence

每种关键材料最多回答五件事：

```text
material and construction
→ surface scale / edge / seam
→ localized use or weathering cause
→ response to the current light
→ response to action, wind, rain or heat
```

示例：`深色旧木桌由宽木板拼接，板缝略不均；常被手肘摩擦的近侧边缘比桌面更亮，背光处保留细小凹痕，蒸汽掠过时只在冷的金属杯壁形成短暂凝结。`

避免：所有表面同样粗糙、全局划痕、均匀污渍、塑料高光、无位置的“做旧感”。

## Atmospheric medium state

空气介质只有在以下字段可回答时才加入：

| Field | Question |
|---|---|
| Medium | 灰尘、蒸汽、烟、雾、湿气、花粉或其他什么？ |
| Source | 炉灶、矿尘、舞台、海风、雨后地面等从何产生？ |
| Distribution | 靠近地面、窗边光束、热源上方还是整个空间？ |
| Density | 是否足以影响能见度，还是只在逆光中偶尔可见？ |
| Driver | 风、热对流、人物经过、机械或降水如何推动？ |
| Light interaction | 哪个有来源的光使其可见？ |
| Continuity | 前后镜是否保持，何种事件允许变化？ |

可复制骨架：

```text
场景继承 [Look/Light State]。空气中存在少量 [medium]，来源是 [physical source]，主要分布在 [location/height]；只有经过 [motivated light] 时才可见，由 [wind/heat/action] 缓慢推动。它提供前后景层次，但不遮挡主体、不形成均匀浓雾，也不无因增减。
```

## Lived-in environment

生活感来自因果组合：物件为什么在那里、谁经常使用、哪里更容易磨损、热量和水汽从何处产生、室内外光色为何不同。一个可靠环境 Prompt 通常只需要少量高辨识细节，不需要列举整个房间。

例如室内暖光与室外冷夜可以同时存在，但要写出实际光源、门窗关系和材料反射；不能只写“冷暖对比、电影氛围”。

## Grain, haze and lens language

胶片颗粒、黑柔、薄雾、浅景深等不是同一层：黑柔/Pro-Mist、Halation、Bloom 和数字锐化属于成像/后期；雾、烟、蒸汽与尘属于物理空气；胶片颗粒属于记录质感。只有 Visual Bible/Look State 已批准且当前镜头需要时才加入，分别写清强度和作用，避免用镜头滤镜伪装空气，也避免它们遮盖皮肤、织物、文字或空间证据。
