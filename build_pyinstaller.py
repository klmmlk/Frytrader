"""
PyInstaller 打包脚本
"""
import subprocess
import sys
import os

def build():
    """使用 PyInstaller 打包"""
    # 获取当前目录（项目根目录）
    current_dir = os.path.dirname(os.path.abspath(__file__))

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--name=ths_api",
        "--console",
        "--clean",
        "--noconfirm",
        f"--add-data=.env;.",
        # 添加所有 Python 模块（作为数据文件）
        f"--add-data=api.py;.",
        f"--add-data=trader.py;.",
        f"--add-data=models.py;.",
        f"--add-data=main.py;.",
        # 隐藏导入
        "--hidden-import=api",
        "--hidden-import=trader",
        "--hidden-import=models",
        "--hidden-import=main",
        "--hidden-import=easytrader",
        # uvicorn 相关
        "--hidden-import=uvicorn.logging",
        "--hidden-import=uvicorn.loops",
        "--hidden-import=uvicorn.protocols",
        "--hidden-import=uvicorn.protocols.http",
        "--hidden-import=uvicorn.protocols.http.auto",
        "--hidden-import=uvicorn.quic",
        "--hidden-import=uvicorn.lifespan.on",
        # 其他依赖
        "--hidden-import=pydantic",
        "--hidden-import=pydantic_settings",
        "--hidden-import=starlette",
        "--hidden-import=starlette.responses",
        "--hidden-import=starlette.middleware.cors",
        "--hidden-import=dotenv",
        # 收集 easytrader 所有模块
        "--collect-all=easytrader",
        # 入口文件改为 startup.py
        "startup.py"
    ]

    print("=" * 60)
    print("开始打包...")
    print("=" * 60)
    print(f"工作目录: {current_dir}")
    print(f"命令: {' '.join(cmd)}")
    print("=" * 60)

    try:
        subprocess.run(cmd, check=True, cwd=current_dir)
        print("\n" + "=" * 60)
        print("✅ 打包成功！")
        print(f"可执行文件: {os.path.join(current_dir, 'dist', 'ths_api.exe')}")
        print("=" * 60)
    except subprocess.CalledProcessError as e:
        print("\n" + "=" * 60)
        print(f"❌ 打包失败: {e}")
        print("=" * 60)

if __name__ == "__main__":
    build()