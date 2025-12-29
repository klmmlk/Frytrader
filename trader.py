from easytrader import use
from typing import Dict, List, Optional, Any
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TraderClient:
    """EasyTrader 客户端封装"""

    def __init__(self, exe_path: str = None, host: str = "127.0.0.1"):
        """
        初始化交易客户端

        Args:
            exe_path: 同花顺 xiadan.exe 的完整路径
            host: 服务器地址
        """
        self.exe_path = exe_path
        self.client = None
        self._connect()

    def _connect(self):
        """建立连接"""
        try:
            logger.info(f"正在连接交易客户端")
            self.client = use('universal_client')
            self.client.connect(self.exe_path)
            self.client.enable_type_keys_for_editor()
            logger.info("✅ 交易客户端连接成功")
        except Exception as e:
            logger.error(f"❌ 交易客户端连接失败: {e}")
            raise

    def buy(self, stock_code: str, price: float, amount: int) -> Dict[str, Any]:
        """
        买入股票

        Args:
            stock_code: 股票代码 (6位数字)
            price: 委托价格
            amount: 委托数量 (100的整数倍)

        Returns:
            交易结果
        """
        try:
            logger.info(f"买入请求: {stock_code}, 价格: {price}, 数量: {amount}")
            result = self.client.buy(stock_code, price, amount)
            logger.info(f"买入结果: {result}")
            return {
                "success": True,
                "message": "买入委托成功",
                "data": result
            }
        except Exception as e:
            logger.error(f"买入失败: {e}")
            return {
                "success": False,
                "message": f"买入失败: {str(e)}",
                "data": None
            }

    def sell(self, stock_code: str, price: float, amount: int) -> Dict[str, Any]:
        """
        卖出股票

        Args:
            stock_code: 股票代码 (6位数字)
            price: 委托价格
            amount: 委托数量 (100的整数倍)

        Returns:
            交易结果
        """
        try:
            logger.info(f"卖出请求: {stock_code}, 价格: {price}, 数量: {amount}")
            result = self.client.sell(stock_code, price, amount)
            logger.info(f"卖出结果: {result}")
            return {
                "success": True,
                "message": "卖出委托成功",
                "data": result
            }
        except Exception as e:
            logger.error(f"卖出失败: {e}")
            return {
                "success": False,
                "message": f"卖出失败: {str(e)}",
                "data": None
            }

    def cancel(self, order_id: str) -> Dict[str, Any]:
        """
        撤销委托

        Args:
            order_id: 委托单号

        Returns:
            撤单结果
        """
        try:
            logger.info(f"撤单请求: {order_id}")
            result = self.client.cancel_entrust(order_id)
            logger.info(f"撤单结果: {result}")
            return {
                "success": True,
                "message": "撤单成功",
                "data": result
            }
        except Exception as e:
            logger.error(f"撤单失败: {e}")
            return {
                "success": False,
                "message": f"撤单失败: {str(e)}",
                "data": None
            }

    def get_balance(self) -> Dict[str, Any]:
        """
        查询资金余额

        Returns:
            资金信息
        """
        try:
            logger.info("查询资金余额")
            result = self.client.balance
            logger.info(f"资金信息: {result}")
            return {
                "success": True,
                "message": "查询成功",
                "data": result
            }
        except Exception as e:
            logger.error(f"查询资金失败: {e}")
            return {
                "success": False,
                "message": f"查询失败: {str(e)}",
                "data": None
            }

    def get_positions(self) -> Dict[str, Any]:
        """
        查询持仓

        Returns:
            持仓信息
        """
        try:
            logger.info("查询持仓")
            result = self.client.position
            logger.info(f"持仓信息: {result}")
            return {
                "success": True,
                "message": "查询成功",
                "data": result
            }
        except Exception as e:
            logger.error(f"查询持仓失败: {e}")
            return {
                "success": False,
                "message": f"查询失败: {str(e)}",
                "data": None
            }

    def get_today_orders(self) -> Dict[str, Any]:
        """
        查询今日委托

        Returns:
            今日委托信息
        """
        try:
            logger.info("查询今日委托")
            result = self.client.today_entrusts
            logger.info(f"今日委托: {result}")
            return {
                "success": True,
                "message": "查询成功",
                "data": result
            }
        except Exception as e:
            logger.error(f"查询今日委托失败: {e}")
            return {
                "success": False,
                "message": f"查询失败: {str(e)}",
                "data": None
            }

    def get_today_trades(self) -> Dict[str, Any]:
        """
        查询今日成交

        Returns:
            今日成交信息
        """
        try:
            logger.info("查询今日成交")
            result = self.client.today_trades
            logger.info(f"今日成交: {result}")
            return {
                "success": True,
                "message": "查询成功",
                "data": result
            }
        except Exception as e:
            logger.error(f"查询今日成交失败: {e}")
            return {
                "success": False,
                "message": f"查询失败: {str(e)}",
                "data": None
            }
