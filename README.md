# Ebbinghaus-Trello

[中文版](https://github.com/anhenghuang/ebbinghaus-trello/blob/main/README_CN.md)

Ebbinghaus-Trello is a tool to refresh your memory based on The Ebbinghaus Forgetting Curve.

<div  align="center">    
<img width="50%" src="https://raw.githubusercontent.com/anhenghuang/ebbinghaus-trello/main/images/ForgettingCurve.png"/>
</div>

## 1. Usage

1. Create a trello board: https://trello.com
   - add 'board_name' to config.py
1. Get API Key
   - go to https://trello.com/app-key
   - ![screenshot_get_api_key_secret](https://raw.githubusercontent.com/anhenghuang/ebbinghaus-trello/main/images/screenshot_get_api_key_secret.png)
   - add 'api_key' and 'api_secret' to config.py
1. Get Token and Token-Secret
   - run get_token.py
   - add 'token' and 'token_secret' to config.py
1. Deploy cron job on your server

## 2. Demo

<div  align="center">    
<img width="90%" src="https://raw.githubusercontent.com/anhenghuang/ebbinghaus-trello/main/images/screenshot_Board.png"/>
</div>
