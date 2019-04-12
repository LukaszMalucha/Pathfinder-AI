from behave import *
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptance.locators.base_page import BasePageLocators

use_step_matcher('re')


@given('I wait for the page to load')
def step_impl(context):
    WebDriverWait(context.driver, 2).until(
        expected_conditions.visibility_of_element_located(BasePageLocators.PAGE)
    )


@given('I wait for the dropdown to load')
def step_impl(context):
    WebDriverWait(context.driver, 2).until(
        expected_conditions.visibility_of_element_located(BasePageLocators.DROPDOWN)
    )

@given('I wait for the algorithm page to load')
def step_impl(context):
    time.sleep(3)
