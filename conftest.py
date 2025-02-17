import pytest

from selene import browser


@pytest.fixture(scope="function")
def browser_1920_1080():
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    browser.open('https://duckduckgo.com/')
    yield
    browser.quit()