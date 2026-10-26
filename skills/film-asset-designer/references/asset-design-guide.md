# Asset Design Guide

## Minimum sufficient asset

先问下游究竟需要识别什么和从哪些角度复用，再决定资产规格。

- 仅一个正面静态出现的背景人物：可能只需单张身份参考。
- 跨镜复用人物：根据实际辨识需要先批准 Canonical Anchor，再派生必要角度/状态。露脸需要正面人脸；纯背影、剪影或抽象形象可先用体态/轮廓，不推定未知面部。
- 多套服装或明显状态变化：先锁定基础身份，再做独立状态板。
- 空间需要人物走动和反向观看：需要同一拓扑的正反向/平面关系参考。
- 关键道具会翻转、打开或被持用：需要关键可见面和尺度参考。

不要为了“完整”生成下游用不到的九宫格、大全套和装饰图。

View Matrix 的 Need / Source 回指剧本 Scene、动作、预计观看范围或风险，Required 写 REQUIRED / DEFERRED / NOT_REQUIRED；延期项注明启用条件。尚未设计机位时不要求先完成 Shot List，也不把未来可能用到的所有角度都设为 P0。后续机位新增需求再补对应视图并复核受影响依赖。

## Character and wardrobe dependency order

以下是依赖关系，不是每人必做的图数清单。按当前需求选取步骤；体态/轮廓足以辨识时使用 Canonical Anchor，不能因为跳过正脸就声称面部身份通过。

1. `Canonical Face`：正面人脸特写，平视、无表情、无遮挡、均匀中性光和简单背景。
2. `Head Angles`：按需要选择角度，从确切批准的 Canonical Face 逐张编辑派生。
3. `Body Identity`：中性站姿、稳定体态比例和基础内层，不让正式服装反向定义人物身份。
4. `Body Views`：只做必要观看方向；确需六视图时可用正面、左前 45°、左侧、背面、右侧、右前 45°，每个角度独立原图。
5. `Costume / Makeup-Hair`：版型、层次、穿戴、发型和妆容单独建资产与版本。
6. `Combined Look`：绑定 Character、Costume、Makeup/Hair 的批准版本，验证当前所需可见面；未验证的方向不自动可用。
7. `Detail Plates`：脸部识别点、皮肤/头发、布料织纹、缝线、金属、皮革、磨损、配饰和剧情需要的手部细节。

Contact Sheet 从已批准独立原图排版生成，只用于整体审阅。不要在一个多格生成中让模型同时重新发明六个身份。

所有资产按用途确定规格，不把“非全套”视作质量降级；必要视图缺失必须补足，未用视图可延期。

## Usability and artistic rules

从 Visual Bible 继承 Rule / State IDs、Observable Acceptance、Presentation Mode 和 Artistic Rule IDs。按实际用途看人物比例/识别、服装层次与合体、道具尺度/持用逻辑、场景出入口与固定锚点；远景身份参考不能证明细节接触或近景材料已合格。

PHYSICAL / MIXED 的物理层检查合理结构与材料，STYLIZED 的有意形变、绘画平面感和非物理效果按批准艺术规则及内部连续性审核。中性参考保留媒介，不强制摄影写实。批准范围外的随机漂移不能借艺术模式放行；物理空气与象征形态仍分开。资产可证明身份、结构和必要静态持用，完整多人互动、镜头构图与动态效果分别留到 Storyboard / Motion / Generation / QC。

## Scoped approval

Approval Scope 列明确切文件、版本、用途、视图和状态；Unverified / Deferred Use 列未验证用途。正脸批准不代表背面、表情变化、服装合体或所有角度通过。新用途超出旧范围时创建待验证的扩展版本/视图，保留已批准母版；当前生产关口检查所需范围的实际覆盖，不只看资产名旁的 APPROVED。

用户对确切图片明确批准时按其范围记录 USER-APPROVED，不重复审核，也不把未评估维度写成 PASS。PLAN_ONLY/HANDOFF 的验收点是待验证计划；内容交付不要求先收媒体，生产级依赖仍须真实批准证据。

## Decision gates

高影响 OPEN 字段包括：

- 人物年龄层、性别呈现、文化/族群身份和非人解剖；
- 服装所属时代、身份等级、宗教或制度含义；
- 历史建筑、器物与文字形制；
- 核心场景拓扑和关键道具功能。

这些字段不能通过多抽几张图来决定。先提出一个最上游问题；同时可以推进不依赖该决定的资产。

## Prompt compilation

实际生成时从合同编译提示词：资产目的 → derivation parent → locked features → required view/state → materials/geometry → neutral presentation → negative constraints。不要从风格词开始，也不要复制 Visual Bible 全文。

平台语法、模型名、种子、尺寸和参考图权重只存在 generation log；换模型时不能改变合同。

## Review loop

1. 生成最小样本。
2. 实际查看原图。
3. 先判断身份与结构，再判断审美。
4. 只针对失败字段返工；跨视图漂移返回 locked features 或主参考，不堆叠无关风格词。
5. 保留未采用版本的状态，不覆盖已批准资产。

## Rights and originality

- 记录用户参考图的来源和允许用途。
- 不复刻现有影视/游戏角色、宗门、道具或标志性场景。
- 用户提出某位在世艺术家的风格时，转译为可描述的媒介、材质、色彩、形状和空间品质。
- 真实人物或可识别肖像需要明确授权范围。

## Self-audit

- 所需视图和状态是否有剧本、动作、预计可见方向或连续性风险依据，未需要部分是否标明 DEFERRED / NOT_REQUIRED？
- 是否把 OPEN 身份交给模型随机决定？
- 是否把 presentation choice 锁成 identity？
- 是否检查真实像素而非只看提示词？
- 是否把 PLAN 当作 GENERATED 或 APPROVED？
- 是否在失败时只修正相关字段？
- 是否误生成了镜头图或视频 Prompt？
