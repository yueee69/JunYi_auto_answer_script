from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from .BASE import BaseParser

class InputAnswerAreaParser(BaseParser):
    def can_handle(self, driver, question, html, widgets):
        self.number_keys = [
            k for k, v in widgets.items()
            if v.get("type") == "input-number" and "value" in v.get("options", {})
        ]
        if not self.number_keys:
            return False

        return len(html["number_inputs"]) == len(self.number_keys)


    def handle(self, driver, question, html, widgets):
        elems = html["number_inputs"]

        number_keys = sorted(self.number_keys, key=lambda x: int(x.split()[1]))

        for elem, key in zip(elems, number_keys):
            options = widgets[key]["options"]
            value = options["value"]

            elem.clear()
            elem.send_keys(str(value))
