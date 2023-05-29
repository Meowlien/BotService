﻿from flask import jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import json

class MeowSwagger():

    def __init__(self,
            url_prefix: str='/swagger/index',
            url_suffix: str='/swagger.json'
        ) -> None:
        self.url_prefix = url_prefix
        self.url_suffix = url_suffix
        self.api_url = url_prefix + url_suffix

        self.blueprint = get_swaggerui_blueprint(self.url_prefix, self.api_url)
        self.register_local()
        self.use_swagger_template()
    
    def use_swagger_template(self, path: str='./BotService/Commons/Swaggers/swagger.json') -> None:
        self._swagger_template_path = path

    # 路由注冊
    def register_local(self) -> None:
        self.blueprint.add_url_rule(self.url_suffix, view_func=self.generate_swagger_spec)

    # 生成 swagger.json
    def generate_swagger_spec(self):
        try:
            with open(self._swagger_template_path, 'r') as data:
                swagger_content = json.load(data)
                return jsonify(swagger_content)
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")