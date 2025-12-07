from src.driver.feature.parsers.radio_answer_area import RadioAnswerAreaParser

class FakeElem:
    def __init__(self):
        self.clicked = False
    def click(self):
        self.clicked = True

class FakeDriver:
    pass

def test_can_handle_correct_structure():
    parser = RadioAnswerAreaParser()

    elems = [FakeElem(), FakeElem(), FakeElem()]
    html = {"radio_labels": elems}

    question = {
        "question": {
            "answerArea": {
                "options": {
                    "choices": [
                        {"content": "A"}, {"content": "B"}, {"content": "C"}
                    ]
                }
            }
        }
    }

    assert parser.can_handle(FakeDriver(), question, html, {}) is True


def test_handle_clicks_correct_answer():
    parser = RadioAnswerAreaParser()

    elems = [FakeElem(), FakeElem(), FakeElem()]
    html = {"radio_labels": elems}

    question = {
        "question": {
            "answerArea": {
                "options": {
                    "choices": [
                        {"content": "A", "correct": False},
                        {"content": "B", "correct": True},
                        {"content": "C", "correct": False},
                    ]
                }
            }
        }
    }

    parser.handle(FakeDriver(), question, html, {})

    assert elems[1].clicked is True
