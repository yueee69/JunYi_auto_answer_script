import pytest
from src.driver.feature.parsers.radio_widget import RadioWidgetParser

class FakeDriver:
    def find_elements(self, by=None, value=None):
        return ["label1", "label2", "label3"]

def test_radio_widget_can_handle():
    parser = RadioWidgetParser()

    fake_driver = FakeDriver()

    question = {
        "question": {
            "question": {
                "widgets": {
                    "radio 1": {
                        "options": {
                            "choices": [
                                {"content": "A"},
                                {"content": "B"},
                                {"content": "C"},
                            ]
                        }
                    }
                }
            }
        }
    }

    html = {
        "radio_labels": ["label1", "label2", "label3"]
    }

    widgets = {"radio 1": {}}

    assert parser.can_handle(fake_driver, question, html, widgets) == True
