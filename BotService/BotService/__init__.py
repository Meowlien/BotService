"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

# 路由注冊
from BotService.Routes import Register
Register(app)
