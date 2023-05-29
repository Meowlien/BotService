from flask import Flask
from BotService.Commons.WebApiTemplate_Blueprint import WebApiTemplate

class HomeController(WebApiTemplate):

    def __init__(self,
        url_prefix=None
    ) -> None:
        super().__init__(
            name = self.__class__.__name__,
            name_import = __name__.replace('.', '_') + '_bp',
            url_prefix = url_prefix
        )

    # 路由注冊
    def register_local(self) -> None:
        self.add_url_rule('/', view_func=self.index) # 導向指定方法
        # More...

    def index(self):
        return 'This is Home Index For HomeController'