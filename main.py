import sys
import os
sys.path.append(os.getcwd())

from postman import Binance
from alerts_bot import Bot


if __name__ == '__main__':
    # binance = Binance()
    bot: Bot = Bot()
    bot.send_video(video="video/hiveos 搭建转发ssl节点 教程.mp4",chat_id= bot.chat_id)
