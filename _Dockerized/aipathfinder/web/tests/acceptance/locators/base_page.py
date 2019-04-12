from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME, 'strong'
    NAV_LINKS =  By.ID, 'navigation'
    DROPDOWN = By.ID, 'trigger'
    DROPDOWN_LINKS = By.ID, 'dropdown_link'
    PAGE = By.ID, 'page-index'
    FORM_ENV = By.ID, 'form-env'
    SUBMIT_BUTTON = By.ID, 'submit-button'