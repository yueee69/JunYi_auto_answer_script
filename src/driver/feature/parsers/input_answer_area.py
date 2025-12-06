from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from .BASE import BaseParser

class InputAnswerAreaParser(BaseParser):
    def can_handle(self, driver: WebDriver, question: dict[str], html: dict, widgets: dict) -> bool:
        keys = [k for k in widgets.keys() if k.startswith("input-number ")]
        return len(keys) > 0 and len(html["number_inputs"]) == len(keys)

    def handle(self, driver: WebDriver, question: dict[str], html: dict, widgets: dict) -> None:
        elems = html["number_inputs"]
        
        num_keys = sorted(widgets.keys(), key = lambda x: int(x.split()[1]))

        for elem, key in zip(elems, num_keys):
            value = widgets[key]["options"]["value"]
            elem.send_keys(str(value))