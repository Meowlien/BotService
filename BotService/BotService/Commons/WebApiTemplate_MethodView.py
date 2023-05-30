from flask import Flask
from flask import Blueprint
from flask.views import MethodView
from BotService.Logging.Logger import Log

class WebApiTemplate(MethodView):

    # 構建式
    def __init__(self, name: str='_view`', rule: str=None, dbgInfo: bool=False) -> None:
        super().__init__()
        self.name = name.replace('.', '_') + '_view'
        self.rule = rule
        if dbgInfo == True:
            Log.LogInfomation("Registered >> '" + self.rule + "'")

    @property
    def view(self):
        return self._view

    @view.setter
    def view(self, view):
        self._view = view

    @property
    def blueprint(self):
        return self._blueprint

    @blueprint.setter
    def blueprint(self, blueprint):
        self._blueprint = blueprint

    # 一般路由注冊
    def register(self, app: Flask) -> None:
        pass
