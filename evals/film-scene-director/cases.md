# Film Scene Director V1 Cases

## CASE-D01｜老菜市场资产待定

- **Input：** COMPLETE Screenplay、READY Visual Bible、PLAN_ONLY Asset Manifest。
- **Expected：** 完成 S001–S005 的功能性场景设计，但状态为 DRAFT_ASSET_PENDING；不锁定外貌、精确尺度或镜头；下一步为 Asset Decision，不是 Shot Design。

## CASE-D02｜老菜市场资产已批准

- **Input：** 与 CASE-D01 相同，且 P0 人物和场景资产均经实际审核 APPROVED。
- **Expected：** 核对调度可由批准拓扑和身份执行，状态升级为 READY FOR SHOT DESIGN。

## CASE-D03｜修仙上游 Gate

- **Expected：** 返回 Treatment/User Decision，不进行场景调度。

## CASE-D04｜八王之乱研究不足

- **Expected：** 返回 Research，不为传令、解兵和人物位置设计无依据调度。

## CASE-D05｜观察式场景

- **Expected：** 允许重复行为的微差和边界变化构成场景转折，不强制争吵、反派或高潮。

