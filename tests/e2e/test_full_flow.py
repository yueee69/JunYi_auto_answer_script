import pytest
from selenium import webdriver
from src.driver.feature.UniversalDriver import UniversalDriver

def test_e2e_junyi_exam_runs_without_error():
    driver = webdriver.Chrome()

    url = "https://www.junyiacademy.org/exam/227105cfb60542b7a7292db0a81c6873"

    fake_answer = [{
        "question": {
            "question": {
                "widgets": {
                    "radio 100": {
                        "options": {
                            "choices": [
                                {"content": "(A) fake", "correct": False},
                                {"content": "(B) fake", "correct": True}
                            ]
                        }
                    }
                }
            }
        }
    }]

    uni = UniversalDriver(lambda: driver, url, fake_answer)

    try:
        uni.run()
        success = True
    except Exception as e:
        success = False
        print("E2E crashed:", e)

    assert success is True, "UniversalDriver.run() crashed during E2E execution"

    assert "均一教育平台" in driver.title, "Driver did not load the expected exam page"

    try:
        _ = driver.title  
        session_ok = True
    except:
        session_ok = False

    assert session_ok, "WebDriver session was unexpectedly closed"

    driver.quit()
