from tests.external.support.driver.server_driver import ServerDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from splinter import Browser
import os
import pytest

@pytest.fixture(scope="session")
def base_url():
    return 'http://host.docker.internal:8080'

@pytest.fixture(scope="session")
def server():
    server = ServerDriver(name='MyServer', port=5000)
    server.start(cmd=['gunicorn', 'backend:app', '-w', '1', '-b', '0.0.0.0:{0}'.format(5000)])
    return server

@pytest.fixture(scope="session")
def browser(server, base_url):
    browser = Browser('firefox', headless=True)
    yield browser
    browser.quit()
    server.shutdown()

