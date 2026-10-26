# 04-道具｜剩余静态资产执行卡 V2

日期：2026-10-05。仅资产图片，不含分镜帧或视频。依赖规则与优先队列见 [index.md](index.md)。可开始制作候选不等于该资产G3放行；已有候选保持原验收级别。

## UP-056

PROP-LONGBLADE-001｜B刀W0材料基准

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/state-w0-material-intact-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-056及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png>) — 只用中间B型锁刀身几何；已存在，沿用当前版本
2. [assets/props/PROP-LONGBLADE-001/structure-b-detail-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/structure-b-detail-v001.png>) — 对应身份角度或上一状态，用途以主提示词限定；已存在，沿用当前版本
3. [assets/locations/MAT-BATTLEFIELD-001/material-dark-metal-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-dark-metal-v001.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本
4. [assets/locations/MAT-BATTLEFIELD-001/material-wood-grip-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-wood-grip-v001.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一把本片视觉重构B型长刀，几何唯一来自第一张比较图中间B：刃背、刀尖、刀柄、连接套箍、长度比例不变，不使用另两候选或持刀图的刀尖误差。暗铁窄高光、粗木柄、实用握缠，不改成关刀偃月刀，不声称历史陌刀唯一复原。灰背景自然光，整刀入画，无文字水印。制作W0完整使用旧态：干燥、无新伤，保留几何，在整刀旁放刀刃/套箍/握缠/铁柄尾四个同一物的细节放大；金属和木板只锁材料质感，套箍连接能承重，无装饰纹。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：W0同时补材料近景，不再另生相同的材料图；连接件不能凭放大板随机新增。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-057

PROP-LONGBLADE-001｜W1汗尘

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/state-w1-sweat-dust-v001.png`（新版本，不覆盖原图）。
- 前置：UP-056 state-w0-material-intact-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-057及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png>) — 只用中间B型锁刀身几何；已存在，沿用当前版本
2. [assets/props/PROP-LONGBLADE-001/state-w0-material-intact-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/state-w0-material-intact-v001.png>) — 仅材质或受光，不改身份/几何；待UP-056回传并通过
3. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一把本片视觉重构B型长刀，几何唯一来自第一张比较图中间B：刃背、刀尖、刀柄、连接套箍、长度比例不变，不使用另两候选或持刀图的刀尖误差。暗铁窄高光、粗木柄、实用握缠，不改成关刀偃月刀，不声称历史陌刀唯一复原。灰背景自然光，整刀入画，无文字水印。第二张只作上一状态，第三张仅在落地状态引用干土材质。只在握持区加汗尘深色，向上暴露面少量干尘，刃口无新增缺口。一张单状态，不合成连续动画。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：同几何同磨损，汗尘不均匀糊满刀，W3不代替C的独特遗刀。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-058

PROP-LONGBLADE-001｜W2轻损

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/state-w2-small-damage-v001.png`（新版本，不覆盖原图）。
- 前置：UP-057 state-w1-sweat-dust-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-058及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png>) — 只用中间B型锁刀身几何；已存在，沿用当前版本
2. [assets/props/PROP-LONGBLADE-001/state-w1-sweat-dust-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/state-w1-sweat-dust-v001.png>) — 对应父状态：保留身份、污染与损伤；待UP-057回传并通过
3. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一把本片视觉重构B型长刀，几何唯一来自第一张比较图中间B：刃背、刀尖、刀柄、连接套箍、长度比例不变，不使用另两候选或持刀图的刀尖误差。暗铁窄高光、粗木柄、实用握缠，不改成关刀偃月刀，不声称历史陌刀唯一复原。灰背景自然光，整刀入画，无文字水印。第二张只作上一状态，第三张仅在落地状态引用干土材质。从W1只加少量刃口小缺损和接触擦痕，不折断、不弯刃，保留汗尘。一张单状态，不合成连续动画。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：同几何同磨损，汗尘不均匀糊满刀，W3不代替C的独特遗刀。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-059

PROP-LONGBLADE-001｜W3遗落

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/state-w3-dropped-v001.png`（新版本，不覆盖原图）。
- 前置：UP-058 state-w2-small-damage-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-059及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png>) — 只用中间B型锁刀身几何；已存在，沿用当前版本
2. [assets/props/PROP-LONGBLADE-001/state-w2-small-damage-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/state-w2-small-damage-v001.png>) — 对应父状态：保留身份、污染与损伤；待UP-058回传并通过
3. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一把本片视觉重构B型长刀，几何唯一来自第一张比较图中间B：刃背、刀尖、刀柄、连接套箍、长度比例不变，不使用另两候选或持刀图的刀尖误差。暗铁窄高光、粗木柄、实用握缠，不改成关刀偃月刀，不声称历史陌刀唯一复原。灰背景自然光，整刀入画，无文字水印。第二张只作上一状态，第三张仅在落地状态引用干土材质。同一W2刀横落简化干土地，重力接触和局部尘附着可信；旧汗尘和小缺损保留，不变柄长。一张单状态，不合成连续动画。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：同几何同磨损，汗尘不均匀糊满刀，W3不代替C的独特遗刀。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-060

PROP-LONGBLADE-001｜三角色刀差异

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/role-variants-b-v001.png`（新版本，不覆盖原图）。
- 前置：UP-025 contact-longblade-l1-v002.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-060及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png>) — 只用中间B型锁刀身几何；已存在，沿用当前版本
2. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-blade-m3-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-blade-m3-v001.png>) — 同一标记物/状态（结构以使用态优先）；已存在，沿用当前版本
3. [assets/costumes/COST-LISIYE-001/contact-longblade-l1-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/costumes/COST-LISIYE-001/contact-longblade-l1-v002.png>) — 已有接触姿态，仅证明实际可见接触；待UP-025回传并通过

