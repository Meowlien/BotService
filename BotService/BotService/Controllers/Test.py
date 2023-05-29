

# 定義處理函式
def get_pets():
    # 處理 GET /pets 路由的邏輯
    return "OpenApi Tester"

# 注冊處理函式
def rrr(app):
    app.add_url_rule('/pets', 'get_pets', get_pets, methods=['GET'])