import time

import pytest
from pages.home_page import HomePage

@pytest.fixture()
def before_after():
    print("before test")
    yield None
    print("\nafter test")


def test_login(browser):
    simple_page = HomePage(browser)
    simple_page.open()
    simple_page.type_username('<PASSWORD>')
    simple_page.type_password('<PASSWORD>')
    time.sleep(4)

def test_login1(browser):
    simple_page = HomePage(browser)
    simple_page.open()
    simple_page.type_username('<PASSWORD>')
    simple_page.type_password('<PASSWORD>')
    time.sleep(4)