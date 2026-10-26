# Film Shot Director V1 Cases

## CASE-SH01｜老菜市场 S005 Ready Fixture

- **Input：** `fixtures/ready-s005-scene-design.md`。
- **Expected：** 完整覆盖停住—看见—允许—跨界—收摊；固定世界坐标和轴线；时长闭合；不加入和解表演；不输出图或 Prompt。

## CASE-SH02｜资产待定 Scene Pack

- **Input：** `film-scene-director/outputs/emotional-old-market-scene-design-pack.md`，状态 DRAFT_ASSET_PENDING。
- **Expected：** 返回 Asset Decision，不生成生产级 Shot List。

## CASE-SH03｜历史场景 Return

- **Expected：** 继承 Research Return，不用摄影术语掩盖缺失的历史空间和调度依据。

## CASE-SH04｜复杂运动

- **Expected：** 每次运动包含起点、触发、路径、主体关系、终点和停止理由；不能只写“环绕/推近”。

## CASE-SH05｜连续剧部分场景

- **Expected：** 只覆盖用户点名的完整场景范围，保留稳定 Shot ID 和跨场 continuity out；不假装全剧已完成。

