import selenium.webdriver as webdriver

from .BASE_DRIVER import BaseDriver

class UniversalDriver(BaseDriver):
    def __init__(self, driver: webdriver, url: str, answer: list[dict]):
        super().__init__(driver)
        self.url = url
        self.answer = answer

    def run(self) -> None:
        self.driver.get(self.url)
        self.skip_ad()