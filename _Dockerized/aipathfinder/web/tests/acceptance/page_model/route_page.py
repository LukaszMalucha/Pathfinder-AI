from selenium.webdriver.common.by import By

from tests.acceptance.locators.route_page import RoutePageLocators
from tests.acceptance.page_model.base_page import BasePage


class RoutePage(BasePage):

    @property
    def url(self):
        return super(RoutePage, self).url + '/pathfinder'

    @property
    def title(self):
        return self.driver.find_element(*RoutePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*RoutePageLocators.NAV_LINKS)

    @property
    def dropdown(self):
        return self.driver.find_element(*RoutePageLocators.DROPDOWN)

    @property
    def dropdown_links(self):
        return self.driver.find_elements(*RoutePageLocators.DROPDOWN_LINKS)


    @property
    def home_button(self):
        return self.driver.find_element(*RoutePageLocators.HOME_BUTTON)

    @property
    def tile_path(self):
        return self.driver.find_elements(*RoutePageLocators.TILE_PATH)













