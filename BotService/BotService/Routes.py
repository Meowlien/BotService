# from BotService.Routes

from BotService.Commons.MeowFlask import MeowFlask

from BotService.Commons.Swaggers.swagger import MeowSwagger as Swagger
from BotService.Controllers.Samples.MethodViewController import MethodViewController as mv_Sample
from BotService.Controllers.Samples.BlueprintController import BlueprintController as bp_Sample

# 注冊 Controller
def Register(app: MeowFlask) -> None:

    # Basic Arguments
    show_debug_info = True

    # 前置-注冊
    app.register_blueprint(Swagger(         '/api/swagger', dbgInfo=show_debug_info).blueprint) # OpenApi

    # 範例-注冊
    app.register(mv_Sample(                 '/api/sample/methodView', show_debug_info))
    app.register_blueprint(bp_Sample(       '/api/sample/blueprint', show_debug_info))
    
    # 一般-注冊

