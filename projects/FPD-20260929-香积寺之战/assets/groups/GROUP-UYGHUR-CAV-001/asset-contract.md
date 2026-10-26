# ASSET CONTRACT

## IDENTITY

- **Asset ID：** GROUP-UYGHUR-CAV-001
- **Type：** GROUP
- **Working Name：** 回纥骑兵组织资产
- **Version：** V1.1
- **Status：** THREE_RIDER_BASE_GENERATED
- **Evidence Status：** RESEARCHED BATTLE ROLE / VISUAL RECONSTRUCTION / CULTURAL REVIEW REQUIRED

## LOCKED FEATURES

- 作为有组织的盟军骑兵出现，行动由指挥响应、间距、转向和马具家族体现，不以异域奇观化服饰表现。
- 与仆固怀恩使用同一功能性骑装和马具母体系，但普通骑手不得复制其面孔或指挥维护度。
- 人马比例、脚镫、缰绳、髋膝角度和队列间距必须在静态父资产中成立。
- 东翼行动方向与 LOC-BATTLEFIELD-001 拓扑一致；群体尘尾另由环境状态管理。

## REQUIRED VIEWS / STATES

1. 三骑组织母图：侧向/正斜向/后向。
2. 4—6 个受控骑手轮廓与 3—4 种马匹花色变体。
3. U0 等候；U1 统一转向；U2 加速；U3 接敌后。
4. 领骑和普通骑手的维护度、姿态与间距差异。

## NEGATIVE CONSTRAINTS

- 无复制脸、复制马、完全同步姿态或无间距人墙。
- 无皮草奇观、羽饰、兽牙、纹面、野蛮化咆哮或幻想游牧甲。
- 无现代蒙古帝国模板、现代马术装备、披风海洋和全员弓骑兵刻板图。

## DERIVATION RULE

- 以 `PROP-HORSE-TACK-001/rider-contact-left-v001.png` 为人马接触结构父资产。
- 仆固怀恩只出现一次且位置明确；普通骑手脸型、年龄和马匹花色受控变化。
- U1—U3 只改变转向、速度、缰绳张力、队形和汗尘，不改变装备家族。

## FILES AND REVIEW

- `formation-three-riders-v001.png`，1536×1024：三骑正斜向组织母图。
- **Self-review pass：** 三名普通骑手面孔不复制仆固怀恩；三匹马花色、面部标记与体态有受控差异；脚镫、手—缰和安全间距可读；装备属于同一功能家族。
- **Known risk：** 头盔和甲片差异仍偏小，远景易显复制；后续 4—6 轮廓扩展需增加维护、袖口、盔侧和马匹体型差异，避免模板化。
- **Remaining：** 侧向/后向、更多轮廓、U1 转向、U2 加速、U3 接敌后。
- **Decision：** SELF-REVIEWED_BASE_PASS；允许派生群体状态。
