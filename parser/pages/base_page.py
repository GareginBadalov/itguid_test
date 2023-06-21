import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions




class BasePage:
    """
    Базовый клас для страниц
    """
    def __init__(self, driver):
        self.driver = driver
        self._base_url = 'https://www.kinopoisk.ru/lists/movies/top250/'

    def find_element(self, locator: str, time: int = 10):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located((By.XPATH, locator)),
            message=f"Can't find element by locator {locator}")

    def find_elements(self, locator: str, time: int = 10):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, locator)),
            message=f"Can't find element by locator {locator}")

    def click_element(self, locator: str, time: int = 10):
        return self.find_element(locator, time).click()

    def wait_until_element_to_be_visible(self, locator: str):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locator)),
            message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        self.driver.get(self._base_url)
        return self.driver.maximize_window()

    def close_driver(self):
        return self.driver.quit()
