from flask import Flask
from BotService.Commons.WebApiTemplate_Blueprint import WebApiTemplate

# 範例：藍圖控制器
class BlueprintController(WebApiTemplate):

    def __init__(self,
        url_prefix=None,
        dbgInfo: bool=False
    ) -> None:
        super().__init__(
            name=self.__class__.__name__,
            name_import=__name__.replace('.', '_') + '_bp',
            url_prefix=url_prefix,
            dbgInfo=dbgInfo
        )

    # 路由注冊
    def register_local(self) -> None:
        self.add_url_rule('/', view_func=self.index) # 導向指定方法
        # More...

    def index(self):
        return 'Blueprint Controller'