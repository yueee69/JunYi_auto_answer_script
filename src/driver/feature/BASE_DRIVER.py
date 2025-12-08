import time
import hashlib

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseDriver:
    def __init__(self, driver):
        self.driver = driver()

    def wait_visible(self, by, value, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def wait_clickable(self, by, value, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def click(self, by, value):
        self.wait_clickable(by, value).click()

    def fill(self, by, value, text):
        elem = self.wait_visible(by, value)
        elem.clear()
        elem.send_keys(text)

    def wait_options(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_elements(
                By.CSS_SELECTOR,
                "[data-testid='perseus-radio-widget'] label"
            )
        )

    def click_option(self, index):
        options = self.wait_options()
        options[index].click()

    def skip_ad(self):
        for _ in range(2):
            try:
                self.click(By.CLASS_NAME, "MuiButton-containedPrimary")
            except:
                break

    def finish_quetion(self):
        self.click(By.ID, "watch-report-directly-input-big-screen")
        try:
            self.click(By.CSS_SELECTOR, ".swal2-confirm")
        except:
            pass

    def submit_question(self):
        self.click(By.ID, "check-answer-button")

        try:
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.ID, "next-question-button"))
            )

            WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(By.ID, "next-question-button").is_enabled()
            )

            self.driver.find_element(By.ID, "next-question-button").click()
            return

        except:
            pass 

        try:
            self.click(By.ID, "check-answer-button")
        except:
            pass

    def get_question_text(self):
        elem = self.driver.find_element(By.CSS_SELECTOR, ".perseus-renderer")
        return elem.text.strip()

    def wait_for_question_text_change(self, old_text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(By.CSS_SELECTOR, ".perseus-renderer").text.strip() != old_text
        )
