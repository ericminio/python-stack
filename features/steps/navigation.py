from behave import given, when, then

@given('I visit the home page')
def visit(context):
    context.browser.visit('http://nginx:8080?page=home')
    
@given('I visit the users page')
def visit(context):
    context.browser.visit('http://nginx:8080?page=users')
    
