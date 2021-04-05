from behave import given, when, then
from hamcrest import assert_that, equal_to
from environment import find_element

@then('I see "{message}"')
def title(context, message):
    element = find_element('body', context.browser)
    assert_that(element.text, equal_to(message))