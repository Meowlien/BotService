
class Logger():

    def LogInfomation(info: str):
        print("[Debug]: " + info)

    def LogWarning(info: str):
        print("[Warning]: " + info)

    def LogError(info: str):
        print("[Error]: " + info)

# Global
Log = Logger