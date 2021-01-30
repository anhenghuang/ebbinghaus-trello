# Ebbinghaus-Trello

Ebbinghaus-Trello 是一个基于记忆曲线的定期回顾工具，它完全基于非常易用的敏捷管理工具 [Trello](https://trello.com) 的公开 API。

<div  align="center">    
<img width="50%" src="https://raw.githubusercontent.com/anhenghuang/ebbinghaus-trello/main/images/ForgettingCurve.png"/>
</div>

在记忆曲线的每个关键节点，Ebbinghaus-Trello 都会及时把对应的「卡片」移动到「复习列表」中。您只需要：

- 将当日新完成的卡片创建在「完成列表」
- 将当日完成复习的卡片从「复习列表」移动到「完成列表」

Ebbinghaus-Trello 会自动化的：

- 每天 23：30 分，将当日完成的卡片从「完成列表」自动移动到「记忆仓库」，同时自动打上
- 每天 00：30 分，检查「记忆仓库」中的每张卡片，如果今天需要复习，就会自动移动到「复习列表」中。
   - 是否需要复习基于我对记忆曲线的概括性公式：
      - date_diff(今天，上次记忆的日期) = 上次记忆的日期 + 2^(记忆次数-1) 天

## 1. 使用方法

1. 在 Trello 注册并建立一个看板(board) [Trello](https://trello.com)
   - 把看板的名称 'board_name' 配置到 config.py 中
1. 获取 Trello 的 API Key：
   - 在登录的状态下，打开网址： https://trello.com/app-key
   - ![screenshot_get_api_key_secret](https://raw.githubusercontent.com/anhenghuang/ebbinghaus-trello/main/images/screenshot_get_api_key_secret.png)
   - 把 'api_key' 和 'api_secret' 配置到 config.py 中
1. 获取 Token and Token-Secret
   - 完成上述配置文件后，运行 get_token.py，按照提示操作
   - 把得到的 'token' 和 'token_secret' 配置到 config.py 中
1. 将定时任务部署到任意服务环境中即可

## 2. 示例

<div  align="center">    
<img width="90%" src="https://raw.githubusercontent.com/anhenghuang/ebbinghaus-trello/main/images/screenshot_Board.png"/>
</div>
