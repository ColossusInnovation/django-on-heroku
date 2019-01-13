from behave import *
from hamcrest import assert_that, equal_to
from splinter import Browser

use_step_matcher("re")


@when("I run the tests")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Headless chrome works normally")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    browser = Browser('chrome', headless=True)
    browser.visit(context.get_url())
    assert_that(browser.html, equal_to("<html xmlns=\"http://www.w3.org/1999/xhtml\"><head></head><body><h1>Not Found</h1><p>The requested resource was not found on this server.</p></body></html>"))
