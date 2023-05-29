from atexit import register
from flask import Flask
from flask import Blueprint
from flask.views import MethodView

class WebApiTemplate(Blueprint):

    def __init__(self, name: str='_bp`', name_import: str=__name__, url_prefix=None) -> None:
        super().__init__(name, name_import, url_prefix=url_prefix)
        self.register_local()

    def register_local(self) -> None:
        pass
