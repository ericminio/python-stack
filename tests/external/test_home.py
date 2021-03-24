from splinter import Browser

def test_home_greetings(browser, base_url):
    browser.visit(base_url + '/')
    element = browser.find_by_css('#title').first

    assert element.value == 'hello world'

def test_home_lists_users(browser, base_url):
    browser.visit(base_url + '/')
    
    element = browser.find_by_css('#users #user-1').first
    assert element.text == 'Alice'

    element = browser.find_by_css('#users #user-2').first
    assert element.text == 'Bob'
