from behave import given, when, then

@given('I visit the home page')
def visit(context):
    context.browser.visit('http://nginx:8080')
    
