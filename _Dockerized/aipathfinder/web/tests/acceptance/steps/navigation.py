from behave import *
from selenium import webdriver

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.environment_page import EnvironmentPage
from tests.acceptance.page_model.login_page import LoginPage
from tests.acceptance.page_model.register_page import RegisterPage
from tests.acceptance.page_model.route_page import RoutePage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')  ## path to chromedriver
    page = BasePage(context.driver)
    context.driver.get(page.url)


@given('I am on the register page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = RegisterPage(context.driver)
    context.driver.get(page.url)


@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = LoginPage(context.driver)
    context.driver.get(page.url)


@then('I am on the homepage')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.driver.current_url == expected_url


@then('I am on the register page')
def step_impl(context):
    expected_url = RegisterPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the login page')
def step_impl(context):
    expected_url = LoginPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the environment page')
def step_impl(context):
    expected_url = EnvironmentPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the route page')
def step_impl(context):
    expected_url = RoutePage(context.driver).url
    assert context.driver.current_url == expected_url