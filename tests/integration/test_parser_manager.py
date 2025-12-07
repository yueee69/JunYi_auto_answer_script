import pytest
from src.driver.feature.ParserManager import ParserManager


# --- Fake Classes 用來模擬 HTML / Driver ---
class FakeDriver:
    def find_elements(self, *a, **kw):
        return []


def test_parser_priority():
    pm = ParserManager()

    called = []

    class P1:
        def can_handle(self, driver, question, html, widgets):
            return True
        def handle(self, driver, question, html, widgets):
            called.append("P1")

    class P2:
        def can_handle(self, driver, question, html, widgets):
            return True
        def handle(self, driver, question, html, widgets):
            called.append("P2")

    pm.parsers = [P1(), P2()]

    pm.solve_question(FakeDriver(), {})

    assert called == ["P1"]


def test_no_parser_can_handle():
    pm = ParserManager()

    class P:
        def can_handle(self, driver, question, html, widgets):
            return False

    pm.parsers = [P()]

    pm.solve_question(FakeDriver(), {})



def test_parser_error_should_not_crash():
    pm = ParserManager()

    class BadParser:
        def can_handle(self, driver, question, html, widgets):
            return True
        def handle(self, driver, question, html, widgets):
            raise Exception("fail")

    pm.parsers = [BadParser()]

    pm.solve_question(FakeDriver(), {})
