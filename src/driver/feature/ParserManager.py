from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .parsers.BASE import BaseParser
from .parsers.radio_answer_area import RadioAnswerAreaParser
from .parsers.radio_widget import RadioWidgetParser
from .parsers.input_answer_area import InputAnswerAreaParser
from .parsers.input_number_widget import InputNumberWidgetParser
from .parsers.input_draggable_widget import InputDraggableWidgetParser

class ParserManager:
    def __init__(self) -> None:
        self.parsers: list[BaseParser] = [
            RadioAnswerAreaParser(),
            RadioWidgetParser(),
            InputAnswerAreaParser(),
            InputNumberWidgetParser(),
            InputDraggableWidgetParser(),
        ]

    def solve_question(self, driver: WebDriver, question: dict[str]) -> None:
        html_info = {
            "radio_labels": driver.find_elements(By.CSS_SELECTOR, '[data-testid="perseus-radio-widget"] label'),
            "number_inputs": driver.find_elements(By.CSS_SELECTOR, 'input[data-testid="perseus-input-number-widget"]'),
        }

        widgets = question.get("question", {}).get("question", {}).get("widgets", {})
        for parser in self.parsers:
            try:
                if parser.can_handle(driver, question, html_info, widgets):
                    parser.handle(driver, question, html_info, widgets)
                    return
            except:
                continue

        print("[WARN] No parser can handle this question structure.")