### 直接复制｜主提示词

```text
同一把本片视觉重构B型长刀，几何唯一来自第一张比较图中间B：刃背、刀尖、刀柄、连接套箍、长度比例不变，不使用另两候选或持刀图的刀尖误差。暗铁窄高光、粗木柄、实用握缠，不改成关刀偃月刀，不声称历史陌刀唯一复原。灰背景自然光，整刀入画，无文字水印。无字三栏参考：主角常规B刀；李嗣业使用同制造家族B刀，适合现有人体握距但不夸张变成巨刃；瘦高C刀上握持区为深褐缠握加浅赭细缠线、局部磨亮和小缺口，普通铁箍柄尾。三刀基准几何相同，只依参考差异锁使用标记，不凭空增加雕花。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：第三张校准后才能引用；C标记不可染给主角刀，李刀不随演员力量幻想增大。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-064

PROP-FLAGS-001｜三旗无风垂落

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-FLAGS-001/flags-drape-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-064及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/props/PROP-FLAGS-001/flags-comparison-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-FLAGS-001/flags-comparison-front-v001.png>) — 同一旗几何/补缀/阵营配色；已存在，沿用当前版本
2. [assets/props/PROP-FLAGS-001/flags-comparison-reverse-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-FLAGS-001/flags-comparison-reverse-v001.png>) — 同一旗几何/补缀/阵营配色；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一三种本片原创识别旗：小暗红前军旗两处浅褐补缀、较大完整暗红中军旗、灰褐燕旗。保留矩形比例、暗包边、两道绑绳、木杆与粗织布，不能加字龙纹印章，不宣称史实旗制。自然光低饱和写实、无文字水印。第一张锁正面，第二张锁反面关系，灰背景。三旗分隔并列，无风自然沿杆下垂、折叠有重量；每种杆绳与补缀不变。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：补缀同位置同洞；正反缝法、杆绳真实连接；反面此前未证明的结构记重构。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-065

PROP-FLAGS-001｜三旗同向侧风

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-FLAGS-001/flags-sidewind-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-065及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/props/PROP-FLAGS-001/flags-comparison-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-FLAGS-001/flags-comparison-front-v001.png>) — 同一旗几何/补缀/阵营配色；已存在，沿用当前版本
2. [assets/props/PROP-FLAGS-001/flags-comparison-reverse-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-FLAGS-001/flags-comparison-reverse-v001.png>) — 同一旗几何/补缀/阵营配色；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一三种本片原创识别旗：小暗红前军旗两处浅褐补缀、较大完整暗红中军旗、灰褐燕旗。保留矩形比例、暗包边、两道绑绳、木杆与粗织布，不能加字龙纹印章，不宣称史实旗制。自然光低饱和写实、无文字水印。第一张锁正面，第二张锁反面关系，灰背景。三旗分隔并列，在同向微侧风中布面略展开，弯曲和绳拉力合理，不飘成硬板。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：补缀同位置同洞；正反缝法、杆绳真实连接；反面此前未证明的结构记重构。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-066

PROP-FLAGS-001｜旗反面与杆绳细节

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-FLAGS-001/front-flag-reverse-stitch-detail-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-066及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/props/PROP-FLAGS-001/flags-comparison-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-FLAGS-001/flags-comparison-front-v001.png>) — 同一旗几何/补缀/阵营配色；已存在，沿用当前版本
2. [assets/props/PROP-FLAGS-001/flags-comparison-reverse-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-FLAGS-001/flags-comparison-reverse-v001.png>) — 同一旗几何/补缀/阵营配色；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一三种本片原创识别旗：小暗红前军旗两处浅褐补缀、较大完整暗红中军旗、灰褐燕旗。保留矩形比例、暗包边、两道绑绳、木杆与粗织布，不能加字龙纹印章，不宣称史实旗制。自然光低饱和写实、无文字水印。第一张锁正面，第二张锁反面关系，灰背景。四处无字细节：前军旗补洞反面针脚与正面同一补缀；包边；两道绑绳与杆；磨损木杆。反面不是新贴两个装饰补丁。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：补缀同位置同洞；正反缝法、杆绳真实连接；反面此前未证明的结构记重构。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-067

PROP-FLAGS-001｜F1前军倾旗由人承重

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-FLAGS-001/front-flag-f1-bearer-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-067及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/props/PROP-FLAGS-001/flags-comparison-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-FLAGS-001/flags-comparison-front-v001.png>) — 同一旗几何/补缀/阵营配色；已存在，沿用当前版本
2. [assets/props/PROP-FLAGS-001/front-flag-f1-tilted-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-FLAGS-001/front-flag-f1-tilted-v001.png>) — 对应身份角度或上一状态，用途以主提示词限定；已存在，沿用当前版本
3. [assets/groups/GROUP-TANG-FRONT-001/lineup-six-soldiers-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/lineup-six-soldiers-v002.png>) — 身份索引，不覆写剧情站位；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一三种本片原创识别旗：小暗红前军旗两处浅褐补缀、较大完整暗红中军旗、灰褐燕旗。保留矩形比例、暗包边、两道绑绳、木杆与粗织布，不能加字龙纹印章，不宣称史实旗制。自然光低饱和写实、无文字水印。只出现一面小暗红前军旗与普通唐军旗手，全身手脚和杆端入画。旗杆倾斜，由旗手双手和身体重心支撑，保留F1轻损与两处补缀。简化干土地，不出现展示台底座，风与布面重力一致，不复制核心演员脸。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：前军F1已有孤旗图，本图只补持旗受力。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-068

PROP-FLAGS-001｜F2中军维持旗号

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-FLAGS-001/center-flag-f2-bearer-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-068及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/props/PROP-FLAGS-001/flags-comparison-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-FLAGS-001/flags-comparison-front-v001.png>) — 同一旗几何/补缀/阵营配色；已存在，沿用当前版本
2. [assets/characters/CHAR-GUOZIYI-001/action-g0-raise-hand-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/characters/CHAR-GUOZIYI-001/action-g0-raise-hand-v001.png>) — 对应身份角度或上一状态，用途以主提示词限定；已存在，沿用当前版本
3. [assets/costumes/COST-GUOZIYI-001/combined-look-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/costumes/COST-GUOZIYI-001/combined-look-front-v001.png>) — 衣甲连续性/穿戴结构；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一三种本片原创识别旗：小暗红前军旗两处浅褐补缀、较大完整暗红中军旗、灰褐燕旗。保留矩形比例、暗包边、两道绑绳、木杆与粗织布，不能加字龙纹印章，不宣称史实旗制。自然光低饱和写实、无文字水印。只使用较大完整暗红中军旗。普通旗手在简化干土地上真实双手竖直持杆，杆端接地，不用展示底座。郭子仪在侧前方作小幅抬手制止退旗的状态，面孔衣甲遵循第二三张，手势不被旗遮住。前景清洁空气，人物完整稳定，不拍成帝王高台演说。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：工作室旗层级测试已有，不当作此战地持旗证据；F2通过后交叉引用郭子仪，不重生G0。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-069

PROP-CONTINUITY-MARKERS-001｜缺左护耳整顶头盔结构校核

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-structure-detail-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-069及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/groups/GROUP-TANG-FRONT-001/soldier-a-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-a-front-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
2. [assets/groups/GROUP-TANG-FRONT-001/soldier-a-left-side-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-a-left-side-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
3. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-helmet-m3-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-helmet-m3-v001.png>) — 同一标记物/状态（结构以使用态优先）；已存在，沿用当前版本

### 直接复制｜主提示词

```text
制作同一件连续性遗物的无字结构参考，以人物正侧使用态为结构首要锚点，落地M3仅为材质/落地辅助，不继承其可能漂移的结构。人物解剖左护耳在战前就缺，保留左安装环、右护耳、内衬和甲片排数，绝不让已缺护耳再次掉落。灰背景自然光写实，单物全形加连接/结法/缺损细节，不加血浆断肢铭牌，不新增装饰。若M0/M3冲突，优先保持M0结构。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：先核对M0/M3是同一物；失败只修这件结构，不生成新的标记体系。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-070

