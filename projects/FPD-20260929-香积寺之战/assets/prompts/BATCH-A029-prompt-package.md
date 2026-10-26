# A029 战前地形B0

2026-10-04；内置图像生成。原句柄81失效且未找到输出后重试。
父参考：assets/locations/LOC-BATTLEFIELD-001/topology-plan-v002.png。

Use case: lighting-weather. Input is locked production terrain topology. Create B0 PREBATTLE clean-air environment state by editing ONLY light and small surface wear; same exact camera viewpoint, framing, rock clusters, sparse bushes, central open combat space, right-side eastern corridor, crossing routes and all fixed terrain anchors must stay pixel-aligned as closely as possible. Subdue warm sunshine to diffuse overcast neutral gray-yellow daylight, low-saturation yellow-brown compact earth, no blue tint wash. Keep only sparse old shallow footprints and hoof marks, no fresh battle debris or bodies, no large troops, no new objects. Clear air, no fog smoke airborne dust glow or sunbeams. No new hills, roads, buildings, towers or walls. Photorealistic reusable environment state plate, not a shot composition.

第一版已归档state-b0-prebattle-v001.png；地形宏观连续，但重复蹄印微纹理过密，HOLD_GROUND_TEXTURE，不能作为B0基准。

## V2局部修订

V2仍未去除重复纹理，未通过。V3回到原拓扑父图，仅改变天光，不再要求重绘地表。

## V3单变量天光修订

结果：V1/V2/V3均已生成留档，三版重复地表微纹理问题仍在，HOLD_GROUND_TEXTURE，未计合格B0。没有运行中任务。

Use case: lighting-weather. Change ONLY the illumination and color balance of the supplied landscape photograph, from warm direct sunshine to softly diffuse neutral overcast daylight. Keep the original ground surface EXACTLY unchanged: do not repaint soil, do not invent marks, and do not add tracks. Keep every object, path, stone, bush and cart in the identical position, preserve same camera and frame. Lower orange warmth slightly while retaining earthy yellow-brown colors. Air remains completely clear. No haze, fog, dust, sunlight shafts, new detail, texture enhancement or stylization. This is the prebattle clean-light variant of the same production landscape.

Use case: precise-object-edit. Edit image 1 B0 terrain state. Change ONLY ground microtexture: REMOVE densely repeated hoof-shaped crescents, looping ridges and squiggly patterned marks covering open earth. Replace with natural mostly untracked compact dusty yellow-gray soil with sparse irregular tiny pebbles, subtle granular earth and a FEW old shallow tracks along existing paths only. No tiling or repeating procedural texture. Preserve EXACT terrain macrogeometry, camera, framing, rock clusters, bush positions, all existing routes including eastern corridor, tiny carts and neutral overcast lighting. Do not add debris, people, flags, fog, smoke or airborne dust. Photorealistic natural ground from high oblique view, prebattle, not churned battle ground.
