"""
The flask application package.
"""

from flask import Flask, jsonify

from flask_swagger_ui import get_swaggerui_blueprint
from BotService.Commons.WebApiTemplate_MethodView import WebApiTemplate

class MyFlask(Flask):
    def register(self, view: WebApiTemplate):
        view.register(self)

app = MyFlask(__name__)

from BotService.Routes import Register
Register(app)