PROP-CONTINUITY-MARKERS-001｜缺左护耳整顶头盔M1松脱

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-m1-transition-v001.png`（新版本，不覆盖原图）。
- 前置：UP-069 marker-a-structure-detail-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-070及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/groups/GROUP-TANG-FRONT-001/soldier-a-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-a-front-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
2. [assets/groups/GROUP-TANG-FRONT-001/soldier-a-left-side-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-a-left-side-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
3. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-helmet-m3-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-helmet-m3-v001.png>) — 同一标记物/状态（结构以使用态优先）；已存在，沿用当前版本
4. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-structure-detail-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-structure-detail-v001.png>) — 同一物的已审结构；待UP-069回传并通过

### 直接复制｜主提示词

```text
同一名军士与同一标志物的局部受力参考，依结构校核图固定该物。人物解剖左护耳在战前就缺，保留左安装环、右护耳、内衬和甲片排数，绝不让已缺护耳再次掉落。M1状态：整顶头盔因冲击松动但仍在A头上。自然光低饱和写实，背景简化，只表现一个瞬间，无字水印，无具体死法。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：M1仍属于原所有者，不提前变成M3遗物；左右/结/刃口位置一致。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-071

PROP-CONTINUITY-MARKERS-001｜缺左护耳整顶头盔M2无人持有

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-m2-unheld-v001.png`（新版本，不覆盖原图）。
- 前置：UP-069 marker-a-structure-detail-v001.png 通过后；UP-070 marker-a-m1-transition-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-071及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/groups/GROUP-TANG-FRONT-001/soldier-a-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-a-front-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
2. [assets/groups/GROUP-TANG-FRONT-001/soldier-a-left-side-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-a-left-side-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
3. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-helmet-m3-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-helmet-m3-v001.png>) — 同一标记物/状态（结构以使用态优先）；已存在，沿用当前版本
4. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-structure-detail-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-structure-detail-v001.png>) — 同一物的已审结构；待UP-069回传并通过
5. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-m1-transition-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-m1-transition-v001.png>) — 同一标记物/状态（结构以使用态优先）；待UP-070回传并通过

### 直接复制｜主提示词

```text
同一件标志物M2无人持有状态。人物解剖左护耳在战前就缺，保留左安装环、右护耳、内衬和甲片排数，绝不让已缺护耳再次掉落。由已审M1派生：整顶缺左护耳头盔刚离头触地，仍保留右护耳和内衬。物与地面真实接触，灰褐干土，自然光写实，无字水印无血浆。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：M2→M3仅尘附着/静止，不换物；具体落点以后绑定同一战场B3和T4，不随机指定地理坐标。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-072

