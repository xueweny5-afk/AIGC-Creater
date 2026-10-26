# ASSET CONTRACT

## IDENTITY

- **Asset ID：** CST-001
- **Type：** COSTUME
- **Working Name：** 西晋官署服饰范围
- **Version：** v1.2
- **Status：** APPROVED
- **Purpose：** 为张翰建立可信的西晋属官在职与离任行旅服装层级，避免以通用古装代替身份。
- **Source Visual Bible Version：** `visual-development/world-visual-bible.md` v1
- **Evidence Status：** RESEARCH-INFERRED + OPEN DETAILS

## LOCKED FEATURES

- 时代范围为西晋，身份为齐王冏府属官层级；不升格为王侯、公卿礼服或武官甲胄。
- 服装必须支持室内文职活动、起身离开和水路行旅，不用纯装饰结构限制行动。
- 在职、离任、归途均从同一基础衣层派生；减层有穿脱逻辑，不能瞬间换成另一时代的便服。
- 材料表现织物重量、折叠、系结和使用痕迹；不出现现代拉链、纽扣体系或塑料质感。
- 正式在职状态以《晋令》所见“掾、属，官品第七，朝服，进贤一梁冠”为制度锚点；不锁定未经证实的官阶颜色。

## VARIABLE STATES

- **A｜在职完整层：** 进贤一梁冠候选、基础衣层、朝服外层与简洁腰带；删除 v2 图中未经核验的连续金属方銙装饰。
- **B｜离任减层：** 去除职务专属物，保留适合短途离开的基础衣层。
- **C｜水路行旅：** 在 B 上增加可解释的防风、行旅褶皱或外罩选择，具体形式待研究。
- 色彩、织物粗细、袖量、衣长、缘饰、鞋履与携带方式均可在证据范围内比较。

## PRESENTATION CHOICES

- 服装板采用前、侧、背与分层拆解；中性光线和背景，重点检查结构而非气氛。
- 可用简洁材料近观确认织物与系结；不制作动态场面或人物情绪图。
- 暂按写实历史电影质感呈现实际穿着重量，不做舞台戏服式夸张轮廓。

## UNKNOWN / OPEN FIELDS

- 冠帽具体形式与使用场合。
- 属官服色、衣层名称、腰间制度物、佩物、鞋履和纹样。
- 西晋洛阳季节与南归途中是否需要额外外层。
- 现有博物馆/考古图像对该具体官职的支持强度。

## REQUIRED VIEWS / PLATES

1. **Evidence Plate：** 每个拟采用元素对应来源、时代、地域、身份与限制；后世图像单列，不混为直接证据。
2. **Layer Plate：** 基础层、在职外层、制度物与可移除部分的穿着顺序。
3. **Turnaround Plate：** 批准服装的前、侧、背结构一致性。
4. **State Plate：** 在职、离任、水路行旅三状态的增减关系。
5. **Material Plate：** 织物、系结、鞋履和可能配件的尺度与磨损范围。

## NEGATIVE CONSTRAINTS

- 不混用唐宋幞头、明清补服、戏曲水袖、帝王冕服、武将甲胄或现代汉服商品套装。
- 不以大面积精致刺绣、龙纹、金属亮片或飘带制造“高级感”。
- 不使用散发、敞胸或衣带无限加长表达放达。
- 不在证据不足时用具体官阶颜色制造虚假确定性。
- 不出现品牌、现代扣件、水印或无来源文字。

## FILES AND PATHS

- **Contract：** `assets/costumes/CST-001/asset-contract.md`
- **Generated Images：** `assets/costumes/CST-001/zhang-han-costume-state-reference-v1.png`
- **Evidence Plate：** `assets/costumes/costume-evidence-brief.md`

## REVIEW RESULTS

- **Review Evidence：** USER-APPROVED / 2026-09-23
- **Files Inspected：** `assets/costumes/CST-001/zhang-han-costume-state-reference-v1.png`
- **Passed：** 三状态保持同一张翰身份与结实体态；在职、离任和归途的衣层增减可解释；归途外层完整，无乞者化、破洞或异常毛边。
- **Failed / Open：** 一梁进贤冠的精确结构、官服色相和制度带具仍不能视为考古复原。
- **Decision：** 用户确认视觉与功能方向，升级为 APPROVED；精确冠服制度仍保持研究推定标记。

## DOWNSTREAM USE

- CST-001 通过后绑定 CHR-001，作为其所有状态的服装母合同。
- 任何场景只能改变已批准的可变状态，不能自行增加官阶、时代或纹样信息。

## CHANGE LOG

- **v1｜2026-09-21：** 建立西晋属官服饰研究与状态合同；未生成图片。
- **v1.1｜2026-09-23：** 自动生成三状态服装板；内部定向降低冠体高度并修复归途衣摆破损感，归档为待用户确认候选。
- **v1.2｜2026-09-23：** 用户确认三状态板无问题；批准人物辨识、视觉方向与穿脱逻辑，不宣称精确服制复原。
