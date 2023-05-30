# from Program
"""
This script runs the BotService application using a development server.
"""
import configparser
from BotService import app

# 設定檔
config = configparser.ConfigParser()
config.read('settings.ini') # 讀取-設定檔
#config.get('欄位', '變數名稱')

# 主程式
if __name__ == '__main__':

    HOST = config.get('Service', 'Host')
    PORT = config.get('Service', 'Port')

    app.run(HOST, PORT)