PROP-CONTINUITY-MARKERS-001｜右前臂旧布结构校核

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-structure-detail-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-072及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/groups/GROUP-TANG-FRONT-001/soldier-b-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-b-front-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
2. [assets/groups/GROUP-TANG-FRONT-001/soldier-b-right-side-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-b-right-side-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
3. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-cloth-m3-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-cloth-m3-v002.png>) — 同一标记物/状态（结构以使用态优先）；已存在，沿用当前版本

### 直接复制｜主提示词

```text
制作同一件连续性遗物的无字结构参考，以人物正侧使用态为结构首要锚点，落地M3仅为材质/落地辅助，不继承其可能漂移的结构。人物解剖右前臂灰褐旧布，保留固定结法、两端不等长毛边、汗尘色差，脱离后为柔软布条而非硬套筒。灰背景自然光写实，单物全形加连接/结法/缺损细节，不加血浆断肢铭牌，不新增装饰。若M0/M3冲突，优先保持M0结构。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：先核对M0/M3是同一物；失败只修这件结构，不生成新的标记体系。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-073

PROP-CONTINUITY-MARKERS-001｜右前臂旧布M1松脱

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-m1-transition-v001.png`（新版本，不覆盖原图）。
- 前置：UP-072 marker-b-structure-detail-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-073及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/groups/GROUP-TANG-FRONT-001/soldier-b-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-b-front-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
2. [assets/groups/GROUP-TANG-FRONT-001/soldier-b-right-side-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-b-right-side-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
3. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-cloth-m3-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-cloth-m3-v002.png>) — 同一标记物/状态（结构以使用态优先）；已存在，沿用当前版本
4. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-structure-detail-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-structure-detail-v001.png>) — 同一物的已审结构；待UP-072回传并通过

