import requests
from typing import Type
import selenium.webdriver as webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from config.manager import MainManager
from .feature.UniversalDriver import UniversalDriver

class MainHandler:
    def __init__(self, url: str):
        self.url = url
        self.manager = MainManager()
        self.driver: Type[WebDriver] = self.__get_driver()
        self.answer = self.__get_answer()
        
    def __get_driver(self) -> Type[WebDriver]:
        maps = {
            "chrome": webdriver.Chrome,
            "edge": webdriver.Edge
        }
        driver = maps.get(self.manager.driver_manager.get_driver(), None)
        if driver is None:
            raise ValueError("Unsupported driver! ensure driver is chrome or edge\nThis error from MainHandler.__get_driver.")
        
        return driver
    
    def __get_answer(self) -> list[dict]:
        answer = requests.get(self.manager.answer_manager.get_answer_url(self.url)).json()["data"] #一定會200
        if len(answer) == 0:
            raise ValueError("Failed to get answers from the provided URL.")

        return answer

    def run(self) -> None:
        url = self.manager.answer_manager.get_base_url(self.url, complete = True)
        driver = UniversalDriver(self.driver, url, self.answer)
        driver.run()