from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from splinter import Browser
import os
import pytest

@pytest.fixture(scope="session")
def base_url():
    return 'http://nginx'

@pytest.fixture(scope="session")
def browser(base_url):
    browser = Browser('firefox', headless=True)
    yield browser
    browser.quit()

