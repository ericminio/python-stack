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
        let elements = [
            'hw-home',
            'hw-users'
        ];      
        let search = (selector, dom)=>{ 
            let candidate = dom.querySelector(selector); 
            if (candidate) { 
                return candidate;
            } 
            else { 
                let children = [];
                for (let k=0; k < elements.length; k++) {
                    let name = elements[k];
                    let components = dom.querySelectorAll(name);
                    for (let j=0; j < components.length ; j++) {
                        children.push(components[j].shadowRoot);
                    }
                }
                for (let i=0; i < children.length; i++) {
                    let child = children[i];
                    let element = search(selector, child);
                    if (element) { return element; }
                }
                return null;
            }   
        };
        return search('{what}', document)
    """.replace("{what}", selector)
    return browser.execute_script(search)
