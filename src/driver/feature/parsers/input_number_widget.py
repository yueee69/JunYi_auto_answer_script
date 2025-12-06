from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from .BASE import BaseParser

class InputNumberWidgetParser(BaseParser):
    def can_handle(self, driver: WebDriver, question: dict[str], html: dict, widgets: dict) -> bool:
        if not any(k.startswith("input-number ") for k in widgets):
            return False

        return len(html["number_inputs"]) > 0

    def handle(self, driver: WebDriver, question: dict[str], html: dict, widgets: dict) -> None:
        elems = html["number_inputs"]

        for idx, elem in enumerate(elems, start=1):
            key = f"input-number {idx}"
            if key in widgets:
                elem.send_keys(str(widgets[key]["options"]["value"]))