### 直接复制｜主提示词

```text
同一名军士与同一标志物的局部受力参考，依结构校核图固定该物。人物解剖右前臂灰褐旧布，保留固定结法、两端不等长毛边、汗尘色差，脱离后为柔软布条而非硬套筒。M1状态：右臂旧布结开始松动、尾端下垂，B仍在。自然光低饱和写实，背景简化，只表现一个瞬间，无字水印，无具体死法。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：M1仍属于原所有者，不提前变成M3遗物；左右/结/刃口位置一致。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-074

PROP-CONTINUITY-MARKERS-001｜右前臂旧布M2无人持有

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-m2-unheld-v001.png`（新版本，不覆盖原图）。
- 前置：UP-072 marker-b-structure-detail-v001.png 通过后；UP-073 marker-b-m1-transition-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-074及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/groups/GROUP-TANG-FRONT-001/soldier-b-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-b-front-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
2. [assets/groups/GROUP-TANG-FRONT-001/soldier-b-right-side-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-b-right-side-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
3. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-cloth-m3-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-cloth-m3-v002.png>) — 同一标记物/状态（结构以使用态优先）；已存在，沿用当前版本
4. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-structure-detail-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-structure-detail-v001.png>) — 同一物的已审结构；待UP-072回传并通过
5. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-m1-transition-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-m1-transition-v001.png>) — 同一标记物/状态（结构以使用态优先）；待UP-073回传并通过

### 直接复制｜主提示词

```text
同一件标志物M2无人持有状态。人物解剖右前臂灰褐旧布，保留固定结法、两端不等长毛边、汗尘色差，脱离后为柔软布条而非硬套筒。由已审M1派生：旧布离开手臂，松散下垂刚触地，结与毛边连续。物与地面真实接触，灰褐干土，自然光写实，无字水印无血浆。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：M2→M3仅尘附着/静止，不换物；具体落点以后绑定同一战场B3和T4，不随机指定地理坐标。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-075

PROP-CONTINUITY-MARKERS-001｜C独特B刀结构校核

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-structure-detail-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-075及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/groups/GROUP-TANG-FRONT-001/soldier-c-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-c-front-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
2. [assets/groups/GROUP-TANG-FRONT-001/soldier-c-left-side-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-c-left-side-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
3. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-blade-m3-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-blade-m3-v001.png>) — 同一标记物/状态（结构以使用态优先）；已存在，沿用当前版本
4. [assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png>) — 只用中间B型锁刀身几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
制作同一件连续性遗物的无字结构参考，以人物正侧使用态为结构首要锚点，落地M3仅为材质/落地辅助，不继承其可能漂移的结构。瘦高C的B型刀，上握持区深褐缠握与浅赭细缠线、局部磨亮和小缺口，普通铁箍尾，不染到主角刀。灰背景自然光写实，单物全形加连接/结法/缺损细节，不加血浆断肢铭牌，不新增装饰。若M0/M3冲突，优先保持M0结构。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：先核对M0/M3是同一物；失败只修这件结构，不生成新的标记体系。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-076

PROP-CONTINUITY-MARKERS-001｜C独特B刀M1松脱

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-m1-transition-v001.png`（新版本，不覆盖原图）。
- 前置：UP-075 marker-c-structure-detail-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-076及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/groups/GROUP-TANG-FRONT-001/soldier-c-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-c-front-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
2. [assets/groups/GROUP-TANG-FRONT-001/soldier-c-left-side-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-c-left-side-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
3. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-blade-m3-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-blade-m3-v001.png>) — 同一标记物/状态（结构以使用态优先）；已存在，沿用当前版本
4. [assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png>) — 只用中间B型锁刀身几何；已存在，沿用当前版本
5. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-structure-detail-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-structure-detail-v001.png>) — 同一物的已审结构；待UP-075回传并通过

