from flask import Flask
from BotService.Commons.WebApiTemplate_MethodView import WebApiTemplate

class MethodViewController(WebApiTemplate):

    def __init__(self, rule: str = '/api', dbgInfo: bool=False) -> None:
        super().__init__(__name__, rule, dbgInfo)
        self.view = MethodViewController.as_view(self.name)

    # 藍圖注冊
    #    self.blueprint = Blueprint(self._name + '_bp', __name__)
    #    self.blueprint.add_url_rule('/', view_func=self.view, methods=['GET'])

    # 一般注冊(Base)
    def register(self, app: Flask) -> None:
        app.add_url_rule(self.rule + '/', view_func=self.view, methods=['GET'])

    def get(self):
        return '[Get]: Method View Controller'

    def post(self):
        return '[Post]: Method View Controller'
