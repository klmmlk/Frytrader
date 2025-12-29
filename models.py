from pydantic import BaseModel, Field, field_validator
from typing import Optional, Any, Dict


class BuyRequest(BaseModel):
    """买入请求"""
    stock_code: str = Field(..., description="股票代码(6位数字)", example="000001")
    price: float = Field(..., gt=0, description="委托价格", example=12.5)
    amount: int = Field(..., gt=0, description="委托数量(100的整数倍)", example=100)

    @field_validator('stock_code')
    @classmethod
    def validate_stock_code(cls, v: str) -> str:
        """验证股票代码格式"""
        if not v.isdigit() or len(v) != 6:
            raise ValueError('股票代码必须是6位数字')
        return v

    @field_validator('amount')
    @classmethod
    def validate_amount(cls, v: int) -> int:
        """验证数量必须是100的整数倍"""
        if v % 100 != 0:
            raise ValueError('委托数量必须是100的整数倍')
        return v


class SellRequest(BaseModel):
    """卖出请求"""
    stock_code: str = Field(..., description="股票代码(6位数字)", example="000001")
    price: float = Field(..., gt=0, description="委托价格", example=12.5)
    amount: int = Field(..., gt=0, description="委托数量(100的整数倍)", example=100)

    @field_validator('stock_code')
    @classmethod
    def validate_stock_code(cls, v: str) -> str:
        """验证股票代码格式"""
        if not v.isdigit() or len(v) != 6:
            raise ValueError('股票代码必须是6位数字')
        return v

    @field_validator('amount')
    @classmethod
    def validate_amount(cls, v: int) -> int:
        """验证数量必须是100的整数倍"""
        if v % 100 != 0:
            raise ValueError('委托数量必须是100的整数倍')
        return v


class CancelRequest(BaseModel):
    """撤单请求"""
    order_id: str = Field(..., description="委托单号", example="123456")


class TradeResponse(BaseModel):
    """交易响应"""
    success: bool = Field(..., description="操作是否成功")
    message: str = Field(..., description="响应消息")
    data: Optional[Any] = Field(None, description="响应数据")


class BalanceResponse(BaseModel):
    """资金余额响应"""
    success: bool = Field(..., description="操作是否成功")
    message: str = Field(..., description="响应消息")
    data: Optional[Dict[str, Any]] = Field(None, description="资金数据")


class PositionResponse(BaseModel):
    """持仓响应"""
    success: bool = Field(..., description="操作是否成功")
    message: str = Field(..., description="响应消息")
    data: Optional[list] = Field(None, description="持仓数据列表")


class OrdersResponse(BaseModel):
    """委托响应"""
    success: bool = Field(..., description="操作是否成功")
    message: str = Field(..., description="响应消息")
    data: Optional[list] = Field(None, description="委托数据列表")


class HealthResponse(BaseModel):
    """健康检查响应"""
    status: str = Field(..., description="健康状态")
    client_connected: bool = Field(..., description="客户端是否已连接")
