# 《洛阳无赢家》MiniMax H3｜参考图＋逐镜提示词一体执行版 R3

Project ID：`FPD-20260917-八王之乱瞬间`。项目根目录：`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20260917-八王之乱瞬间\`；下文图片路径均从此目录起算。源合同：`direction/shot-list-r1-review.md`、`storyboard/animatic/animatic-plan-r1.md`、`motion/motion-spec-r3-exploration.md`；18 张现有静帧已获用户接受。本文件是视频生成前的执行卡，**不是已生成或审核通过的视频**。文字版 75 秒顺序已确认，带声 Animatic 未实播；试片仍需验证。

**使用顺序：**先选 RunningHub 中明确标为 MiniMax H3 的**首帧图生视频 I2VA**入口；按每卡顺序上传首帧，状态核对图不放进无角色说明的槽。设置 9:16。下面每条提示词按**5 秒试片**编排：若页面提供 5 秒档就选 5 秒，前段完成成片所需动作，余下时间保持终态；后期从开头裁出各卡目标时长。若入口只支持其他时长，先按实际档位重排时间码，不要直接套用。只复制每卡代码框，不复制路径和验收。历史旁白、字幕、地图字和最终声轨均由后期完成；模型原生声仅供试片参考。

**格式说明：**用户示例的 `subject_definitions / summary / retention_analysis / detailed_description` 六段式属于 H3 全参考 Ref2VA；本项目每镜以静帧固定 0 秒，按 MiniMax 官方 I2VA 格式使用首帧声明＋`integrated_multimodal_description / overall_soundscape / non_diegetic_music`。主体身份与必须保留内容写在主描述里；这属于生成约束，不是已生成结果的 `fully_preserved` 审核结论。结构依据：[MiniMax 官方 H3 提示词指南](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/skills/h3-prompt-writing/references/base-en.txt)。

**先试片：**SH01→02、SH03、SH04B、SH12B、SH14、SH19→20。每次保存 `镜号-H3-入口-实际秒数-Take编号` 的原 MP4 和所用图；上镜实际终态审核后再做强依赖下镜。四个静态单元 SH07、08、11、17 不提交视频模型。全片 21 个叙事镜号、23 个画面单元，目标成片 75 秒。H3 模型模式参考 [MiniMax 官方资料](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/README.zh-CN.md)；RunningHub 具体工作流差异需以实际页面为准。

通用验收：历史纪录片式实拍质地，夯土／旧木／麻布／皮甲／玉石有局部真实磨损；不变成游戏 CG、夸张 HDR、无来源烟尘；不生成任何可读文字、Logo、现代物品。下列排除已写进各卡主词，RunningHub 入口无独立负向栏也可直接复制。先做 SH01、03、04B、12B、14、19/20 技术试片。

## SH01｜00:00–00:03，门缝未知感

操作｜首帧上传 `assets/locations/S01-洛阳城门/S01-窄缝-R2-v1.png`；`assets/locations/S01-洛阳城门/S01-城内望城外清洁拓扑-R2-v2.png` 只核空间，不作尾帧。成片保留 3 秒；门洞可通行才剪 SH02。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. Preserve the same Western Jin Luoyang gate from <Picture 1>: two heavy timber leaves, rammed-earth walls, the narrow central slit, and low grey morning fog outside. A low camera inside the gateway remains completely static. During 0.00–0.50 seconds, the slit holds and the approaching riders remain unidentifiable. During 0.50–2.70 seconds, the two door leaves slowly open inward with visible weight and resistance; the slit expands into a passable opening. Cool overcast daylight enters only through the growing gap, and the opening draws a little ground-level fog inward. By 2.70 seconds the doors stop. The passable doorway holds through 5.00 seconds. Do not reveal countable riders, faces, a second gate, smoke, golden beams, or text.
overall_soundscape: Distant hoofbeats approach beneath a low outdoor wind. Damp timber and hinges strain softly as the leaves move, then settle.
non_diegetic_music: N/A
```

验收：门洞末态可供 SH02 入城；先无脸无军数。H3 原生声只作临时声轨，门轴／蹄声后配。

## SH02｜00:03–00:06，骑兵入城

