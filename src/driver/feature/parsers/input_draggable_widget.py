from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from .BASE import BaseParser

class InputDraggableWidgetParser(BaseParser):

    def can_handle(self, driver: WebDriver, question: dict[str], html: dict, widgets: dict) -> bool:
        try:
            inner_widgets = question["question"]["question"]["widgets"]["draggable-container 1"]["options"]["widgets"]
        except KeyError:
            return False

        return len(html["number_inputs"]) > 0

    def handle(self, driver: WebDriver, question: dict[str], html: dict, widgets: dict) -> None:
        inner_widgets = question["question"]["question"]["widgets"]["draggable-container 1"]["options"]["widgets"]
        elems = html["number_inputs"]

        for idx, elem in enumerate(elems, start=1):
            key = f"input-number {idx}"
            if key in inner_widgets:
                elem.send_keys(str(inner_widgets[key]["options"]["value"]))