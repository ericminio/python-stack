from behave import given, when, then

@given('I visit the home page')
def step_impl(context):
    context.browser.visit('http://nginx:8080')
    
@then('I see "{message}"')
def step_impl(context, message):
    element = context.browser.find_by_css('#title')
    assert element.text == message