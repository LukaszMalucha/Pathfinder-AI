from selenium.webdriver.common.by import By


class RoutePageLocators:
    TITLE = By.TAG_NAME, 'strong'
    NAV_LINKS =  By.ID, 'navigation'
    DROPDOWN = By.ID, 'user_dropdown'
    DROPDOWN_LINKS = By.ID, 'dropdown_link'
    PAGE = By.ID, 'page-index'
    HOME_BUTTON = By.ID, 'button_command'
    TILE_PATH = By.ID, 'mars_path'
