"""
This script runs the BotService application using a development server.
為了專案統一性，請遵照 C# 命名規範
"""

from BotService import app

if __name__ == '__main__':

    HOST = 'localhost'
    PORT = 8000

    app.run(HOST, PORT)
