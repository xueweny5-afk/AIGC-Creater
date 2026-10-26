# Film Project Director Run｜发布结构主动询问

## Case A｜信息缺失

**User Input**

> 我想做各种宗门的 AIGC 修仙内容，有正道、邪道，也想表现不同宗门的规则。

**Expected Skill Response**

> 你希望先按哪种形式开发：单支短片、每集独立的系列短片，还是连续剧情剧集？

**Behavior Check**

- 只提出一个会改变项目架构的问题。
- 未同时询问时长、平台、画幅、集数或人物名单。
- 未生成完整 Project Brief。
- 未因“各种宗门”擅自推断为单元剧。

**Status：** PASS

## Case B｜用户确认共享世界单元短片

**User Input**

> 每集一个宗门故事，可以独立看，但世界和少数人物可以复用。集数还没想好。

**Expected Mapping**

- **Release Format：** [LOCKED · USER_FACT] Short-form Series
- **Series Architecture：** [LOCKED · USER_FACT] Shared World Episodes
- **Planned Count / Season Scope：** [OPEN] 待确定
- 不生成分集选题、季弧或每集故事。

**Status：** PASS

## Regression Found and Fixed

旧版《宗门志》Project Brief 曾把“多种宗门”推断为“系列化幻想短片”。已撤回该假设，将现有《山门内外》改为独立测试原型，并把最终 Release Format 与 Series Architecture 恢复为 `OPEN`。
