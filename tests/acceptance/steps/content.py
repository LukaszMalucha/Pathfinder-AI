from behave import *
from pathlib import Path

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.environment_page import EnvironmentPage
from tests.acceptance.page_model.login_page import LoginPage
from tests.acceptance.page_model.register_page import RegisterPage
from tests.acceptance.page_model.route_page import RoutePage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@then('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content


@then('There are three buttons shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.clear_button.is_displayed()
    assert page.download_button.is_displayed()
    assert page.predict_button.is_displayed()

@then('I can see there is a register form on the page')
def step_impl(context):
    page = RegisterPage(context.driver)
    assert page.form.is_displayed()


@then('I can see there is a login form on the page')
def step_impl(context):
    page = LoginPage(context.driver)
    assert page.form.is_displayed()



@then('I can see there are all key tiles displayed')
def step_impl(context):
    page = EnvironmentPage(context.driver)
    assert page.tile_start.is_displayed()
    assert page.tile_astronauts.is_displayed()
    assert page.tile_base.is_displayed()
    assert len(page.tile_storms) == 4



@then('I can see there is a path visible')
def step_impl(context):
    page = RoutePage(context.driver)
    assert len(page.tile_path) > 2