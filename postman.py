from datetime import datetime, timedelta

import ccxt
from ccxt import Exchange
import pandas as pd
from pandas import DataFrame


class Binance(Exchange):
    def __init__(self):
        super(Binance, self).__init__()
        self.exchange = ccxt.binance(
            {
                "apiKey": "8KC85Aq2hOAnJYaec0wjJjEWMJ6XeBqpN70uVx60Eew4n71h8isRvt7J7T6yShoJ",
                "secret": "0H6DapVskebsGuIC0VAlxvlDMuPhw8VWBvCnfrmKp4yHWba0sBzaZ4ypIc4JfiOZ"
            }
        )
        self.kines = {}

    def price_monitoring(self, set_price):
        """
        如果价格超过设定的价格发出警报
        :param set_price: 预设的价格
        :return: 警报消息
        """

    def fetch_bars(self, symbol: str, timeframe: str, limit: int) -> DataFrame:
        """
        获取币种价格信息
        :param limit: 返回bars数量
        :param timeframe: '1m','5m'
        :param symbol: 例如BTC/USDT
        :return: DateFrame
        """
        data = self.exchange.fetch_ohlcv(symbol=symbol, timeframe=timeframe, limit=limit)
        df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
        # 交易所返回的是时间戳格式，要转化为北京时间datetime格式要在utc时间上加8个小时
        df["timestamp"] = df["timestamp"].apply(
            lambda timestamp: datetime.strftime(datetime.fromtimestamp(int(timestamp) / 1000) + timedelta(hours=8),
                                                '%Y-%m-%d %H:%M:%S'))
        return df

    def fetch_kines(self, symbol: str) -> str:
        """
        获取k线
        :param symbol: btc/usdt
        :return: 一个字符串包含high,low,bid,ask,close,open,datetime,symbol,average,last
        """
        self.kines = self.exchange.fetch_ticker(symbol=symbol)
        return "%s--最新价:%s--\n" \
               "--最高价:%s--\n" \
               "--最低价:%s--\n"\
               % (self.kines.get("symbol"), self.kines.get("last"),self.kines.get("high"),self.kines.get("low"))

