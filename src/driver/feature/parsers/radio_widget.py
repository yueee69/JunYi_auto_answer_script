from selenium.webdriver.remote.webdriver import WebDriver

from .BASE import BaseParser


class RadioWidgetParser(BaseParser):
    def extract_radio_choices(self, widgets: dict):
        for key, widget in widgets.items():
            if widget.get("type") == "radio":
                return widget["options"]["choices"]
        return None

    def can_handle(self, driver: WebDriver, question: dict, html: dict, widgets: dict) -> bool:
        choices = self.extract_radio_choices(widgets)
        if not choices:
            return False

        return len(html["radio_labels"]) == len(choices)

    def handle(self, driver: WebDriver, question: dict, html: dict, widgets: dict) -> None:
        choices = self.extract_radio_choices(widgets)
        if not choices:
            return

        elems = html["radio_labels"]

        for idx, choice in enumerate(choices):
            if choice.get("correct") is True:
                elems[idx].click()
