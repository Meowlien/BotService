# from BotService
"""
The flask application package.
"""
from flask import Flask, jsonify
from BotService.Commons.MeowFlask import MeowFlask
from BotService.Routes import Register

# 創建 app 實體
app = MeowFlask(__name__)

# 注冊
Register(app)
