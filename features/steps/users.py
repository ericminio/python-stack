from behave import given, when, then

@then('I see the user list')
def users(context):
    elements = context.browser.find_by_css('#users')
    assert len(elements) > 0

@then('I see the first user is "{name}"')
def first_user(context, name):
    element = context.browser.find_by_css('#users .user:nth-child(1)').first
    assert element.text == name

@then('I see the second user is "{name}"')
def second_user(context, name):
    element = context.browser.find_by_css('#users .user:nth-child(2)').first
    assert element.text == name