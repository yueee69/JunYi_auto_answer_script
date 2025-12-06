from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from .BASE import BaseParser

class RadioAnswerAreaParser(BaseParser):
    def can_handle(self, driver: WebDriver, question: dict[str], html: dict, widgets: dict) -> bool:
        try:
            choices = question["question"]["answerArea"]["options"]["choices"]
        except KeyError:
            return False

        return len(html["radio_labels"]) == len(choices)


    def handle(self, driver: WebDriver, question: dict[str], html: dict, widgets: dict) -> None:
        elems = html["radio_labels"]
        choices = question["question"]["answerArea"]["options"]["choices"]

        for idx, choice in enumerate(choices):
            if choice.get("correct") is True:
                elems[idx].click()