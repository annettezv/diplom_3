import allure

from pages.account_page import AccountPage
from pages.login_page import LoginPage
from conftest import driver, user

class TestAccount:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_redirect_to_account_page(self, driver, user):
        account_page = AccountPage(driver)
        account_page.open_account_profile()
        assert '/account/profile' in account_page.get_current_url()

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