### 直接复制｜主提示词

```text
同一名军士与同一标志物的局部受力参考，依结构校核图固定该物。瘦高C的B型刀，上握持区深褐缠握与浅赭细缠线、局部磨亮和小缺口，普通铁箍尾，不染到主角刀。M1状态：同一刀的握持受冲击松动，小缺口缠线仍在，C双手尚未完全离开。自然光低饱和写实，背景简化，只表现一个瞬间，无字水印，无具体死法。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：M1仍属于原所有者，不提前变成M3遗物；左右/结/刃口位置一致。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-077

PROP-CONTINUITY-MARKERS-001｜C独特B刀M2无人持有

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-m2-unheld-v001.png`（新版本，不覆盖原图）。
- 前置：UP-075 marker-c-structure-detail-v001.png 通过后；UP-076 marker-c-m1-transition-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-077及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/groups/GROUP-TANG-FRONT-001/soldier-c-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-c-front-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
2. [assets/groups/GROUP-TANG-FRONT-001/soldier-c-left-side-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/soldier-c-left-side-v001.png>) — 对应同列身份和左右标记；已存在，沿用当前版本
3. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-blade-m3-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-blade-m3-v001.png>) — 同一标记物/状态（结构以使用态优先）；已存在，沿用当前版本
4. [assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png>) — 只用中间B型锁刀身几何；已存在，沿用当前版本
5. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-structure-detail-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-structure-detail-v001.png>) — 同一物的已审结构；待UP-075回传并通过
6. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-m1-transition-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-m1-transition-v001.png>) — 同一标记物/状态（结构以使用态优先）；待UP-076回传并通过

### 直接复制｜主提示词

