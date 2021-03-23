from tests.external.support.driver.server_driver import ServerDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from splinter import Browser
import os
import pytest

@pytest.fixture(scope="session")
def port():
    return 8080

@pytest.fixture(scope="session")
def base_url(port):
    return 'http://localhost:' + str(port)

@pytest.fixture(scope="session")
def server(port):
    server = ServerDriver(name='MyServer', port=port)
    server.start(cmd=['gunicorn', 'app:app', '-w', '1', '-b', '0.0.0.0:{0}'.format(port)])
    return server

@pytest.fixture(scope="session")
def browser(server, base_url):
    browser = Browser('firefox', headless=True)
    yield browser
    browser.quit()
    server.shutdown()

