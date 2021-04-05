from behave import fixture, use_fixture
from splinter import Browser

@fixture
def selenium_browser_chrome(context):
    browser = Browser('firefox', headless=True)
    context.browser = browser
    yield
    context.browser.quit()

def before_all(context):
    use_fixture(selenium_browser_chrome, context)
    
def find_element(selector, browser):
    search = """
        let search = (selector, dom)=>{ 
            let candidate = dom.querySelector(selector); 
            if (candidate !== null) { 
                return candidate;
            } 
            else { 
                let component = dom.querySelector('hw-home');
                if (component !== null) {
                    return search(selector, dom.querySelector('hw-home').shadowRoot);
                }
                else {
                    return null;
                }
            }   
        };
        return search('{what}', document)
    """.replace("{what}", selector)
    return browser.execute_script(search)
