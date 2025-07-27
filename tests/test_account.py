import allure

from pages.account_page import AccountPage
from pages.registration_page import RegistrationPage
from configs.urls import Urls
from locators.login_page_locators import LoginPageLocators
from conftest import driver, user
from pages.base_page import BasePage
from pages.login_page import LoginPage

class TestAccount:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_redirect_to_account_page(self, driver, user):
        base_page = BasePage(driver)
        base_page.open_url(Urls.ACCOUNT_PROFILE_URL)
        assert '/account/profile' in base_page.get_current_url()

    @allure.title("Переход в раздел «История заказов»")
    def test_redirect_to_order_history(self, driver, user):
        login_page = LoginPage(driver)
        login_page.click_login_success_button()
        account_page = AccountPage(driver)
        account_page.go_to_order_history()
        assert '/account/order-history' in account_page.get_current_url()

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, user):
        login_page = LoginPage(driver)
        login_page.click_login_success_button()
        account_page = AccountPage(driver)
        account_page.logout()

        login_page.wait_for_login_button()
        assert '/login' in account_page.get_current_url()
