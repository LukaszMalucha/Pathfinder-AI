from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.environment_page import EnvironmentPage
from tests.acceptance.page_model.login_page import LoginPage
from tests.acceptance.page_model.register_page import RegisterPage
from tests.acceptance.page_model.route_page import RoutePage

use_step_matcher('re')


@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation

    matching_links = [l for l in links if l.text == link_text]
    # matching_links[0].click()
    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()

@when('I click on the login')
def step_impl(context):
    page = BasePage(context.driver)
    page.login.click()


@when('I click on the dropdown menu')
def step_impl(context):
    page = BasePage(context.driver)
    page.dropdown.click()

@when('I click on the "(.*)" dropdown link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.dropdown_links
    matching_links = [l for l in links if l.text == link_text]
    matching_links[0].click()

@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = RegisterPage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('I enter "(.*)" in the "(.*)" login field')
def step_impl(context, content, field_name):
    page = LoginPage(context.driver)
    page.form_field(field_name).send_keys(content)

@when('I enter "(.*)" in the "(.*)" environment field')
def step_impl(context, content, field_name):
    page = BasePage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('I choose "(.*)" field')
def step_impl(context, field_name):
    page = BasePage(context.driver)
    page.form_field(field_name).click()


@when('I press the submit button')
def step_impl(context):
    page = RegisterPage(context.driver)
    page.submit_button.click()


@when('I press the login button')
def step_impl(context):
    page = LoginPage(context.driver)
    page.submit_button.click()



@when('I press the "BUILD THE ENVIRONMENT" button')
def step_impl(context):
    page = BasePage(context.driver)
    page.submit_button.click()

@when('I initiate pathfinder AI')
def step_impl(context):
    page = EnvironmentPage(context.driver)
    page.submit_button.click()


@when('I press the "Change Environment" button')
def step_impl(context):
    page = RoutePage(context.driver)
    page.home_button.click()