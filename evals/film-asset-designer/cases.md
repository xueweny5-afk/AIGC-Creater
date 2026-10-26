# Film Asset Designer V1 Cases

## CASE-A01｜老菜市场 PLAN_ONLY

- **Input：** READY Visual Bible + Asset Requirements。
- **Expected：** 创建版本化 manifest；地点与道具可进入 PLANNED；两名人物因年龄范围、性别呈现和经营品类仍 OPEN，建立一个身份决定 Gate；不得声称已有图片或批准资产。

## CASE-A02｜老菜市场 GENERATE

- **Input：** 用户回答人物身份 Gate 并明确要求生成。
- **Expected：** 先生成最小 P0 参考，逐张检查；三向视图保持同一身份；真实审核前状态为 GENERATED_PENDING_REVIEW，不自动 APPROVED。

## CASE-A03｜修仙上游未 READY

- **Input：** Visual Development Return。
- **Expected：** 不创建宗门人物、法术、场景或道具资产；返回 Treatment/User Decision。

## CASE-A04｜八王之乱证据不足

- **Input：** Historical Visual Return。
- **Expected：** 不生成驺虞幡、青纸诏、服制或空间资产；返回 Research。

## CASE-A05｜已有三视图审核

- **Input：** 用户提供人物正、侧、背三张图。
- **Expected：** 实际查看原图，检查脸、年龄、体态、发型、服装层、配饰和肢体；把具体失败字段标为 REWORK，不靠补充风格词掩盖漂移。

## CASE-A06｜主要人物完整资产组

- **Input：** 跨镜头复用主角，需要两套服装并会在风雨中行动。
- **Expected：** 先批准正面人脸特写，再派生必要头部角度与独立全身六视图；人物、服装、妆发分别建合同，两套服装记录面料、缝线、层级、磨损与风雨响应；最后用确切版本建立 Combined Look，不让合体图替代源资产。

## CASE-A07｜核心场景和道具细节

- **Input：** 多镜复用室内场景与近景使用的木桌、纸张和金属道具。
- **Expected：** 场景先锁定拓扑，再建立墙地顶、陈设、空气/天气和使用痕迹 Detail Plates；道具记录尺寸、结构、材料、表面细节、状态和人物比例关系。
