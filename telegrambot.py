import telepot
import os
import time


token = '1251352869:AAHY_ZiBXNjn-F1r31XufN1AMRYuNLJIUDA'
mc = '1251352869'
bot = telepot.Bot(token)

status = True

def handle(msg):
    content, chat, id = telepot.glance(msg)

    if content == 'text':
        if msg['text'] == '즐겨찾기':
            bot.sendMessage(id,'즐겨찾기 목록을 출력합니다.')
        else:
            bot.sendMessage(id, "안녕하세요! 약국 검색 프로그램입니다.")

bot.message_loop(handle)

while status ==True:
    time.sleep(10)