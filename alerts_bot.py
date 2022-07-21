from typing import Union, Any

import telebot


class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot("5431491320:AAFlOQ3LYlTXA6qnZyw10t0dC-aixN33iDQ")
        self.chat_id: str = "5345982141"

    def send_message(self, message: str, chat_id: str) -> None:
        self.bot.send_message(text=message, chat_id=chat_id)

    def send_photo(self, photo: str, chat_id: str) -> None:
        """
        发送图片
        :param photo: 图片的相对路径地址或者url地址
        :param chat_id: 接受方用户id
        :return: None
        """
        if photo.startswith("http"):
            self.bot.send_photo(photo=photo, chat_id=chat_id)
        else:
            with open(photo, "rb") as f:
                byte = f.read()
                self.bot.send_photo(photo=byte, chat_id=chat_id)

    def send_audio(self, audio: Union[Any, str], chat_id: str):
        """
        发送音频
        :param audio: 视频的相对路径地址或者url地址
        :param chat_id: 接受方用户id
        :return: None
        """
        if audio.startswith("http"):
            self.bot.send_audio(audio=audio, chat_id=chat_id)
        else:
            with open(audio, "rb") as f:
                byte = f.read()
                self.bot.send_audio(audio=byte, chat_id=chat_id)

    def send_video(self, video: Union[Any, str], chat_id: str):
        """
        发送音频
        :param video: 视频的相对路径地址或者url地址
        :param chat_id: 接受方用户id
        :return: None
        """
        if video.startswith("http"):
            self.bot.send_video(video=video, chat_id=chat_id)
        else:
            with open(video, "rb") as f:
                byte = f.read()
                self.bot.send_video(video=byte, chat_id=chat_id)


