from splinter import Browser

def test_home_greetings(browser, base_url):
    browser.visit(base_url + '/')
    element = browser.find_by_css('#title').first

    assert element.value == 'hello world'

def test_home_lists_users_in_alphabetical_order(browser, base_url):
    browser.visit(base_url + '/')
    
    element = browser.find_by_css('#users .user:nth-child(1)').first
    assert element.text == 'Alice'

    element = browser.find_by_css('#users .user:nth-child(2)').first
    assert element.text == 'Bob'


def test_home_user_list_discloses_database_id(browser, base_url):
    browser.visit(base_url + '/')
    
    element = browser.find_by_css('#user-2').first
    assert element.text == 'Alice'
