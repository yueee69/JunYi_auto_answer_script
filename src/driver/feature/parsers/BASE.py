from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver

class BaseParser(ABC):

    @abstractmethod
    def can_handle(self, driver: WebDriver, question: dict[str], html: dict, widgets: dict) -> bool:
        pass

    @abstractmethod
    def handle(self, driver: WebDriver, question: dict[str], html: dict, widgets: dict) -> None:
        pass