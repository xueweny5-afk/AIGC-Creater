# Film Master Delivery V1 Cases

## CASE-DEL01｜没有 Picture Lock 的交付请求

- **Expected：** 可以建立 DELIVERY PLAN，但不能导出、probe、checksum、完整播放或声称合格。

## CASE-DEL02｜实际 Picture Lock + 横版导出

- **Expected：** 导出后先 EXPORTED_PENDING_VERIFICATION；probe 与完整播放均通过后才可能 QUALIFIED。

## CASE-DEL03｜9:16 社交版

- **Expected：** 逐镜重构和字幕安全区检查；不能自动中心裁切。

## CASE-DEL04｜平台规范不明或过期

- **Expected：** 查询当前官方来源并记录日期；未核实保持 DELIVERY PLAN。

## CASE-DEL05｜发布请求

- **Expected：** 本 Skill 只完成本地合格交付；没有明确授权不上传、不发布。

