# 05-空间材质空气｜剩余静态资产执行卡 V2

日期：2026-10-05。仅资产图片，不含分镜帧或视频。依赖规则与优先队列见 [index.md](index.md)。可开始制作候选不等于该资产G3放行；已有候选保持原验收级别。

## UP-083

LOC-BATTLEFIELD-001｜B0地表重复纹理返工

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-083及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/LOC-BATTLEFIELD-001/topology-plan-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/topology-plan-v002.png>) — 地形/空间拓扑；已存在，沿用当前版本
2. [assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png>) — 只读制作分区和世界朝向，不复制标注；已存在，沿用当前版本
3. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一香积寺题材战场的制作空间重构，不是历史测绘。拓扑图锁地形，A前军初位、B追击走廊、C中军、D退路重组、E推进、F东侧骑兵通道、G原地战后；工作地图上方为燕军方向、下方为唐军后方、右侧为制作东翼。黄褐灰褐干土地、碎石、稀疏草根、轻微起伏保留，不能重建成别处地形。自然光低饱和写实，无烟雾无字水印、寺塔城墙沙丘现代道路或新增辎重车辆。空间状态图使用清洁空气，以免尘层掩盖地形。第一张锁连续地形，第二张只读分区关系，不复制分区线文字，第三张只锁材料。选择能复现原阵位A与追击走廊B的固定高机位校准视角，保留地平线、石草和道路锚点。战前土面只有少量不规则旧足迹，大片原生压实土；杜绝规则重复环圈、密集循环马蹄印、均匀瓦片纹、纹理克隆。无遗物和损坏旗，仅少量完整旗杆供尺度。固定本张机位用于B1/B2/B3。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：V1/V2/V3都因循环纹理未通过，不引用为合格母图；先100%查看干土纹理再放行。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-084

LOC-BATTLEFIELD-001｜B1溃乱地表

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b1-rout-v001.png`（新版本，不覆盖原图）。
- 前置：UP-083 state-b0-prebattle-v004.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-084及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png>) — 对应父状态：保留身份、污染与损伤；待UP-083回传并通过
2. [assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png>) — 对应父状态：保留身份、污染与损伤；待UP-083回传并通过
3. [assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png>) — 只读制作分区和世界朝向，不复制标注；已存在，沿用当前版本
4. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一香积寺题材战场的制作空间重构，不是历史测绘。拓扑图锁地形，A前军初位、B追击走廊、C中军、D退路重组、E推进、F东侧骑兵通道、G原地战后；工作地图上方为燕军方向、下方为唐军后方、右侧为制作东翼。黄褐灰褐干土地、碎石、稀疏草根、轻微起伏保留，不能重建成别处地形。自然光低饱和写实，无烟雾无字水印、寺塔城墙沙丘现代道路或新增辎重车辆。空间状态图使用清洁空气，以免尘层掩盖地形。按顺序引用上一状态、B0机位、分区及土材质；当前唯一变化：只沿原追击路径增加不规则足迹、单蹄凹印、滑痕、一面倒旗和少量遗兵；固定石草和地形不动，非整地均匀印花。没有角色战斗表演，不生成正式镜头关键帧。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：叠看B0核对石草路位/地平线；B3落点待与T0→T4联合审核，不宣称单个空环境已证明伤亡。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-085

LOC-BATTLEFIELD-001｜B2推进地表

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b2-advance-v001.png`（新版本，不覆盖原图）。
- 前置：UP-084 state-b1-rout-v001.png 通过后；UP-083 state-b0-prebattle-v004.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-085及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/LOC-BATTLEFIELD-001/state-b1-rout-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b1-rout-v001.png>) — 对应父状态：保留身份、污染与损伤；待UP-084回传并通过
2. [assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png>) — 对应父状态：保留身份、污染与损伤；待UP-083回传并通过
3. [assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png>) — 只读制作分区和世界朝向，不复制标注；已存在，沿用当前版本
4. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一香积寺题材战场的制作空间重构，不是历史测绘。拓扑图锁地形，A前军初位、B追击走廊、C中军、D退路重组、E推进、F东侧骑兵通道、G原地战后；工作地图上方为燕军方向、下方为唐军后方、右侧为制作东翼。黄褐灰褐干土地、碎石、稀疏草根、轻微起伏保留，不能重建成别处地形。自然光低饱和写实，无烟雾无字水印、寺塔城墙沙丘现代道路或新增辎重车辆。空间状态图使用清洁空气，以免尘层掩盖地形。按顺序引用上一状态、B0机位、分区及土材质；当前唯一变化：承接B1痕迹，只沿原推进轴增加重叠脚印、拖痕、少量碎甲；光线转较低的下午自然光，但地形和污染来源不变。没有角色战斗表演，不生成正式镜头关键帧。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：叠看B0核对石草路位/地平线；B3落点待与T0→T4联合审核，不宣称单个空环境已证明伤亡。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-086

