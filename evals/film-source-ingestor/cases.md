# Film Source Ingestor Cases

## Case 1｜长篇小说部分读取

- 输入只有前十章可读，结局在未提供章节。
- 应输出 `PARTIAL`、明确未读范围，不根据简介或常识补结局，不进入完整改编判断。

## Case 2｜多版本剧本

- 同一场景存在初稿和修订稿。
- 应分别登记版本与差异，不混合对白、事件和人物状态；需要用户决定主版本时只问该问题。

## Case 3｜历史小说改编

- 原作写到真实人物和历史事件。
- 应把原作内容标为 Source Evidence，并把历史真实性问题交给 Research，不能直接标 `CONFIRMED`。

## Case 4｜人物说法与叙述冲突

- 角色声称某事件发生，但后文叙述否定。
- 应区分 `CHARACTER_BELIEF` 与 `SOURCE_EVENT / NARRATOR_CLAIM`，保留冲突和定位。

## Case 5｜短想法

- 用户只提供两句话原创构思。
- 应判断无需建立 Source Intake，直接路由 Project Direction，不制造不必要文件。
