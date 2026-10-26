# BATCH-A003 IDENTITY + TOPOLOGY PROMPT PACKAGE

- **Date：** 2026-10-01
- **Canon Parent：** `assets/characters/CHAR-ANXI-001/canon-face-front-v002.png`
- **Location Parent：** `assets/locations/LOC-BATTLEFIELD-001/topology-plan-v002.png`

## HEAD LEFT 45

- **Output：** `head-left45-v001.png`
- **Method：** Built-in image edit / identity preserve.
- **Change：** 只将头部转向画面左侧约 45°。
- **Preserve：** 颅骨、五官、耳形、发际线、胡茬、年龄、肤质、衣领、背景与中性光。
- **Exclude：** 换脸、美化、盔甲、饰物、情绪表演、散发与戏剧光。

## BODY IDENTITY FRONT

- **Output：** `body-identity-front-v001.png`
- **Method：** Built-in image generation with approved Canon Face reference.
- **Subject：** 同一人物，全身正面中性站姿，耐力型体态。
- **Clothing：** 仅灰褐基础内层、布带、裤、绑腿与素面靴。
- **Exclude：** 甲胄、兵器、健美英雄体态、战损、道具与文字。

## A—G TOPOLOGY OVERLAY

- **Outputs：** `topology-zones-v001.svg`；`topology-zones-v001.png`。
- **Method：** Deterministic editable SVG over `topology-plan-v002.png`; browser-rendered PNG preview.
- **Content：** A 前军、B 追击/溃退、C 中军、D 退路/重组、E 反攻推进、F 东翼骑兵、G 战后原阵位。
- **Coordinate Note：** 上=燕军方向，下=唐军后方，右=真实东翼；只用于制作关系，不宣称历史测绘。
