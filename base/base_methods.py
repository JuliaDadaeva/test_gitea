from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import *


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.basic_url = BASIC_URL

    def find_element_for_click(self, selector: tuple, time=10):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(selector))

    def find_element_presence(self, selector: tuple, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(selector))

    def go_to_site(self, url):
        self.driver.get(url)
