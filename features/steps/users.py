from behave import given, when, then
from hamcrest import assert_that, equal_to, is_not
from environment import find_element

@then('I see the user list')
def users(context):
    element = find_element('#users', context.browser)
    assert_that(element, is_not(equal_to(None)))

@then('I see the first user is "{name}"')
def first_user(context, name):
    element = find_element('#users .user:nth-child(1)', context.browser)
    assert_that(element.text, equal_to(name))

@then('I see the second user is "{name}"')
def second_user(context, name):
    element = find_element('#users .user:nth-child(2)', context.browser)
    assert_that(element.text, equal_to(name))

@then('I don\'t see the user list')
def nousers(context):
    elements = find_element('#users', context.browser)
    assert_that(elements, equal_to(None))