操作｜首帧上传 `storyboard/frames/S001-SH02-F01/S001-SH02-F01-v2.png`。成片保留 3 秒；若 SH01 实际开门终态与此不符，先核对门形再生成。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. <Picture 1> establishes the already-open Luoyang gate, the leading mounted soldier, the following riders, and travel from outside into the city. Do not reopen the doors. During 0.00–2.50 seconds, the lead horse crosses the threshold and the following riders enter at slightly uneven intervals. Leather tack and halberd shafts respond only to the horses' steps. The low camera pulls backward along the gateway axis with small amplitude at a speed slower than the horses. By 2.50–3.00 seconds, a foreleg nears the lower frame edge; this advancing state holds or continues minimally through 5.00 seconds for trimming. Keep the timber gate, rammed-earth walls, and cool fog-side daylight consistent. No turn, charge, shout, water contact, new palace gate, or visible modern tack.
overall_soundscape: Hooves move from muffled distance into the gate passage, with restrained leather and armor movement. No spoken voice.
non_diegetic_music: N/A
```

验收：入城方向与 SH01 一致，门已开；保留可剪到 SH03 的马步余势。

## SH03｜00:06–00:10，一次蹄水与避让

操作｜首帧上传 `storyboard/frames/S002-SH03-F01/S002-SH03-F01-v2.png`；`storyboard/frames/S002-SH03-F02/S002-SH03-F02-v2.png` 仅供人工核对接触后状态，**不上传尾帧槽**。成片保留 4 秒。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. Preserve the same wet Luoyang street, one descending forehoof, shallow puddle, wall, and two civilians in <Picture 1>. From 0.00–1.30 seconds the hoof approaches the water while the first civilian lowers their gaze. At 1.30–2.00 seconds the hoof touches the puddle exactly once, creating a short, low splash localized at the contact point. From 2.00–3.30 seconds droplets fall by gravity and ripples weaken; the second civilian reacts later by gathering a sleeve and pressing toward the wall. The horse continues in its original direction. A low camera moves backward only a short distance, retaining the hoof, water, and staggered human reactions in one frame. From 3.30–5.00 seconds the passage remains clear. Overcast light creates limited reflection on wet mud and droplets. No second splash, giant wave, synchronized kneeling, screaming, or global mist.
overall_soundscape: One hoof strikes shallow water; the splash falls back over subdued street ambience and brief cloth movement. No voices.
non_diegetic_music: N/A
```

验收：唯一一次触水；F02 仅作为人工末态核对，不放尾帧槽。

## SH04A｜00:10–00:13，雨中诏书

操作｜首帧上传 `storyboard/frames/S003-SH04A-F01/S003-SH04A-F01-v2.png`。成片保留 3 秒；纸开场已落地。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. The single paper edict in <Picture 1> is already lying on the same wet palace step. The low close camera is completely static. Throughout 0.00–3.00 seconds, steady restrained rain lands on paper and stone; the red seal edge absorbs water and spreads only slightly, while a thin surface flow passes the paper edge. The paper does not change position. Hold the resulting wet paper and stone through 5.00 seconds. Preserve cool overcast diffuse light, visible paper fibers, and their physical contact with the step. Do not show the paper falling again, a hand retrieving it, rapid dissolution, legible writing, blood, extra people, or artificial light effects.
overall_soundscape: Continuous natural rain taps paper and stone, with a thin trickle along the step. No dialogue or impact.
non_diegetic_music: N/A
```

验收：与 SH04B 同一纸位置；雨量保持克制。

## SH04B｜00:13–00:15，宫门碰合

操作｜开门态候选为 `storyboard/frames/S003-SH04A-F01/S003-SH04A-F01-v2.png`；闭门目标是 `storyboard/frames/S003-SH04B-F01/S003-SH04B-F01-v2.png`。两图景别可能不同，**先检查是否真能当同机位首尾帧**；若不能，不强行首尾帧插值，先以闭门目标作构图参照补同机位开门首帧。当前入口有专用尾帧槽且两帧已对位时才上传尾帧。成片保留合门过程约 2 秒。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. <Picture 1> must be the verified open state of this same palace gate, seen from a low fixed camera below the wet steps; the one paper edict is already in place. Hold the open state for 0.00–0.20 seconds. From 0.20–1.70 seconds, the two heavy timber leaves close toward the central axis with credible mass and hinge resistance. At 1.70–2.00 seconds the leaves meet once and settle with a slight residual vibration. Hold the closed gate through 5.00 seconds. Rain continues, while the paper stays fixed on the stone. Keep doorframe, columns, paper, and overcast light spatially consistent. No reverse opening, flying paper, person placing or collecting the edict, new figure inside, or shot cut.
overall_soundscape: Restrained rain continues beneath one heavy wooden door closure and its short decay. No speech.
non_diegetic_music: N/A
```

