
from flask import Flask

# 引入 Controllers
from BotService.Controllers.Samples.SampleController import SampleController
from BotService.Controllers.HomeController import HomeController
# More...

# 注冊 Controller
def Register(app: Flask) -> None:
    app.register_blueprint(SampleController, url_prefix='/api/sample')
    app.register_blueprint(HomeController, url_prefix='/api/home')
    # More...

