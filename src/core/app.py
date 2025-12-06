import os
from selenium.common.exceptions import WebDriverException, NoSuchWindowException

from utils.toolkit import Tool
from driver.main_driver import MainHandler

def main():
    os.system('chcp 65001')
    print('\n均一網站\n>>> https://www.junyiacademy.org/\n')

    user_input = input('請輸入測驗網址(https://www.junyiacademy.org/XXXXXXXXXXXXXXXX)\n')
    url = Tool.get_format_url(user_input)

    try:
        handler = MainHandler(url)
        handler.run()
    except (ValueError, WebDriverException, NoSuchWindowException):
        print("\n[INFO] 使用者已關閉瀏覽器，程式結束。")
        return

    print('\n程式已經結束，請確認分數！')
    os.system('pause')
