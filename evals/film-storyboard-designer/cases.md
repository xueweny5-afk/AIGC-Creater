# Film Storyboard Designer V1 Cases

## CASE-B01｜老菜市场 S005 PLAN_ONLY

- **Input：** READY Shot List + Continuity Ledger + evaluation-approved assets。
- **Expected：** 4 个 Shot 使用 5 个必要 Frame；SH04 使用 Start/End；只有一个 Hero Frame 候选；全部状态 PLANNED、无虚构文件路径或批准结论。

## CASE-B02｜实际生成

- **Expected：** 生成后先标 GENERATED_PENDING_REVIEW，逐张查看原图后才能 READY；身份、轴线、夹子、托盘缺席和扫帚接触必须检查。

## CASE-B03｜资产待定

- **Expected：** 返回 Asset Design，不生成替代人物或场景。

## CASE-B04｜镜头不可视化

- **Expected：** 返回 Shot Revision，不用文字箭头修补错误镜头。

## CASE-B05｜Hero Frame 选择

- **Expected：** 只选择主题/转折审批价值最高的少量帧，不把每张 Board 美化成 Hero Frame。