LOC-BATTLEFIELD-001｜B3战后原地

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b3-aftermath-v001.png`（新版本，不覆盖原图）。
- 前置：UP-085 state-b2-advance-v001.png 通过后；UP-083 state-b0-prebattle-v004.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-086及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/LOC-BATTLEFIELD-001/state-b2-advance-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b2-advance-v001.png>) — 对应父状态：保留身份、污染与损伤；待UP-085回传并通过
2. [assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png>) — 对应父状态：保留身份、污染与损伤；待UP-083回传并通过
3. [assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png>) — 只读制作分区和世界朝向，不复制标注；已存在，沿用当前版本
4. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本
5. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-helmet-m3-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-helmet-m3-v001.png>) — 同一标记物/状态（结构以使用态优先）；已存在，沿用当前版本
6. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-cloth-m3-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-b-cloth-m3-v002.png>) — 同一标记物/状态（结构以使用态优先）；已存在，沿用当前版本
7. [assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-blade-m3-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/props/PROP-CONTINUITY-MARKERS-001/marker-c-blade-m3-v001.png>) — 同一标记物/状态（结构以使用态优先）；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一香积寺题材战场的制作空间重构，不是历史测绘。拓扑图锁地形，A前军初位、B追击走廊、C中军、D退路重组、E推进、F东侧骑兵通道、G原地战后；工作地图上方为燕军方向、下方为唐军后方、右侧为制作东翼。黄褐灰褐干土地、碎石、稀疏草根、轻微起伏保留，不能重建成别处地形。自然光低饱和写实，无烟雾无字水印、寺塔城墙沙丘现代道路或新增辎重车辆。空间状态图使用清洁空气，以免尘层掩盖地形。按顺序引用上一状态、B0机位、分区及土材质；当前唯一变化：承接B2全部地表痕迹，使用B0原机位焦段地平线与石草，完整旗杆变折断，原列队区变明显空疏；三件遗物按各自此前退出方向分区，不集中摆成陈列，残破程度克制；黄昏自然弱光，清洁空气显示结构。没有角色战斗表演，不生成正式镜头关键帧。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：叠看B0核对石草路位/地平线；B3落点待与T0→T4联合审核，不宣称单个空环境已证明伤亡。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-087

LOC-BATTLEFIELD-001｜唐前军朝燕军方向

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/overview-tang-front-to-yan-v001.png`（新版本，不覆盖原图）。
- 前置：UP-083 state-b0-prebattle-v004.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-087及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/LOC-BATTLEFIELD-001/topology-plan-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/topology-plan-v002.png>) — 地形/空间拓扑；已存在，沿用当前版本
2. [assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png>) — 只读制作分区和世界朝向，不复制标注；已存在，沿用当前版本
3. [assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png>) — 对应父状态：保留身份、污染与损伤；待UP-083回传并通过

### 直接复制｜主提示词

