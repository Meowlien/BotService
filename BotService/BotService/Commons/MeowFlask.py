from flask import Flask
from BotService.Commons.WebApiTemplate_MethodView import WebApiTemplate

class MeowFlask(Flask):

    # override
    def register(self, view: WebApiTemplate) -> None:
        view.register(self)






