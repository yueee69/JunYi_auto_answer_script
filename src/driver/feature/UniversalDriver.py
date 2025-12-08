import time
import selenium.webdriver as webdriver

from .BASE_DRIVER import BaseDriver
from .ParserManager import ParserManager


class UniversalDriver(BaseDriver):
    def __init__(self, driver: webdriver, url: str, answer: list[dict]):
        super().__init__(driver)
        self.url = url
        self.answer = answer

    def run(self) -> None:
        self.driver.get(self.url)
        self.driver.set_window_size(1200, 1600)
        self.driver.execute_script("document.body.style.zoom='100%'")
        self.skip_ad()

        parser_manager = ParserManager()

        for idx, question in enumerate(self.answer, start=1):
            old_text = self.get_question_text()

            parser_manager.solve_question(self.driver, question)

            if idx == len(self.answer):
                self.finish_quetion()
                break

            self.submit_question()
            self.wait_for_question_text_change(old_text)