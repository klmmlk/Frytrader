from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings, SettingsConfigDict
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

from api import router
from trader import TraderClient


class Settings(BaseSettings):
    """配置类"""
    ths_path: str = ""
    host: str = "0.0.0.0"
    port: int = 8000
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


# 加载环境变量
load_dotenv()

# 创建配置实例
settings = Settings()

# 全局交易客户端实例
trader_client = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    global trader_client
    # 启动时
    try:
        trader_client = TraderClient(exe_path=settings.ths_path)
        print("✅ 交易客户端初始化成功")
    except Exception as e:
        print(f"❌ 交易客户端初始化失败: {e}")

    yield

    # 关闭时
    if trader_client:
        print("👋 交易客户端已关闭")


# 创建 FastAPI 应用
app = FastAPI(
    title="同花顺交易 API",
    description="基于 FastAPI 和 EasyTrader 的股票交易接口",
    version="0.1.0",
    lifespan=lifespan
)
mcp= FastApiMCP(
    app
)
mcp.mount()
# 配置 CORS (允许所有来源,方便本地调用)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 注册路由
app.include_router(router, tags=["交易"])


@app.get("/", tags=["系统"])
async def root():
    """根路径"""
    return {
        "message": "同花顺交易 API",
        "version": "0.1.0",
        "docs": "/docs"
    }


@app.get("/health", tags=["系统"])
async def health_check():
    """健康检查"""
    client_ready = trader_client is not None
    return {
        "status": "healthy" if client_ready else "unhealthy",
        "client_connected": client_ready
    }

mcp.setup_server()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=True,
        log_level=settings.log_level.lower()
    )
