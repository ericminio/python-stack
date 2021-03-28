from behave import given, when, then
from hamcrest import assert_that, equal_to

@then('I see the user list')
def users(context):
    elements = context.browser.find_by_css('#users')
    assert_that(len(elements) > 0, equal_to(True))

@then('I see the first user is "{name}"')
def first_user(context, name):
    element = context.browser.find_by_css('#users .user:nth-child(1)').first
    assert_that(element.text, equal_to(name))

@then('I see the second user is "{name}"')
def second_user(context, name):
    element = context.browser.find_by_css('#users .user:nth-child(2)').first
    assert_that(element.text, equal_to(name))