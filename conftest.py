
import pytest
from selenium import webdriver

from configs.urls import Urls
from locators.account_page_locators import AccountPageLocators
from pages.account_page import AccountPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from locators.login_page_locators import LoginPageLocators


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture()
def user():
    return {'name': 'test',
            'email': 'test@test.ru',
            'password': '123456'}


@pytest.fixture()
def setup(driver, user):
    account_page = AccountPage(driver)
    account_page.open_url(Urls.REGISTER_PAGE_URL)
    account_page.register_user(user)
    account_page.confirm_registration()
    login_page = LoginPage(driver)
    login_page.wait_for_login_header()

