from BotService import MyFlask

from BotService.Commons.Swaggers.swagger import MeowSwagger as Swagger
from BotService.Controllers.HomeController import HomeController as bp_Home
from BotService.Controllers.Samples.SampleController import SampleController as mv_Sample

# 注冊 Controller
def Register(app: MyFlask) -> None:

    # 前置-注冊
    app.register_blueprint(Swagger('/api/swagger').blueprint) # OpenApi
    # 一般-注冊
    app.register(mv_Sample(rule='/api/sample'))
    app.register_blueprint(bp_Home(url_prefix='/api/home'))
    
