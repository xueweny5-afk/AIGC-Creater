# ATMOSPHERE STATE REGISTER｜R1

## IDENTITY

- Project ID：FPD-20260917-八王之乱瞬间。
- Version：ATMOSPHERE-R1；2026-09-30开始整理，2026-10-01完成登记。
- Visual Bible：VISUAL-BIBLE-R1；来源为SCREENPLAY-MASTER-R1。
- Status：DEFINED／READY FOR VISUAL HANDOFF（文字）；ACTUAL MEDIA PENDING QC。
- Skill：film-atmosphere-designer。本登记不是新制作阶段。
- 未把空气效果写成历史天气证据；物理响应可推导，具体当日天气为重建。

## STATES

### ATM-S01-FOG-R1

- Version／Status：R1／DEFINED；实际媒体待QC。
- Bound Location／Scene／Arc／Look：S01／S001／LA01／LLS-S01-DAWN-R1。
- Medium／Source／Evidence：FOG／户外晨雾；天气重建CREATIVE。
- Distribution／Height／Depth：低位门外较浓、门洞口略稀，非整图均匀。
- Density／Visibility／Color／Scale：远景部分轮廓被遮，门轴与通道可读；灰白不发光。
- Temperature／Humidity：清晨高湿与近地冷凝，具体气温未知。
- Driver／Speed／HOLD：微弱风与开门通风，缓慢横移；马经过造成局部扰动。
- Light Interaction：门外自然光使雾可见，门内不新增体积光。
- Material／Costume／Skin Response：受潮地面、木门局部低反光；非全身凝露。
- Readability Limit：不得遮没门轴、通道或军队进入状态。
- Pre-state→Trigger→Transition→Post-state→Decay：封闭入口→开门→雾进入门洞→分布恢复→弱风持续。
- Allowed／Forbidden：仅低位雾和轮廓密度可变；不得变烟、金色颗粒、波浪墙。
- Asset Requirement：需要同场景可见雾与清晰结构基准，不把雾图当唯一拓扑证据。
- Downstream：Scene/Shot继承ID和遮挡限制；Motion编译驱动与衰减；Prompt只压缩已定字段；QC检查来源、分布、物理响应与相邻镜头密度。
- QC Evidence／Actual Observation：NOT_RUN，无生成或像素通过声明。

### ATM-S02-SPLASH-R1

- Version／Status：R1／DEFINED；实际媒体待QC。
- Bound Location／Scene／Arc／Look：S02／S002／LA01／LLS-S02-WETDAY-R1。
- Medium／Source／Evidence：SPRAY／马蹄碰积水；批准动作的物理推导DERIVED。
- Distribution／Height／Depth：只在蹄接触点附近，水滴沿动量抛出后下落。
- Density／Visibility／Color／Scale：小水花，非慢动作巨浪；背景无新浓雾。
- Temperature／Humidity：湿地／降雨语境，具体气温未知。
- Driver／Speed／HOLD：一次接触动量、重力；落回后涟漪衰减。
- Light Interaction：阴天自然光，仅水滴局部反光。
- Material／Costume／Skin Response：蹄与脚边湿润、泥点在接触范围；百姓上衣不整身淋透。
- Readability Limit：不能遮百姓收袖、蹄接触和马具。
- Pre-state→Trigger→Transition→Post-state→Decay：触水前→一次落蹄→飞溅→水滴落回→涟漪衰减。
- Allowed／Forbidden：不二次踏水、不全局粒子、不飘浮液珠。
- Asset Requirement：动作前与接触后状态需证据；Motion阶段再安排时间。
- Downstream：Scene/Shot继承ID和遮挡限制；Motion编译驱动与衰减；Prompt只压缩已定字段；QC检查来源、分布、物理响应与相邻镜头密度。
- QC Evidence／Actual Observation：NOT_RUN，无生成或像素通过声明。

### ATM-PALACE-RAIN-R1

