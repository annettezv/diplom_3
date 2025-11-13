import allure

from configs.urls import Urls
from pages.recovery_page import RecoveryPage
from locators.login_page_locators import LoginPageLocators
from conftest import driver
from pages.base_page import BasePage
from pages.login_page import LoginPage

class TestRecoveryPassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_redirect_to_recovery_page_by_recovery_btn(self, driver):
        login_page = LoginPage(driver)
        login_page.open_url(Urls.LOGIN_PAGE_URL)
        login_page.click_recovery_password_link()
        assert 'forgot-password' in login_page.get_current_url()

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_recovery_password_email_submit(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.open_url(Urls.RECOVERY_PSW_PAGE_URL)
        test_email = 'test@example.com'
        recovery_page.enter_email(test_email)
        recovery_page.click_recovery_btn()
        recovery_page.wait_for_save_new_password_button()
        assert 'reset-password' in recovery_page.get_current_url()

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_show_password_icon_activates_password_input(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.open_url(Urls.RECOVERY_PSW_PAGE_URL)
        test_email = 'test@example.com'
        recovery_page.enter_email(test_email)
        recovery_page.click_recovery_btn()
        recovery_page.wait_for_save_new_password_button()
        recovery_page.click_show_password_icon()
        assert recovery_page.is_password_input_active(), 'Поле пароля не стало активным после клика по иконке'
