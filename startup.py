"""
PyInstaller 启动脚本
这个脚本作为 PyInstaller 的入口点，它会动态设置 sys.path
以确保所有模块都能被找到
"""
import sys
import os

# 获取应用程序运行目录
if getattr(sys, 'frozen', False):
    # 如果是打包后的 exe
    application_path = os.path.dirname(sys.executable)
else:
    # 如果是开发环境
    application_path = os.path.dirname(os.path.abspath(__file__))

# 将应用程序目录添加到 sys.path
# 这样 import 就能找到 api, trader, models 等模块
if application_path not in sys.path:
    sys.path.insert(0, application_path)

# 现在可以安全地导入 main
import main

if __name__ == '__main__':
    # 如果直接运行这个脚本，启动 uvicorn
    import uvicorn
    uvicorn.run(
        "main:app",
        host=main.settings.host,
        port=main.settings.port,
        reload=False,  # 打包后不需要 reload
        log_level=main.settings.log_level.lower()
    )