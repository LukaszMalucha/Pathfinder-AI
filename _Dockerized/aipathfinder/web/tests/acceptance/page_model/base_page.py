from selenium.webdriver.common.by import By

from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)

    @property
    def dropdown(self):
        return self.driver.find_element(*BasePageLocators.DROPDOWN)

    @property
    def dropdown_links(self):
        return self.driver.find_elements(*BasePageLocators.DROPDOWN_LINKS)

    @property
    def form(self):
        return self.driver.find_element(*BasePageLocators.FORM_ENV)

    @property
    def submit_button(self):
        return self.driver.find_element(*BasePageLocators.SUBMIT_BUTTON)

    def form_field(self, name):
        return self.form.find_element(By.NAME, name)

