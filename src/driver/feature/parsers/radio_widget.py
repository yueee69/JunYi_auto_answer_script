from selenium.webdriver.remote.webdriver import WebDriver

from .BASE import BaseParser
import re

class RadioWidgetParser(BaseParser):
    def extract_radio_choices(self, question: dict):
        widget_sets = [
            question.get("question", {}).get("question", {}).get("widgets", {}),
            question.get("question", {}).get("widgets", {}),
            question.get("widgets", {})
        ]

        for widgets in widget_sets:
            if not isinstance(widgets, dict):
                continue

            for key, obj in widgets.items():
                if re.match(r"radio\s+\d+", key):
                    try:
                        return obj["options"]["choices"]
                    except KeyError:
                        continue

        return None

    def can_handle(self, driver: WebDriver, question: dict, html: dict, widgets: dict) -> bool:
        choices = self.extract_radio_choices(question)
        return choices is not None and len(html["radio_labels"]) == len(choices)

    def handle(self, driver: WebDriver, question: dict, html: dict, widgets: dict) -> None:
        choices = self.extract_radio_choices(question)
        if not choices:
            return

        elems = html["radio_labels"]

        for idx, choice in enumerate(choices):
            if choice.get("correct") is True:
                elems[idx].click()
