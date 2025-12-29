from fastapi import APIRouter, HTTPException
from typing import Dict, Any

from models import (
    BuyRequest,
    SellRequest,
    CancelRequest,
    TradeResponse,
    BalanceResponse,
    PositionResponse,
    OrdersResponse
)
from trader import TraderClient

# 创建路由器
router = APIRouter()

# 获取全局交易客户端 (在 main.py 中初始化)
def get_trader_client() -> TraderClient:
    """获取交易客户端实例"""
    from main import trader_client
    if trader_client is None:
        raise HTTPException(status_code=503, detail="交易客户端未初始化")
    return trader_client


@router.post("/buy", response_model=TradeResponse, summary="买入股票")
async def buy_stock(request: BuyRequest):
    """
    买入股票

    - **stock_code**: 股票代码(6位数字)
    - **price**: 委托价格
    - **amount**: 委托数量(必须是100的整数倍)
    """
    client = get_trader_client()
    result = client.buy(
        stock_code=request.stock_code,
        price=request.price,
        amount=request.amount
    )
    return result


@router.post("/sell", response_model=TradeResponse, summary="卖出股票")
async def sell_stock(request: SellRequest):
    """
    卖出股票

    - **stock_code**: 股票代码(6位数字)
    - **price**: 委托价格
    - **amount**: 委托数量(必须是100的整数倍)
    """
    client = get_trader_client()
    result = client.sell(
        stock_code=request.stock_code,
        price=request.price,
        amount=request.amount
    )
    return result


@router.post("/cancel", response_model=TradeResponse, summary="撤销委托")
async def cancel_order(request: CancelRequest):
    """
    撤销委托单

    - **order_id**: 委托单号
    """
    client = get_trader_client()
    result = client.cancel(order_id=request.order_id)
    return result


@router.get("/balance", response_model=BalanceResponse, summary="查询资金")
async def get_balance():
    """
    查询账户资金余额

    返回总资产、可用资金、持仓市值等信息
    """
    client = get_trader_client()
    result = client.get_balance()
    return result


@router.get("/positions", response_model=PositionResponse, summary="查询持仓")
async def get_positions():
    """
    查询账户持仓

    返回所有持仓股票的详细信息
    """
    client = get_trader_client()
    result = client.get_positions()
    return result


@router.get("/orders", response_model=OrdersResponse, summary="查询今日委托")
async def get_today_orders():
    """
    查询今日所有委托单

    返回今日所有的买入/卖出委托记录
    """
    client = get_trader_client()
    result = client.get_today_orders()
    return result


@router.get("/trades", response_model=OrdersResponse, summary="查询今日成交")
async def get_today_trades():
    """
    查询今日所有成交记录

    返回今日所有已成交的记录
    """
    client = get_trader_client()
    result = client.get_today_trades()
    return result
