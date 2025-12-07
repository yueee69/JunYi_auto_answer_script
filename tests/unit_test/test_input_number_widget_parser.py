from src.driver.feature.parsers.input_number_widget import InputNumberWidgetParser
from tests.fake_driver import FakeDriver, FakeElement

def test_input_number_can_handle():
    parser = InputNumberWidgetParser()

    elems = [FakeElement(), FakeElement()]

    widgets = {
        "input-number 1": {"options": {"value": 11}},
        "input-number 2": {"options": {"value": 22}},
    }

    question = {
        "question": {
            "question": {"widgets": widgets}
        }
    }

    html = {"number_inputs": elems, "radio_labels": []}

    assert parser.can_handle(FakeDriver(), question, html, widgets) is True


def test_input_number_handle_fills_values():
    parser = InputNumberWidgetParser()

    elems = [FakeElement(), FakeElement()]
    widgets = {
        "input-number 1": {"options": {"value": 11}},
        "input-number 2": {"options": {"value": 22}},
    }
    question = {"question": {"question": {"widgets": widgets}}}

    html = {"number_inputs": elems, "radio_labels": []}

    parser.handle(FakeDriver(), question, html, widgets)

    assert elems[0].text == "11"
    assert elems[1].text == "22"
