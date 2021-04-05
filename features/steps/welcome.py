from behave import given, when, then
from hamcrest import assert_that, equal_to

@then('I see "{message}"')
def title(context, message):
    element = context.browser.find_by_tag('body')
    assert_that(element.text, equal_to(message))