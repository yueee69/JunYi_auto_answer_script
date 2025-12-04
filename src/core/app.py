import os

from utils.toolkit import Tool
from driver.main_driver import MainHandler

def main():
    os.system('chcp 65001')
    print('\n均一網站\n>>> https://www.junyiacademy.org/\n')

    user_input = input('請輸入測驗網址(https://www.junyiacademy.org/XXXXXXXXXXXXXXXX)\n')
    url = Tool.get_format_url(user_input)

    handler = MainHandler(url)
    handler.run()