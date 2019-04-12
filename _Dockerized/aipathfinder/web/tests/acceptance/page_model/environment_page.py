from selenium.webdriver.common.by import By

from tests.acceptance.locators.environment_page import EnvironmentPageLocators
from tests.acceptance.page_model.base_page import BasePage


class EnvironmentPage(BasePage):

    @property
    def url(self):
        return super(EnvironmentPage, self).url + '/environment'

    @property
    def title(self):
        return self.driver.find_element(*EnvironmentPageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*EnvironmentPageLocators.NAV_LINKS)

    @property
    def dropdown(self):
        return self.driver.find_element(*EnvironmentPageLocators.DROPDOWN)

    @property
    def dropdown_links(self):
        return self.driver.find_elements(*EnvironmentPageLocators.DROPDOWN_LINKS)

    @property
    def form(self):
        return self.driver.find_element(*EnvironmentPageLocators.FORM_ENV)

    @property
    def submit_button(self):
        return self.driver.find_element(*EnvironmentPageLocators.SUBMIT_BUTTON)

    @property
    def tile_base(self):
        return self.driver.find_element(*EnvironmentPageLocators.TILE_BASE)

    @property
    def tile_astronauts(self):
        return self.driver.find_element(*EnvironmentPageLocators.TILE_ASTRONAUTS)

    @property
    def tile_start(self):
        return self.driver.find_element(*EnvironmentPageLocators.TILE_START)

    @property
    def tile_storms(self):
        return self.driver.find_elements(*EnvironmentPageLocators.TILE_STORM)













