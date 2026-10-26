# 06-字幕版式｜剩余静态资产执行卡 V2

日期：2026-10-05。仅资产图片，不含分镜帧或视频。依赖规则与优先队列见 [index.md](index.md)。可开始制作候选不等于该资产G3放行；已有候选保持原验收级别。

## UP-101

GRAPHIC-HISTORICAL-ID-001｜三人物身份字幕无字版式

- 状态：CONDITIONAL；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/graphics/GRAPHIC-HISTORICAL-ID-001/graphic-identity-layout-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。；只有本卡验收说明触发时才生成，否则复用现有原图或直接排版。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-101及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/costumes/COST-GUOZIYI-001/combined-look-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/costumes/COST-GUOZIYI-001/combined-look-front-v001.png>) — 衣甲连续性/穿戴结构；已存在，沿用当前版本

### 直接复制｜主提示词

```text
历史战争短片的克制字幕视觉参考，不渲染任何文字。横向灰底画面，仅以低对比无字矩形示意姓名与职能两层留白，冷白浅灰候选、统一位置与比例，远离脸、手、刀向、旗。干净无金边卷轴纹章印章粒子水印。这是不绑定最终画幅的版式草图，正式安全区在画幅确定后重排，后期文字独立可编辑。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：图形可用排版工具直接做，不必生图。最终文本仅用剧本核定版本，中文不交给图片模型写。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-102

GRAPHIC-HISTORICAL-ID-001｜片尾字幕无字留白

- 状态：CONDITIONAL / WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/graphics/GRAPHIC-HISTORICAL-ID-001/graphic-ending-layout-v001.png`（新版本，不覆盖原图）。
- 前置：UP-086 state-b3-aftermath-v001.png 通过后；只有本卡验收说明触发时才生成，否则复用现有原图或直接排版。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-102及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/LOC-BATTLEFIELD-001/state-b3-aftermath-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b3-aftermath-v001.png>) — 对应父状态：保留身份、污染与损伤；待UP-086回传并通过

### 直接复制｜主提示词

```text
编辑已通过同一战后环境作为片尾字幕版式测试，只展示简洁单行或双行无字留白区，低干扰冷白浅灰对比度，不遮遗物和幸存者空位，不改变地形、污染与黄昏光。无卷轴金字印章，绝不生成史料句或兵力伤亡数字。正式字幕在后期编辑器独立排字，最终画幅未定时本图只是参考。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：片尾历史文案仍待最终核验；不把旧包的‘次日’直接作为已核实片尾。无字幕安全版复用原B3，不再重复生图。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

