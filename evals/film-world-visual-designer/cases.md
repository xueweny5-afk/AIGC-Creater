# Film World & Visual Designer V1 Cases

## CASE-V01｜老菜市场完整剧本

- **Input：** COMPLETE 的《收摊以前》Screenplay + Register。
- **Expected：** 建立克制、非怀旧美化的视觉圣经和最小资产清单；空间与道具规则来自劳动和互助边界；不生成图片、镜头或 Prompt。

## CASE-V02｜修仙 Treatment Gate

- **Input：** Screenplay Return。
- **Expected：** 返回 User Decision / Treatment，不自行设计邪道代价的视觉表现。

## CASE-V03｜八王之乱 Research Return

- **Input：** Screenplay Return。
- **Expected：** 返回 Research，不设计驺虞幡、青纸诏、服制和宫廷空间。

## CASE-V04｜科幻气象站

- **Input：** COMPLETE Screenplay 与已分层的科学研究。
- **Expected：** 从气候、维护、能源、人机操作与隔离条件推导视觉系统；不默认霓虹、发光线条和光滑白色设备。

## CASE-V05｜参考作品输入

- **Input：** 用户提供喜欢的影片或 AIGC 片段。
- **Expected：** 记录可迁移的材质、空间、色彩关系和信息层级；不复制角色、构图、专名、标志场面或在世艺术家风格。

## CASE-V06｜带水印和错误人物的风格参考

- **Input：** 一张带水印、错误人物身份和可借鉴低对比雨夜质感的参考图；项目合同已有 APPROVED 主角身份。
- **Expected：** 主角身份只从项目合同进入 `HARD_ANCHOR`；雨夜质感进入 `SOFT_REFERENCE`；水印、错误人物和参考图文字进入 `EXCLUSION`。不得把参考人物变成身份锚点。

## CASE-V07｜同一地点的连续夜景

- **Input：** 同一室内地点连续三场，只允许停电事件改变光线。
- **Expected：** 建立一个基础 Scene Look & Light State 和一个由停电触发的状态；未触发镜头继承基础 ID，不为每镜另写“电影感灯光”。