验收：从开到闭，同一纸，余响后切殿。

## SH05｜00:15–00:18，皇帝被大殿吞没

操作｜首帧上传 `storyboard/frames/S004-SH05-F01/S004-SH05-F01-v2.png`。成片保留 3 秒；与 SH06 核同一皇帝和殿轴。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. Preserve Emperor Hui's identity, seated posture, hands on knees, imperial clothing, and the central axis of the great hall shown in <Picture 1>. The wide frame holds its scale for the first 1.00 second. From 1.00–3.00 seconds the camera pushes in along the axis with very small amplitude at slow speed; the emperor still reads as small within the architecture. From 3.00–5.00 seconds the camera and seated figure hold. Only subtle natural breathing is allowed. Weak warm oil-lamp pools and distant cool doorway light keep their original directions; the interior air stays clear. No standing, speaking, exaggerated vacant expression, additional courtiers, second throne, drifting dust, or theatrical light shafts.
overall_soundscape: The previous door resonance fades into a quiet hall with faint distant footsteps and localized lamp crackle. No on-screen speech.
non_diegetic_music: N/A
```

验收：人物尺度小，光与 SH06 连贯。

## SH06｜00:18–00:22，权力遮挡

操作｜首帧上传 `storyboard/frames/S004-SH06-F01/S004-SH06-F01-v2.png`。成片保留 4 秒；参考 SH05 实际结果核脸、座位与光向。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. <Picture 1> fixes the same Emperor Hui, seat, clothing, hall columns, and light direction as the preceding shot. From 0.00–1.50 seconds, anonymous foreground bodies and hanging fabric pass across the frame, progressively obscuring the seated emperor. From 1.50–2.50 seconds, only after the occlusion arrives, his gaze follows it with a small delayed movement; his torso and hands stay in place. From 2.50–4.00 seconds, column and curtain shadows divide his figure further. The camera trucks sideways with small amplitude along the already established column row, then stops; the obscured state holds through 5.00 seconds. Warm oil lamps and cool doorway light remain the same sources; darkness changes only through occlusion. No named faces, dialogue, new blue light, dust beams, or emperor rising.
overall_soundscape: Soft footsteps and cloth movement cross an otherwise quiet hall. No spoken words.
non_diegetic_music: N/A
```

验收：SH05 同脸同座、人物只被分割不离座。

## SH07｜00:22–00:26；SH08｜00:26–00:30

操作｜SH07、SH08 使用同一张 `assets/props/P06-八王形势地图/P06-清洁八棋-R2-v1.png`，各保留 4 秒。两镜均**不投 H3**：固定底图、局部调光、姓名由后期完成。无落子、无棋位改变、无生成文字。

## SH09｜00:30–00:33，双掌托玺

操作｜首帧上传 `storyboard/frames/S006-SH09-F01/S006-SH09-F01-v2.png`。成片保留 3 秒；末态须供 SH10 双掌托同一玺。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. Preserve Sima Lun's face and robe, his two supporting palms, and the sole pale jade seal in <Picture 1>. For 0.00–0.60 seconds his gaze settles on the seal. From 0.60–2.20 seconds both hands lift together only slightly, keeping the jade body level and continuously supported; the cord responds to the small movement. By 2.20–3.00 seconds his hands become still, and that stable two-handed hold continues through 5.00 seconds. The close side camera is static; focus may shift once from sleeve edge to jade surface. Existing dim hall light produces a low, localized reflection on the jade. No second seal, one-handed hold, renewed taking action, grin, speech, altered sleeve, or glowing artifact.
overall_soundscape: Quiet sleeve and seal-cord friction in a restrained indoor ambience. No voice.
non_diegetic_music: N/A
```

验收：能与 SH10 的持玺状态相接。

## SH10｜00:33–00:36，抵达帝座前

操作｜首帧上传 `storyboard/frames/S006-SH10-F01/S006-SH10-F01-v2.png`。成片保留 3 秒；先核 SH09 实际玉玺、袖口和持法。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. Continue from <Picture 1>: Sima Lun already carries the same single jade seal in both palms along the established hall axis. During 0.00–2.00 seconds he completes only the remaining short part of two or three measured steps toward the throne steps; both palms stay beneath the seal. During 2.00–3.00 seconds he stops below the steps and looks toward the seat. Hold this standing, two-handed end state through 5.00 seconds. The low camera pushes in very slowly along the axis and stops when he stops. Timber architecture, dim warm lamps, cool doorway light, and clear interior air remain stable. No second act of taking the seal, no lowered one-hand carry, second seal, sitting on the throne, or sudden mass kneeling.
overall_soundscape: Two or three measured footfalls and restrained robe movement in a quiet hall. No dialogue.
non_diegetic_music: N/A
```

