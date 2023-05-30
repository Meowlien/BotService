from atexit import register
from flask import Flask
from flask import Blueprint
from flask.views import MethodView
from BotService.Logging.Logger import Log

class WebApiTemplate(Blueprint):

    def __init__(self, name: str='_bp`', name_import: str=__name__, url_prefix=None, dbgInfo: bool=False) -> None:
        super().__init__(name, name_import, url_prefix=url_prefix)
        self.register_local()
        if dbgInfo == True:
            Log.LogInfomation("Registered >> '" + self.url_prefix + "'")

    def register_local(self) -> None:
        pass
