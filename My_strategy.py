import json
import os
from datetime import datetime, timedelta

import pandas as pd
import requests
import re #引入正则表达式
import matplotlib.pyplot as plt
from pandas import DataFrame

"""
TIME: 2022/7/20
author: mossloo
本文就ahr999指标，恐惧贪婪指标 编写定投btc策略
为什么选择定投呢？
为什么选择比特币呢？

"""


def ahr999():
    pass


"""
 恐惧&贪婪指数
"""
def fear_and_greed_index(limit:int) ->DataFrame:
    url = f"https://api.alternative.me/fng/?limit={limit}"
    response = requests.get(url)
    res = json.loads(response.content)
    df = pd.DataFrame(data=res["data"],columns=["value","value_classification","timestamp"])
    df["timestamp"] = df["timestamp"].apply(lambda timestamp: datetime.strftime(datetime.fromtimestamp(int(timestamp)),'%Y-%m-%d %H:%M:%S'))
    df = df.set_index("timestamp")
    df["value"] = df["value"].astype(int)
    df.to_csv("fear_and_greed_index.csv")
    return df

def plot_fear_and_greed():
    if not os.path.exists("fear_and_greed_index.csv"):
        fear_and_greed_index(100)
        plot_fear_and_greed()
    else:
        df = pd.read_csv("fear_and_greed_index.csv")
        plt.Figure(figsize=(12,10),dpi=80)
        plt.plot(df.index,df["value"],color="blue",linewidth=1.0,linestyle='-')
        plt.title("fear_and_greed_index")
        plt.show()

if __name__ == '__main__':
    plot_fear_and_greed()