验收：唯一玺、双掌支撑、末尾停步。

## SH11｜00:36–00:40，诸王讨逆示意图

操作｜使用 `assets/props/P06-八王形势地图/P06-无字底图-R2-v1.png`，保留 4 秒；**不投 H3**。多方姓名与趋向洛阳的示意路线由后期加在无字底图上，不让模型生成可读文字或错误地理。

## SH12A｜00:40–00:42，五骑荒野

操作｜首帧上传 `storyboard/frames/S008-SH12A-F01/S008-SH12A-F01-v1.png`。成片只保留连续行进的 2 秒，不加速马匹。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. <Picture 1> fixes exactly five mounted riders, their uneven spacing, travel direction, dry northern plain, and distant hills. Across 0.00–2.00 seconds all five continue riding in the same direction at a controlled pace through the static side-on frame. They neither charge nor pose. Each hoof contact disturbs only a faint, ground-hugging trace of dry dust that falls back quickly; tack and armor respond to the horses' weight. During 2.00–5.00 seconds the same passage continues without changing rider count or terrain. The horizon and camera remain locked. No sixth rider, dust storm, smoke, flag sea, modern tack, or heroic low-angle reframing.
overall_soundscape: A brief layer of five horses' hoofbeats, with restrained leather and armor movement under open-air wind. No shouting.
non_diegetic_music: N/A
```

验收：严格五骑；成片仅保留连续通过的 2 秒。

## SH12B｜00:42–00:45，匿名交玺一次

操作｜首帧只上传 `storyboard/frames/S009-SH12B-F01/S009-SH12B-F01-v1.png`；`storyboard/frames/S009-SH12B-F02/S009-SH12B-F02-v1.png` 仅人工核对承重终态，因构图尺度跳变**不能放尾帧槽**。成片保留 3 秒；失败不要复制玺或硬做变形。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. <Picture 1> fixes the anonymous giver's hands, the receiver's lower hands, and exactly one jade seal at a constant close-up scale. From 0.00–0.70 seconds the giver bears all the weight while the receiving palms hover below. From 0.70–1.80 seconds the receiver touches the underside and progressively takes the weight. Only after that contact is stable, from 1.80–2.50 seconds, the giver's fingers relax and withdraw. From 2.50–3.00 seconds the receiver alone holds the same seal steady; hold that end state through 5.00 seconds. The eye-level camera, grey background, seal size, orientation, and seal cord remain coherent. No faces, second seal, hand intersection, zoom jump, cut, or repeated transfer.
overall_soundscape: Very soft sleeve friction and one small seal-cord movement in a quiet room. No speech.
non_diegetic_music: N/A
```

验收：接收先承重，给予后松手；同一玉体连续可追。

## SH13｜00:45–00:48，车中的惠帝

