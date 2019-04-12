from selenium.webdriver.common.by import By


class EnvironmentPageLocators:
    TITLE = By.TAG_NAME, 'strong'
    NAV_LINKS =  By.ID, 'navigation'
    DROPDOWN = By.ID, 'user_dropdown'
    DROPDOWN_LINKS = By.ID, 'dropdown_link'
    PAGE = By.ID, 'page-index'
    FORM_ENV = By.ID, 'form-path'
    SUBMIT_BUTTON = By.ID, 'button_command'
    TILE_BASE = By.ID, 'mars_base'
    TILE_ASTRONAUTS = By.ID, 'mars_astronauts'
    TILE_START = By.ID, 'start_location'
    TILE_STORM = By.ID, 'mars_storm'
