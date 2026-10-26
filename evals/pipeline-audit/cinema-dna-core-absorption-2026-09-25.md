# Cinema DNA Core Absorption Regression

**Scope:** 验证从外部材料提炼的故事合同、空间证据、实体状态、镜头依赖、输入帧角色、批准版本保护和局部返工能力。测试方法，不复制外部仓库的固定画幅、三镜头模板、文案或脚本。

## Case 1 — 安静的人文故事不被强行改写

**Input:** 老菜市场最后一天，原始材料只有摊主整理物品、熟客告别和卷帘门落下。

**Expected:**

- Story Blueprint 建立 `OSC-###`，保留三个原始锚点；
- 可以把锚点拆成原因、行动、结果，但不新增盗窃、冲突、牺牲或反转；
- 每个 Must Be Visible 映射到 Story Movement。

## Case 2 — 单张场景图的未知背面

**Input:** 只有店铺正面图，提议摄影机绕到柜台背后并拍门后空间。

**Expected:**

- Scene 标记正面为 `VISIBLE`、部分邻接关系为 `INFERRED`、门后为 `UNKNOWN`；
- Shot 不把反向空间标为 READY，返回补充资产或收敛机位；
- 不用“画面左边”替代世界坐标。

## Case 3 — 同一封信的交接

**Input:** 甲把唯一一封信交给乙，后镜由乙打开。

**Expected:**

- 实体使用稳定 ID，数量始终为 1；
- 状态链证明甲释放、乙获得同一实体；
- 交接镜头为 `STATE-CHANGE CRITICAL`，打开信件镜头依赖它；
- 关键帧或 Take 通过后才填写 `Actual Observation`。

## Case 4 — 中间动作帧进入图生视频

**Input:** 输入图中人物已经把剑拔出一半。

**Expected:**

- Motion 标记输入为 `MID`；
- 动作从半拔状态继续到出鞘或停住，不重新从剑在鞘中开始；
- Prompt Adapter 描述当前帧之后的运动；
- Planned Duration 与模型 Generation Duration 分开记录。

## Case 5 — 风格帧包含过期道具

**Input:** 已批准画面只用于水墨风格，但人物手里拿着后续已经交出的旧道具。

**Expected:**

- Approval Scope 为 `STYLE ONLY`；
- Prompt 引用其媒介、线条、色块或光线组织，不继承旧道具状态；
- 身份和当前状态重新锚定原始资产与最新合同，不只链式参考上一张生成图。

## Case 6 — 一镜失败，不重做整场

**Input:** 九个镜头中，交接镜头生成出两封信；其余六个无依赖镜头已通过，两个后续镜头依赖交接结果。

**Expected:**

- QC 记录实体数量错误和可见证据；
- 只返工交接镜头，并将两个 dependents 标为待复核；
- 六个无依赖通过镜头保持 `FROZEN_APPROVED`；
- 不覆盖旧 Take，不宣称文本修正等于运动已验证。

## Acceptance

- 所有相关 Skill 通过 `quick_validate.py`；
- 模板字段能够承载上述六个案例；
- 没有新增固定画幅、固定镜头数、固定景别配额或未经授权的生成动作；
- 既有项目文件不被批量迁移或覆盖，新字段从下一版本交付物开始使用。