操作｜首帧上传 `storyboard/frames/S010-SH13-F01/S010-SH13-F01-v1.png`。成片保留 3 秒；后镜车外体要核同一牛车。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. Preserve Emperor Hui's older travel-state face, clothing, seated position, and the enclosed ox cart's curved wooden frame and single curtain gap from <Picture 1>. For 0.00–0.70 seconds, wheel travel creates a slight regular vibration in the old timber while he remains seated. From 0.70–2.00 seconds his gaze turns slowly toward the curtain gap; cool daylight from that gap passes lightly across his face because the cart is moving. From 2.00–3.00 seconds he continues looking outward without opening the curtain; hold the seated state through 5.00 seconds. The camera shares only the cart's subtle movement and never leaves the narrow interior. No second window, curtain lifting, struggle, speech, smoke, dust, or altered carriage shape.
overall_soundscape: Rolling wooden wheels, a faint old-wood creak, and distant footsteps outside the cart. No on-screen voice.
non_diegetic_music: N/A
```

验收：人物面貌和 SH14 同车连贯。

## SH14｜00:48–00:52，牛车离城

操作｜首帧上传 `storyboard/frames/S011-SH14-F01/S011-SH14-F01-v1.png`。成片保留 4 秒；以城门始终在车后、距离增加作为通过条件。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. Preserve the one ox, same enclosed wooden cart, wet road, and distant Luoyang gate in <Picture 1>. During 0.00–3.00 seconds the ox draws the cart steadily farther outward along the road; the gate remains behind the cart and their real spatial separation increases. A few soldiers continue to escort rather than chase. During 3.00–4.00 seconds the distance increases further; the same travel direction may continue through 5.00 seconds. The roadside camera remains static while wall geometry and road perspective stay fixed. Hooves and wheels disturb mud and shallow water only at contact points; no dry dust rises. Keep overcast natural light and the cart's curved cover, wooden axle, and two wheels consistent. No U-turn toward the gate, extra ox, second cart, second gate, or combat.
overall_soundscape: One ox's steps, wooden wheel rhythm, and limited wet-road contact sounds; escorting footsteps remain subdued. No voices.
non_diegetic_music: N/A
```

验收：门在车后、距离增加；湿路无尘。

## SH15｜00:52–00:56，无烟荒田

操作｜首帧上传 `assets/locations/S07-荒田与流民道路/S07-无烟荒田-R2-v1.png`。成片保留 4 秒；不得继承旧版带烟场景图。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. Preserve the empty field, muddy road, field ridge, and muted dusk light of <Picture 1>. From 0.00–1.00 seconds the frame holds still so the absence of people reads clearly. From 1.00–3.00 seconds the camera trucks a short distance along the field edge at slow speed, revealing the abandoned farm tool and empty grain sack in sequence without changing their physical locations. From 3.00–5.00 seconds it stops and holds the relation between field, objects, and road. Weak wind moves only a little dry grass; the air stays clear. No people, village fire, cooking smoke, thick fog, flags, or airborne dust. Do not turn the shot into a disaster spectacle.
overall_soundscape: Thin open-air wind over an otherwise quiet, unworked field. No speech or dramatic impact.
non_diegetic_music: N/A
```

验收：空田、农具、袋都能看清，末尾能声桥到脚步。

## SH16｜00:56–01:00，母子牵手

操作｜首帧上传 `storyboard/frames/S013-SH16-F01/S013-SH16-F01-v1.png`。成片保留 4 秒；同 SH15 暮光和无烟状态。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. <Picture 1> fixes the mother and child's back-view identities, body proportions, rough clothing, joined hands, damp road, and sparse refugee group ahead. During 0.00–1.00 seconds the mother slows slightly to match the child's shorter stride. From 1.00–3.20 seconds the child catches up; they continue forward in the same direction while keeping the same hands joined. From 3.20–4.00 seconds they reach the loose edge of the group and remain distinguishable. Hold or continue this restrained walking state through 5.00 seconds. A level rear camera remains static. Dusk light and clear, smokeless air match the preceding field; cloth moves only with walking. No separation, turning back, running, crying, conflicting crowd direction, or dry-road dust.
overall_soundscape: Soft footsteps on damp earth and slight coarse-cloth friction under open-air wind. No shouting.
non_diegetic_music: N/A
```

验收：牵手始终可追、人数与身高关系不漂。

## SH17｜后期，不投视频模型

操作｜01:00–01:03 使用 `assets/props/P06-八王形势地图/P06-清洁八棋-R2-v1.png`，在剪辑软件中逐渐压低侧上方光区，保留 3 秒；八枚棋与中央红点像素位置不动。`storyboard/frames/S014-SH17-F01/S014-SH17-F01-v1.png` 仅作暗光氛围参考，因红点消失不可作 H3 尾帧。

## SH18｜01:03–01:06，空殿玺绶