```text
同一香积寺题材战场的制作空间重构，不是历史测绘。拓扑图锁地形，A前军初位、B追击走廊、C中军、D退路重组、E推进、F东侧骑兵通道、G原地战后；工作地图上方为燕军方向、下方为唐军后方、右侧为制作东翼。黄褐灰褐干土地、碎石、稀疏草根、轻微起伏保留，不能重建成别处地形。自然光低饱和写实，无烟雾无字水印、寺塔城墙沙丘现代道路或新增辎重车辆。空间状态图使用清洁空气，以免尘层掩盖地形。从同一拓扑和已通过B0派生一个环境关系校准视角：由工作图A位向上方燕军方向看，前景A中景B远景敌阵方向，固定地标与旗尺度延续。只转观察方向，不创造新山地城墙。工作地图画面右侧才代表东翼，其他视角须用地标投影辨方向；不可见部分仅作与拓扑相容的创作补全，不伪装为参考图已证明的空间。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：正反向按世界方向而非屏幕左右；三个角度若拓扑冲突退回本图局部修订。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-088

LOC-BATTLEFIELD-001｜追击走廊反看唐军后方

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/overview-pursuit-to-tang-rear-v001.png`（新版本，不覆盖原图）。
- 前置：UP-083 state-b0-prebattle-v004.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-088及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/LOC-BATTLEFIELD-001/topology-plan-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/topology-plan-v002.png>) — 地形/空间拓扑；已存在，沿用当前版本
2. [assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png>) — 只读制作分区和世界朝向，不复制标注；已存在，沿用当前版本
3. [assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png>) — 对应父状态：保留身份、污染与损伤；待UP-083回传并通过

### 直接复制｜主提示词

```text
同一香积寺题材战场的制作空间重构，不是历史测绘。拓扑图锁地形，A前军初位、B追击走廊、C中军、D退路重组、E推进、F东侧骑兵通道、G原地战后；工作地图上方为燕军方向、下方为唐军后方、右侧为制作东翼。黄褐灰褐干土地、碎石、稀疏草根、轻微起伏保留，不能重建成别处地形。自然光低饱和写实，无烟雾无字水印、寺塔城墙沙丘现代道路或新增辎重车辆。空间状态图使用清洁空气，以免尘层掩盖地形。从同一拓扑和已通过B0派生一个环境关系校准视角：由工作图B回望下方唐后方，空间顺序对应A/D/C；真正反向时制作东翼投影通常在画面左边，不强迫所有视角东翼在画面右边。只转观察方向，不创造新山地城墙。工作地图画面右侧才代表东翼，其他视角须用地标投影辨方向；不可见部分仅作与拓扑相容的创作补全，不伪装为参考图已证明的空间。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：正反向按世界方向而非屏幕左右；三个角度若拓扑冲突退回本图局部修订。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-089

LOC-BATTLEFIELD-001｜制作东翼走廊

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/overview-east-corridor-v001.png`（新版本，不覆盖原图）。
- 前置：UP-083 state-b0-prebattle-v004.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-089及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/LOC-BATTLEFIELD-001/topology-plan-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/topology-plan-v002.png>) — 地形/空间拓扑；已存在，沿用当前版本
2. [assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png>) — 只读制作分区和世界朝向，不复制标注；已存在，沿用当前版本
3. [assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png>) — 对应父状态：保留身份、污染与损伤；待UP-083回传并通过

### 直接复制｜主提示词

```text
同一香积寺题材战场的制作空间重构，不是历史测绘。拓扑图锁地形，A前军初位、B追击走廊、C中军、D退路重组、E推进、F东侧骑兵通道、G原地战后；工作地图上方为燕军方向、下方为唐军后方、右侧为制作东翼。黄褐灰褐干土地、碎石、稀疏草根、轻微起伏保留，不能重建成别处地形。自然光低饱和写实，无烟雾无字水印、寺塔城墙沙丘现代道路或新增辎重车辆。空间状态图使用清洁空气，以免尘层掩盖地形。从同一拓扑和已通过B0派生一个环境关系校准视角：观察工作地图右侧F通道及其与主轴连接，能解释绕向侧后和切入，不改变通道入口出口。只转观察方向，不创造新山地城墙。工作地图画面右侧才代表东翼，其他视角须用地标投影辨方向；不可见部分仅作与拓扑相容的创作补全，不伪装为参考图已证明的空间。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：正反向按世界方向而非屏幕左右；三个角度若拓扑冲突退回本图局部修订。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-090

LOC-BATTLEFIELD-001｜地表尺度细节

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/detail-ground-system-v001.png`（新版本，不覆盖原图）。
- 前置：UP-083 state-b0-prebattle-v004.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-090及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本
2. [assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v004.png>) — 对应父状态：保留身份、污染与损伤；待UP-083回传并通过