- Version／Status：R1／DEFINED；实际媒体待QC。
- Bound Location／Scene／Arc／Look：宫阶／S003／LA01／LLS-PALACE-RAIN-R1。
- Medium／Source／Evidence：RAIN／剧本已认可的雨；CREATIVE重建。
- Distribution／Height／Depth：开放宫阶垂直或略受风偏斜；门内明显减弱。
- Density／Visibility／Color／Scale：克制连续雨滴，纸诏印边仍可读。
- Temperature／Humidity：湿地／降雨语境，具体气温未知。
- Driver／Speed／HOLD：降雨、重力与阶上浅水流；不无风横向喷射。
- Light Interaction：阴天光；雨滴不是均匀亮线，近火不照亮整场雨。
- Material／Costume／Skin Response：纸吸水、墨印局部渗散；石阶湿润；门框接触积水。
- Readability Limit：必须看清纸诏位置、门缝与闭合状态。
- Pre-state→Trigger→Transition→Post-state→Decay：纸已湿→雨继续→微渗→留在阶上→不瞬间干燥。
- Allowed／Forbidden：不突增暴雨、不让纸溶解、不自动新增血流。
- Asset Requirement：纸纤维与湿石交互样片为必要近景细节。
- Downstream：Scene/Shot继承ID和遮挡限制；Motion编译驱动与衰减；Prompt只压缩已定字段；QC检查来源、分布、物理响应与相邻镜头密度。
- QC Evidence／Actual Observation：NOT_RUN，无生成或像素通过声明。

### ATM-INTERIOR-CLEAN-R1

- Version／Status：R1／DEFINED；实际媒体待QC。
- Bound Location／Scene／Arc／Look：S03／S004、S006、S015；P05／S010；LA02/03/04/05。
- Medium／Source／Evidence：NONE／CLEAN AIR；无显著烟尘源。
- Distribution／Height／Depth：整体清洁空气，油灯局部烟仅在有可见源并另登记时允许。
- Density／Visibility／Color／Scale：不以漂粒证明空间，暗部由真实照度形成。
- Temperature／Humidity：具体气温未知，不用无依据凝露表现湿冷。
- Driver／Speed／HOLD：HOLD；S015穿堂风影响绶带，不要求风可见。
- Light Interaction：油灯和门光作用于物件，不新增可见光柱。
- Material／Costume／Skin Response：织物靠风和姿态响应；皮肤按光源保留颜色。
- Readability Limit：不以灰雾遮人脸、冠式或手与玉。
- Pre-state→Trigger→Transition→Post-state→Decay：清洁→帘/绶带受风→物件响应→空气仍清洁。
- Allowed／Forbidden：不持续飘尘、不殿内低雾、不车内烟气。
- Asset Requirement：清晰场景与衣物材料即可；无单独空气生成需求。
- Downstream：Scene/Shot继承ID和遮挡限制；Motion编译驱动与衰减；Prompt只压缩已定字段；QC检查来源、分布、物理响应与相邻镜头密度。
- QC Evidence／Actual Observation：NOT_RUN，无生成或像素通过声明。

### ATM-ABSTRACT-CLEAN-R1

- Version／Status：R1／DEFINED；实际媒体待QC。
- Bound Location／Scene／Arc／Look：S04／S005、S007、S014；抽象交接／S009；LA02/03/05。
- Medium／Source／Evidence：NONE／图形与道具展示空间。
- Distribution／Height／Depth：清洁，不把地图尘埃当时间流逝特效。
- Density／Visibility／Color／Scale：足以读数量和接触，不添加发光粒子。
- Temperature／Humidity：具体气温未知，不用无依据凝露表现湿冷。
- Driver／Speed／HOLD：HOLD。
- Light Interaction：工作光照物体，不照尘粒。
- Material／Costume／Skin Response：木棋、纸图、玉玺与手部可辨。
- Readability Limit：八枚数量、字图与手指承重不可遮。
- Pre-state→Trigger→Transition→Post-state→Decay：信息变化→图形或接触变化→空气HOLD。
- Allowed／Forbidden：不沙暴、不烟幕、不发光路线气溶胶。
- Asset Requirement：无单独空气素材。
- Downstream：Scene/Shot继承ID和遮挡限制；Motion编译驱动与衰减；Prompt只压缩已定字段；QC检查来源、分布、物理响应与相邻镜头密度。
- QC Evidence／Actual Observation：NOT_RUN，无生成或像素通过声明。

