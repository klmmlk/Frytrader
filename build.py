"""
Nuitka 打包脚本
用于将 FastAPI 应用打包成单个可执行文件
"""

import os
import subprocess
import sys

def build_with_nuitka():
    """使用 Nuitka 打包应用"""

    # 项目根目录
    project_root = os.path.dirname(os.path.abspath(__file__))

    # Nuitka 命令
    cmd = [
        sys.executable,  # 当前 Python 解释器
        "-m", "nuitka",

        # ===== 基本信息 =====
        "--standalone",  # 独立可执行文件
        "--onefile",  # 打包成单个 exe

        # ===== 入口文件 =====
        f"--main={os.path.join(project_root, 'main.py')}",

        # ===== 输出配置 =====
        "--output-dir=dist",  # 输出目录
        "--output-filename=ths_api.exe",  # 输出文件名

        # ===== 包含资源 =====
        "--include-data-files=.env=.env",  # 包含 .env 配置文件

        # ===== 依赖包含 =====
        "--include-module=fastapi",
        "--include-module=uvicorn",
        "--include-module=pydantic",
        "--include-module=pydantic_settings",
        "--include-module=easytrader",

        # ===== 优化选项 =====
        "--follow-imports",  # 跟随所有导入
        "--include-package-data=app",  # 包含 app 包的数据文件

        # ===== Windows 特定选项 =====
        "--windows-console-mode=force",  # 显示控制台（方便调试，生产环境可改为 disable）
        # "--windows-icon-from-ico=icon.ico",  # 如果有图标文件，取消注释此行

        # ===== 性能优化 =====
        "--lto=no",  # 关闭链接时优化（加快编译速度）

        # ===== 其他选项 =====
        "--assume-yes-for-downloads",  # 自动确认下载依赖
        "--show-progress",  # 显示编译进度
        "--show-memory"  # 显示内存使用
    ]

    print("=" * 60)
    print("开始使用 Nuitka 打包应用...")
    print("=" * 60)
    print(f"命令: {' '.join(cmd)}")
    print("=" * 60)

    try:
        # 执行打包命令
        subprocess.run(cmd, check=True)
        print("\n" + "=" * 60)
        print("✅ 打包成功！")
        print(f"可执行文件位置: {os.path.join(project_root, 'dist', 'ths_api.exe')}")
        print("=" * 60)
    except subprocess.CalledProcessError as e:
        print("\n" + "=" * 60)
        print("❌ 打包失败！")
        print(f"错误信息: {e}")
        print("=" * 60)
        sys.exit(1)
    except Exception as e:
        print("\n" + "=" * 60)
        print("❌ 发生未知错误！")
        print(f"错误信息: {e}")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    build_with_nuitka()