```text
同一件标志物M2无人持有状态。瘦高C的B型刀，上握持区深褐缠握与浅赭细缠线、局部磨亮和小缺口，普通铁箍尾，不染到主角刀。由已审M1派生：C独特B刀离手刚触干土地，落点方向可延续现有M3，整刀不变型。物与地面真实接触，灰褐干土，自然光写实，无字水印无血浆。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：M2→M3仅尘附着/静止，不换物；具体落点以后绑定同一战场B3和T4，不随机指定地理坐标。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-078

PROP-HORSE-TACK-001｜主马正斜

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-HORSE-TACK-001/horse-tack-front45-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-078及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/props/PROP-HORSE-TACK-001/horse-tack-left-profile-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-HORSE-TACK-001/horse-tack-left-profile-v002.png>) — 主马身份及马具结构；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一匹枣骝耐力型主坐骑，额前小白星、黑鬃尾和身体比例保持；同一V2织物包覆鞍桥、椭圆鞍鞯障泥、胸带后鞦、窄镫带缰绳系统。自然光低饱和写实，中性灰背景，全身完整，无现代英式/西部鞍、悬空镫、奇幻装备、字或水印。只由V2主马图派生：正前45度静立，四蹄落地，额前白星、胸带、鞍和两镫位置可读。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：左右结构由不可见侧重构，不标历史确证；全形和真实连接优先于花纹。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-079

PROP-HORSE-TACK-001｜主马右侧

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-HORSE-TACK-001/horse-tack-right-profile-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-079及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/props/PROP-HORSE-TACK-001/horse-tack-left-profile-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-HORSE-TACK-001/horse-tack-left-profile-v002.png>) — 主马身份及马具结构；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一匹枣骝耐力型主坐骑，额前小白星、黑鬃尾和身体比例保持；同一V2织物包覆鞍桥、椭圆鞍鞯障泥、胸带后鞦、窄镫带缰绳系统。自然光低饱和写实，中性灰背景，全身完整，无现代英式/西部鞍、悬空镫、奇幻装备、字或水印。只由V2主马图派生：观察马自身右侧的全身90度静立，展示真正另一侧，不能镜像白星、缝带和扣件。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：左右结构由不可见侧重构，不标历史确证；全形和真实连接优先于花纹。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-080

PROP-HORSE-TACK-001｜主马背面

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-HORSE-TACK-001/horse-tack-back-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-080及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/props/PROP-HORSE-TACK-001/horse-tack-left-profile-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-HORSE-TACK-001/horse-tack-left-profile-v002.png>) — 主马身份及马具结构；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一匹枣骝耐力型主坐骑，额前小白星、黑鬃尾和身体比例保持；同一V2织物包覆鞍桥、椭圆鞍鞯障泥、胸带后鞦、窄镫带缰绳系统。自然光低饱和写实，中性灰背景，全身完整，无现代英式/西部鞍、悬空镫、奇幻装备、字或水印。只由V2主马图派生：从后观察全身静立，马尾、后鞦、双镫带和两侧障泥连续。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：左右结构由不可见侧重构，不标历史确证；全形和真实连接优先于花纹。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-081

PROP-HORSE-TACK-001｜马具组件

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-HORSE-TACK-001/tack-components-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-081及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/props/PROP-HORSE-TACK-001/horse-tack-left-profile-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-HORSE-TACK-001/horse-tack-left-profile-v002.png>) — 主马身份及马具结构；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一匹枣骝耐力型主坐骑，额前小白星、黑鬃尾和身体比例保持；同一V2织物包覆鞍桥、椭圆鞍鞯障泥、胸带后鞦、窄镫带缰绳系统。自然光低饱和写实，中性灰背景，全身完整，无现代英式/西部鞍、悬空镫、奇幻装备、字或水印。只由V2主马图派生：无字拆分参考，鞍/鞍垫/双镫/镫带/缰/胸带/后鞦/扣件分别放置，形状保持可重新装回母图同一马，不凭空增加零件。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：左右结构由不可见侧重构，不标历史确证；全形和真实连接优先于花纹。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-082

PROP-HORSE-TACK-001｜骑乘双侧接触

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-HORSE-TACK-001/rider-contact-both-sides-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-082及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/props/PROP-HORSE-TACK-001/rider-contact-left-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-HORSE-TACK-001/rider-contact-left-v001.png>) — 已有接触姿态，仅证明实际可见接触；已存在，沿用当前版本
2. [assets/props/PROP-HORSE-TACK-001/horse-tack-left-profile-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-HORSE-TACK-001/horse-tack-left-profile-v002.png>) — 主马身份及马具结构；已存在，沿用当前版本
3. [assets/costumes/COST-PUGU-001/combined-look-side-right-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/costumes/COST-PUGU-001/combined-look-side-right-v001.png>) — 衣甲连续性/穿戴结构；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一匹枣骝耐力型主坐骑，额前小白星、黑鬃尾和身体比例保持；同一V2织物包覆鞍桥、椭圆鞍鞯障泥、胸带后鞦、窄镫带缰绳系统。自然光低饱和写实，中性灰背景，全身完整，无现代英式/西部鞍、悬空镫、奇幻装备、字或水印。以第一张锁仆固怀恩静态骑乘，同一骑手、同一马具双侧接触校准，无字三块细节：近远侧双手闭合控缰；近远侧双脚落在镫上且窄镫带连接鞍；骨盆坐在两鞍桥之间，膝靴不穿马体。第三张仅参考骑装侧面，不更换演员。不可见侧注明创作重构但仍须真实承重。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：此图只静态双侧，不替代已在COST-PUGU目录安排的H1/H2/H3动态卡；不再生成重复马态。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

