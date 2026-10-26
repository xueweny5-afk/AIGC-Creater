# ASSET CONTRACT

## IDENTITY

- **Asset ID：** COST-LISIYE-001
- **Type：** COSTUME
- **Working Name：** 李嗣业衣甲状态系统
- **Version：** V1.3
- **Status：** L0_L1_FRONT_GENERATED
- **Evidence Status：** DOCUMENTED TEXT TRADITION / STRUCTURAL RECONSTRUCTION

## LOCKED FEATURES

- 与前军基础衣甲属于同一时代军械世界，但尺寸更大、维护度略高。
- L0 完整扣合；L1 只按实际带件和开口敞开外层，肩胸部分裸露；L2 延续敞开并增加汗尘和损伤。
- 状态只单向变化，不在后续镜头自动复原。

## REQUIRED VIEWS / STATES

1. L0 正背面完整穿着。
2. 扣带路径与受力点。
3. L1 外层敞开正面与侧面。
4. L2 推进积尘损伤。
5. 与 B 型长柄刀的静态受力姿态。

## NEGATIVE CONSTRAINTS

- 无一扯即脱、悬空甲片、无因裸上身和现代健美展示。
- 无英雄披风、金甲、关刀和武侠海报构图。

## DERIVATION RULE

- 以 COST-ANXI-FRONT-001 批准结构为时代母体，再按 CHAR-LISIYE-001 体态调整尺寸。
- L1/L2 必须从 L0 编辑派生，不能重新生成不同盔甲。

## FILES AND REVIEW

- `state-l0-complete-front-v001.png`，1024×1536：完整披甲正面；与前军基础装备同一制造家族，尺寸与维护度适配李嗣业体态。
- `state-l1-open-front-v001.png`，1024×1536：外层上身甲卸除/敞开后状态，肩带、袖层、护臂、腰带和下部甲仍保留可解释受力关系。
- `state-l2-dust-front-v001.png`：从 L1 定点派生，敞开范围及身份保持，新增局部汗尘、衣摆与鞋靴积尘；SELF-REVIEWED_CANDIDATE。
- `state-l0-complete-back-v001.png`：L0 背面候选，同制造家族的甲片、护臂及腰甲连续；背面扣带路径为创作重构，仍需结构联合审核。
- `reference-armored-portrait-clean-user-v001.png`、`reference-armored-portrait-dusty-user-v001.png`、`reference-battlewear-diptych-user-v001.png`：用户提供的参考图，非衣甲状态验收图；近景胸甲仍完整，与已定 L1 敞开结构不符，因此不得标为 L1/L2。
- **Self-review pass：** 两状态保持同一身份、头盔、内层、腰甲、绑腿和鞋靴；裸露体态保留体脂与汗尘，不作健美英雄展示。
- **Known risk：** L1 由生成重构实现，不能证明史实中的具体解甲动作；后续以扣合路径板补充结构解释。
- `state-l1-open-side-v001.png`：朝画面左侧的 L1 全身侧面；裸露范围、袖层、护臂与腰甲延续正面；候选自审通过。
- `detail-fastening-path-v001.png`：肩带、侧扣、L1 上臂带件和腰带四处细节；重构结构参考候选，不证明实际解甲过程。
- `contact-longblade-l1-v001.png`：L1 双手持 B 型长刀接触测试；双手闭合握柄、站姿及衣甲接触可读。刀尖曲率仍有轻微漂移，仅作为静态持握候选，不覆盖 PROP-LONGBLADE-001 的几何母图。
- **Remaining：** L0 正背、L1 正侧与 L2 联合审核；持刀图的刀尖几何需按 B 型母图校准。扣带板目前证明局部连接，不能替代解甲动作链。
- **Decision：** SELF-REVIEWED_CANDIDATE；可继续派生，尚未完成状态系统。

## CHANGE LOG

- V1 / 2026-10-01：建立生成合同，等待基础衣甲。
- V1.1 / 2026-10-01：完成 L0/L1 正面，解除基础衣甲阻断；继续补充结构与损伤状态。
- V1.2 / 2026-10-04：内置 imagegen 生成 L2 正面与 L0 背面，像素自审后候选入库；尚未完成全部状态系统。
- V1.3 / 2026-10-04：生成 L1 侧面、扣带细节与长刀接触候选；明确持刀图几何漂移及扣带板的证据范围。