操作｜首帧上传 `storyboard/frames/S015-SH18-F01/S015-SH18-F01-v1.png`。成片保留 3 秒；只动绶带末端一次。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. Preserve exactly one jade seal resting on the same night-hall stone step, with the same dark-red cord, scale, hall axis, and low camera from <Picture 1>. From 0.00–0.80 seconds the empty hall remains still. A single cross-draft lifts only the loose end of the cord between 0.80–2.00 seconds. Gravity brings that loose end back onto the stone by 2.50 seconds. Hold the resulting empty, still composition through 5.00 seconds; the jade body never moves. Limited residual lamp light reaches only nearby stone and leaves the rest dim but readable. No visitor, sliding or rotating seal, glowing artifact, repeated cord motion, drifting dust, or visible light beams.
overall_soundscape: A low draft moves through the hall; the cord brushes stone once and the room returns to near quiet. No speech.
non_diegetic_music: N/A
```

验收：玉体静止、绶带一次，夜殿不被额外灯光点亮。

## SH19｜01:06–01:09，黑暗里的一点

操作｜首帧上传 `assets/locations/S08-洛阳城墙/S08-近火源位置-R2-v1.png`；`assets/locations/S08-洛阳城墙/S08-单火点-R2-v1.png` 只核远点状态和位置。成片保留 3 秒；实际末态核过后再做 SH20。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. <Picture 1> fixes the night watch position behind the battlements, moon, mountain line, nearby brazier, and an exterior horizon with no distant flame. The camera and exposure are completely static. From 0.00–2.00 seconds the far plain stays dark; no distant fire is visible. From 2.00–2.80 seconds exactly one tiny dim amber point gradually appears at a fixed far-away position. From 2.80–5.00 seconds that single point holds, still too distant to reveal people. High clouds may move imperceptibly; the brazier flickers only on nearby surfaces. The distant point never brightens the wall or guard. No second early point, enemy faces, banners, fire sea, ground fog, or change in the battlements and moon.
overall_soundscape: Night wind moves across the wall, with only localized brazier crackle. No battle cries or recognizable army sounds.
non_diegetic_music: N/A
```

验收：前半无远点，尾部唯一点；优先与 SH20 用同一底图核位。

## SH20｜01:09–01:11，远火断续

操作｜优先用 SH19 审核过的实际末帧作首帧；若该末帧不可用，候选为 `assets/locations/S08-洛阳城墙/S08-单火点-R2-v1.png`。`assets/locations/S08-洛阳城墙/S08-断续火线-R2-v1.png` 只核目标火线，不强行作尾帧。成片保留 2 秒。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. At 0.00 seconds <Picture 1> already contains exactly one tiny distant amber fire point at the same night-wall viewpoint as the previous shot. Hold that point alone for 0.00–0.50 seconds. From 0.50–1.70 seconds a few more equally distant points appear one after another near it, forming a sparse broken line; the original point never moves. By 1.70–2.00 seconds the broken line is readable while its owners remain unidentified, and that final state holds through 5.00 seconds. Keep the camera, moon, mountain line, battlements, brazier, and near-wall exposure locked. Distant points do not light the guard's face. No near-wall flames, dense army, banners, battle cries, or text.
overall_soundscape: Night wind and local brazier crackle continue; only indistinct far-off movement may be heard. No identifiable voices or battle shouts.
non_diegetic_music: N/A
```

验收：先一点后断续线，几何对位；若漂移则用静图后期叠火点。

## SH21｜01:11–01:12，握戟后切黑

操作｜首帧上传 `storyboard/frames/S016-SH21-F01/S016-SH21-F01-v1.png`。视频只保留 01:11–01:12 约 1 秒守军动作；01:12–01:15 的 3 秒黑场、两行史实字和一次撞门声由后期添加。

**主提示词**

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action historical reconstruction. Preserve the same wall guard's face, armor, original grip on one long halberd, and fixed eye-level medium close-up from <Picture 1>. During 0.00–1.00 seconds his fingers tighten gradually at the existing grip point; his breath becomes shallow while his gaze stays toward the unknown off-screen distance and his lips stay closed. From 1.00–5.00 seconds he simply holds the tighter grip for a clean edit point. Nearby brazier light warms only a limited part of his face against cool night ambience; far fire does not become a face light. No shout, turn, run, halberd swing, enemy reveal, text, black screen, or visible door impact. The impact and hard cut to black are added in post-production after the first second.
overall_soundscape: Sparse wall-top wind and restrained breathing only; the single door impact will be added in post-production, not repeated here.
non_diegetic_music: N/A
```

验收：一秒内清晰读出握力变化；末尾剪切后在后期叠“公元311年，洛阳陷落。”与“公元316年，西晋灭亡。”
