from flask import Flask
from BotService.Commons.WebApiTemplate_MethodView import WebApiTemplate

class SampleController(WebApiTemplate):

    def __init__(self, rule: str = '/api') -> None:
        super().__init__(__name__, rule)
        self.view = SampleController.as_view(self.name)

    # 藍圖注冊
    #    self.blueprint = Blueprint(self._name + '_bp', __name__)
    #    self.blueprint.add_url_rule('/', view_func=self.view, methods=['GET'])

    # 一般注冊(Base)
    def register(self, app: Flask) -> None:
        app.add_url_rule(self.rule + '/', view_func=self.view, methods=['GET'])






    def get(self):
        return 'This is Get'

    def post(self):
        return 'This is Post'
