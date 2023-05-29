# BotService

## Pip 失效解決辦法
### 錯誤訊息
ModuleNotFoundError: No module named 'pip._vendor.urllib3.packages'

1. 到環境： \Lib\site-packages 手動刪除 pip 開頭的文件
2. 執行：python -m ensurepip
3. 執行：python -m pip install --upgrade pip