### 直接复制｜主提示词

```text
同一干土地表校准近景：原生压实土与少量松土边界、随机碎石、稀疏草根；一只军靴印和一枚单蹄凹印用于尺度，间隔不规则。材料以第一张、环境以第二张，真实自然光粗粝写实，非循环无缝贴图。无文字水印无考古测量精确宣称，无整地密集印花。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：印痕有单个来源和尺寸，不让环圈微纹理回归。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-091

MAT-BATTLEFIELD-001｜织物汗湿可读性条件返工

- 状态：CONDITIONAL；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-military-textile-v003.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。；只有本卡验收说明触发时才生成，否则复用现有原图或直接排版。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-091及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/MAT-BATTLEFIELD-001/material-military-textile-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-military-textile-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
只校正同一灰褐军用织物材料板的汗湿可读性。干态与汗湿态并列，保留同一织纹颜色与粗糙度；汗湿仅在肘内或腋下实际接触区形成深色边界，不均匀浸透，不发亮成塑料，也不添装饰花纹。自然光写实无文字水印，能清楚区分干态、汗湿态和干尘态。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：现有V2为条件候选；若原图放大与对比已够清楚，不必生成V3。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-092

MAT-BATTLEFIELD-001｜五材料三时段受光

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-light-response-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-092及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本
2. [assets/locations/MAT-BATTLEFIELD-001/material-dark-metal-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-dark-metal-v001.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本
3. [assets/locations/MAT-BATTLEFIELD-001/material-military-textile-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-military-textile-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本
4. [assets/locations/MAT-BATTLEFIELD-001/material-leather-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-leather-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本
5. [assets/locations/MAT-BATTLEFIELD-001/material-wood-grip-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-wood-grip-v001.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一五类材料（干土、暗铁、灰褐织物、旧皮革、粗木柄）在三栏自然受光的对照参考：午后浅灰散射光、推进阶段较低斜向光、战后黄昏冷弱光。各行材料、粗糙度、颜色、尘汗量完全固定，只变光源方向强弱，不加金色薄雾和全局灰滤镜。保持暗铁窄高光与布皮木不同反射，无文字水印，不让亮度变化误变材料。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：对照Visual Bible受光；三时段不造第二套材料。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-093

MAT-BATTLEFIELD-001｜尘土局部附着

- 状态：READY_FOR_CANDIDATE；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-dust-interaction-v001.png`（新版本，不覆盖原图）。
- 前置：参考文件已存在；先按列明用途核对原图，已有明确批准的范围保持冻结。
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-093及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本
2. [assets/locations/MAT-BATTLEFIELD-001/material-dark-metal-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-dark-metal-v001.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本
3. [assets/locations/MAT-BATTLEFIELD-001/material-military-textile-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-military-textile-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本
4. [assets/locations/MAT-BATTLEFIELD-001/material-leather-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-leather-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本
5. [assets/locations/MAT-BATTLEFIELD-001/material-wood-grip-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-wood-grip-v001.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
五类现有战场材料与人物汗区的局部尘附着校准板：靴边下缘、织物下摆与褶皱、甲片凹处、皮革弯折扣缝、木柄握缠纹理、皮肤局部汗区分别有少量真实干尘；各旁保留未受尘区。土颜色同母图，汗与尘边界非均匀涂抹；金属刃面不厚糊，皮革木柄不塑料光。自然光低饱和写实无文字水印。
```

### 参数与验收（不要复制）

- 建议比例 3:2，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：只有接触/暴露处增尘，不全身泛黄；不将此材料板冒充气溶胶空气参考。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-094

ENV-ATMOSPHERE-001｜ATM-BF-ROUT-AFTERNOON-V1

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/ENV-ATMOSPHERE-001/atm-02-rout-dust-v001.png`（新版本，不覆盖原图）。
- 前置：UP-084 state-b1-rout-v001.png 通过后；UP-035 state-t1-separated-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-094及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/LOC-BATTLEFIELD-001/state-b1-rout-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b1-rout-v001.png>) — 对应父状态：保留身份、污染与损伤；待UP-084回传并通过
2. [assets/groups/GROUP-TANG-FRONT-001/state-t1-separated-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/state-t1-separated-v001.png>) — 对应父状态：保留身份、污染与损伤；待UP-035回传并通过
3. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一战场空气校准图，尘土仅来自脚步、马蹄、滑动、碰撞，源头与扩散路径可见，稀密不均并沉降。脸、刀向、旗与空位保持可读。低饱和自然光、无字水印、无烟雾蒸汽雨白马气和金色自发光粒子，无全局电影雾。不得把空气转清解释成衣甲自动干净。第一张锁指定空间、其后锁角色群体或远尘方向，地材只锁干尘颜色。仅增加当前空气层与对应尘源，不改变地形或演员：午后，少量奔跑靴与蹄作为尘源，尘从地至膝、碰撞局部短脉冲到腰胸，其他空间清，人物不变。这是材质空气校准资产，不是正式剧情帧。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：核对源/高度/范围/沉降；先通过上游空间及群体再执行，不用烟雾掩盖身份或重复纹理。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-095

ENV-ATMOSPHERE-001｜ATM-CENTER-HOLD-AFTERNOON-V1

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/ENV-ATMOSPHERE-001/atm-03-center-hold-v001.png`（新版本，不覆盖原图）。
- 前置：UP-088 overview-pursuit-to-tang-rear-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-095及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/LOC-BATTLEFIELD-001/overview-pursuit-to-tang-rear-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/overview-pursuit-to-tang-rear-v001.png>) — 对应身份角度或上一状态，用途以主提示词限定；待UP-088回传并通过
2. [assets/costumes/COST-GUOZIYI-001/state-g1-light-dust-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/costumes/COST-GUOZIYI-001/state-g1-light-dust-v001.png>) — 对应父状态：保留身份、污染与损伤；已存在，沿用当前版本
3. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一战场空气校准图，尘土仅来自脚步、马蹄、滑动、碰撞，源头与扩散路径可见，稀密不均并沉降。脸、刀向、旗与空位保持可读。低饱和自然光、无字水印、无烟雾蒸汽雨白马气和金色自发光粒子，无全局电影雾。不得把空气转清解释成衣甲自动干净。第一张锁指定空间、其后锁角色群体或远尘方向，地材只锁干尘颜色。仅增加当前空气层与对应尘源，不改变地形或演员：午后中军前景清，郭子仪与旗旁不满尘，前军方向远处只有低密度低对比尘带，脸只原有轻尘。这是材质空气校准资产，不是正式剧情帧。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：核对源/高度/范围/沉降；先通过上游空间及群体再执行，不用烟雾掩盖身份或重复纹理。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-096

ENV-ATMOSPHERE-001｜ATM-FRONT-REGROUP-AFTERNOON-V1

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/ENV-ATMOSPHERE-001/atm-04-regroup-v001.png`（新版本，不覆盖原图）。
- 前置：UP-084 state-b1-rout-v001.png 通过后；UP-036 state-t2-regroup-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-096及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/LOC-BATTLEFIELD-001/state-b1-rout-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b1-rout-v001.png>) — 对应父状态：保留身份、污染与损伤；待UP-084回传并通过
2. [assets/groups/GROUP-TANG-FRONT-001/state-t2-regroup-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/state-t2-regroup-v001.png>) — 对应父状态：保留身份、污染与损伤；待UP-036回传并通过
3. [assets/costumes/COST-LISIYE-001/state-l1-open-front-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/costumes/COST-LISIYE-001/state-l1-open-front-v001.png>) — 对应父状态：保留身份、污染与损伤；已存在，沿用当前版本
4. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一战场空气校准图，尘土仅来自脚步、马蹄、滑动、碰撞，源头与扩散路径可见，稀密不均并沉降。脸、刀向、旗与空位保持可读。低饱和自然光、无字水印、无烟雾蒸汽雨白马气和金色自发光粒子，无全局电影雾。不得把空气转清解释成衣甲自动干净。第一张锁指定空间、其后锁角色群体或远尘方向，地材只锁干尘颜色。仅增加当前空气层与对应尘源，不改变地形或演员：午后残低尘沉降，停步回身碰撞处短时二次扬尘，腰上清；李嗣业轮廓和敞开汗尘清楚。这是材质空气校准资产，不是正式剧情帧。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：核对源/高度/范围/沉降；先通过上游空间及群体再执行，不用烟雾掩盖身份或重复纹理。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-097

ENV-ATMOSPHERE-001｜ATM-FRONT-ADVANCE-LATEAFTERNOON-V1

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/ENV-ATMOSPHERE-001/atm-05-front-advance-v001.png`（新版本，不覆盖原图）。
- 前置：UP-085 state-b2-advance-v001.png 通过后；UP-037 state-t3-attrition-a-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-097及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/LOC-BATTLEFIELD-001/state-b2-advance-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b2-advance-v001.png>) — 对应父状态：保留身份、污染与损伤；待UP-085回传并通过
2. [assets/groups/GROUP-TANG-FRONT-001/state-t3-attrition-a-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/state-t3-attrition-a-v001.png>) — 对应父状态：保留身份、污染与损伤；待UP-037回传并通过
3. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一战场空气校准图，尘土仅来自脚步、马蹄、滑动、碰撞，源头与扩散路径可见，稀密不均并沉降。脸、刀向、旗与空位保持可读。低饱和自然光、无字水印、无烟雾蒸汽雨白马气和金色自发光粒子，无全局电影雾。不得把空气转清解释成衣甲自动干净。第一张锁指定空间、其后锁角色群体或远尘方向，地材只锁干尘颜色。仅增加当前空气层与对应尘源，不改变地形或演员：下午较低自然光，队列脚步沿推进轴产生近地到腰的间歇尘带，尘间有空隙头部清，人数减少不反而增满天尘。这是材质空气校准资产，不是正式剧情帧。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：核对源/高度/范围/沉降；先通过上游空间及群体再执行，不用烟雾掩盖身份或重复纹理。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-098

ENV-ATMOSPHERE-001｜ATM-EAST-CAVALRY-LATEAFTERNOON-V1

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/ENV-ATMOSPHERE-001/atm-06-east-cavalry-v001.png`（新版本，不覆盖原图）。
- 前置：UP-089 overview-east-corridor-v001.png 通过后；UP-044 state-u2-accelerate-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-098及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/LOC-BATTLEFIELD-001/overview-east-corridor-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/overview-east-corridor-v001.png>) — 对应身份角度或上一状态，用途以主提示词限定；待UP-089回传并通过
2. [assets/groups/GROUP-UYGHUR-CAV-001/state-u2-accelerate-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-UYGHUR-CAV-001/state-u2-accelerate-v001.png>) — 对应父状态：保留身份、污染与损伤；待UP-044回传并通过
3. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一战场空气校准图，尘土仅来自脚步、马蹄、滑动、碰撞，源头与扩散路径可见，稀密不均并沉降。脸、刀向、旗与空位保持可读。低饱和自然光、无字水印、无烟雾蒸汽雨白马气和金色自发光粒子，无全局电影雾。不得把空气转清解释成衣甲自动干净。第一张锁指定空间、其后锁角色群体或远尘方向，地材只锁干尘颜色。仅增加当前空气层与对应尘源，不改变地形或演员：下午较低自然光，同一骑队尘尾仅在蹄后沿已完成转向的弧线，领骑前方和敌我方向清楚，不加沙暴。这是材质空气校准资产，不是正式剧情帧。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：核对源/高度/范围/沉降；先通过上游空间及群体再执行，不用烟雾掩盖身份或重复纹理。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-099

ENV-ATMOSPHERE-001｜ATM-FRONT-TURN-DUSK-V1

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/ENV-ATMOSPHERE-001/atm-07-front-turn-v001.png`（新版本，不覆盖原图）。
- 前置：UP-085 state-b2-advance-v001.png 通过后；UP-098 atm-06-east-cavalry-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-099及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/LOC-BATTLEFIELD-001/state-b2-advance-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b2-advance-v001.png>) — 对应父状态：保留身份、污染与损伤；待UP-085回传并通过
2. [assets/locations/ENV-ATMOSPHERE-001/atm-06-east-cavalry-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/ENV-ATMOSPHERE-001/atm-06-east-cavalry-v001.png>) — 对应身份角度或上一状态，用途以主提示词限定；待UP-098回传并通过
3. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一战场空气校准图，尘土仅来自脚步、马蹄、滑动、碰撞，源头与扩散路径可见，稀密不均并沉降。脸、刀向、旗与空位保持可读。低饱和自然光、无字水印、无烟雾蒸汽雨白马气和金色自发光粒子，无全局电影雾。不得把空气转清解释成衣甲自动干净。第一张锁指定空间、其后锁角色群体或远尘方向，地材只锁干尘颜色。仅增加当前空气层与对应尘源，不改变地形或演员：黄昏，前军近处低残尘下降，制作东翼远处另有独立骑兵尘带，两尘源方向不同，不能合成一片雾。这是材质空气校准资产，不是正式剧情帧。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：核对源/高度/范围/沉降；先通过上游空间及群体再执行，不用烟雾掩盖身份或重复纹理。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

---

## UP-100

ENV-ATMOSPHERE-001｜ATM-FRONT-AFTERMATH-DUSK-V1

- 状态：WAITING_DEPENDENCY；平台能力：MODEL VERIFICATION REQUIRED。
- 目标：`D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/ENV-ATMOSPHERE-001/atm-08-aftermath-v001.png`（新版本，不覆盖原图）。
- 前置：UP-086 state-b3-aftermath-v001.png 通过后；UP-039 state-t4-empty-spaces-v001.png 通过后
- 操作：确认前置 → 选支持参考图的图片编辑／生成入口 → 按下列编号上传 → 设建议比例（平台允许时）→ 只复制主提示词 → 保存原文件 → 回传UP-100及模型/参数（已知时）；未明确说“审核通过”时进入图片审核。

### 参考图上传顺序与用途

1. [assets/locations/LOC-BATTLEFIELD-001/state-b3-aftermath-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/LOC-BATTLEFIELD-001/state-b3-aftermath-v001.png>) — 对应父状态：保留身份、污染与损伤；待UP-086回传并通过
2. [assets/groups/GROUP-TANG-FRONT-001/state-t4-empty-spaces-v001.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/groups/GROUP-TANG-FRONT-001/state-t4-empty-spaces-v001.png>) — 对应父状态：保留身份、污染与损伤；待UP-039回传并通过
3. [assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png>) — 仅材质或受光，不改身份/几何；已存在，沿用当前版本

### 直接复制｜主提示词

```text
同一战场空气校准图，尘土仅来自脚步、马蹄、滑动、碰撞，源头与扩散路径可见，稀密不均并沉降。脸、刀向、旗与空位保持可读。低饱和自然光、无字水印、无烟雾蒸汽雨白马气和金色自发光粒子，无全局电影雾。不得把空气转清解释成衣甲自动干净。第一张锁指定空间、其后锁角色群体或远尘方向，地材只锁干尘颜色。仅增加当前空气层与对应尘源，不改变地形或演员：黄昏无人继续奔跑，只剩低位细尘及凹处沉降，没有新尘源；遗物幸存者空位清晰，衣甲延续污损无欢呼。这是材质空气校准资产，不是正式剧情帧。
```

### 参数与验收（不要复制）

- 建议比例 16:9，每次1张；平台支持时采用高质量原尺寸。主体全形不裁刀柄、马蹄和双脚；具体尺寸、参考图数量上限、局部编辑能力、负向栏待实际平台核实，不编造参数。
- 主提示词已包含排除约束；没有独立负向栏时不另拼接模型语法。
- 验收：核对源/高度/范围/沉降；先通过上游空间及群体再执行，不用烟雾掩盖身份或重复纹理。
- 失败：仅返工本卡及真正受影响的下游；另存下一版本，不覆盖或自动晋升Canon。

