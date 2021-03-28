from behave import fixture, use_fixture
from splinter import Browser

@fixture
def selenium_browser_chrome(context):
    browser = Browser('firefox', headless=True)
    context.browser = browser
    yield context.browser
    context.browser.quit()

def before_all(context):
    use_fixture(selenium_browser_chrome, context)
    
