from splinter import Browser

def test_home(browser, base_url):
    browser.visit(base_url + '/')
    element = browser.find_by_css('#title').first

    assert element.value == 'hello world'
