from behave import given, when, then

@then('I see "{message}"')
def title(context, message):
    element = context.browser.find_by_css('#title')
    assert element.text == message