### ATM-OUTDOOR-CLEAN-R1

- Version／Status：R1／DEFINED；实际媒体待QC。
- Bound Location／Scene／Arc／Look：S05/S06/S07／S008、S011、S012、S013；LA03/04。
- Medium／Source／Evidence：NONE／户外正常空气；显著尘烟来源OPEN。
- Distribution／Height／Depth：自然空气；近地微尘仅有干路证据才新增局部状态。
- Density／Visibility／Color／Scale：行军和流民轮廓可读，背景不灰蒙遮盖。
- Temperature／Humidity：具体气温未知，不用无依据凝露表现湿冷。
- Driver／Speed／HOLD：低风只影响旗、衣、草；不自动生成粒子。
- Light Interaction：阴天或暮光照材料，而非人造空气亮层。
- Material／Costume／Skin Response：泥尘主要表现在接触表面，湿干状态不凭空切换。
- Readability Limit：不可遮马匹数量、轮轴、母子牵手或方向。
- Pre-state→Trigger→Transition→Post-state→Decay：行走→衣旗响应→人物前行→空气保持。
- Allowed／Forbidden：不新增村庄大火、浓烟、全局风沙。
- Asset Requirement：道路材质、衣摆与轮下接触基准；无需烟雾图。
- Downstream：Scene/Shot继承ID和遮挡限制；Motion编译驱动与衰减；Prompt只压缩已定字段；QC检查来源、分布、物理响应与相邻镜头密度。
- QC Evidence／Actual Observation：NOT_RUN，无生成或像素通过声明。

### ATM-S08-CLEAN-NIGHT-R1

- Version／Status：R1／DEFINED；实际媒体待QC。
- Bound Location／Scene／Arc／Look：S08／S016／LA05／LLS-S08-NIGHT-R1。
- Medium／Source／Evidence：NONE／夜城空气；未在剧本锁定城外雾。
- Distribution／Height／Depth：高空云可既有缓移；地面黑暗不是雾幕。
- Density／Visibility／Color／Scale：保持远火点尺度，不出现包围点的大光晕。
- Temperature／Humidity：具体气温未知，不用无依据凝露表现湿冷。
- Driver／Speed／HOLD：云受高空风；近处火源热对流只在火盆局部。
- Light Interaction：夜光与近火只影响相应物体；远火不照亮近城。
- Material／Costume／Skin Response：守军衣甲受近处实用火光，地面不新增无来源湿亮。
- Readability Limit：城垛、山线、单火点位置始终稳定。
- Pre-state→Trigger→Transition→Post-state→Decay：黑暗→单点显露→断续火线→身份仍未知→黑场。
- Allowed／Forbidden：不添加大片平流雾、不远火照脸、不把火点当粒子特效。
- Asset Requirement：黑暗、单点、火线同空间状态对照；先核几何。
- Downstream：Scene/Shot继承ID和遮挡限制；Motion编译驱动与衰减；Prompt只压缩已定字段；QC检查来源、分布、物理响应与相邻镜头密度。
- QC Evidence／Actual Observation：NOT_RUN，无生成或像素通过声明。

## TRANSITIONS

S001晨雾进入门洞由开门引起；S002低水花来自积水接触，不能把晨雾密度无因转为街巷浓烟。S003有剧本规定的雨，与S004室内空气清洁的变化由地点和时间切换解释。S004→S006跨年代，空气身份不要求沿十年连续。S012→S013同暮色户外，空气密度HOLD。S016黑暗→火点→火线只是信息显露，不增加介质或改变近光。

## DECISION REGISTER

LOCKED：剧本雨、晨雾、一次接触、空殿绶带和未知火线。DEFINED：上述状态的因果分布、驱动、可读性和禁止项。OPEN：旧图额外烟、尘、雾是否有来源；核图后处理，不能仅因图中出现就批准。没有真实气象资料，不写具体温湿数值。

## NEXT ROUTE

Asset Design：审核场景结构基准与空气交互细节；空气板不能替代场景拓扑。之后由Scene/Shot继承，再由Motion/Prompt编译；实际生成后才填写QC证据。

