import allure

from configs.urls import Urls
from pages.recovery_page import RecoveryPage
from locators.login_page_locators import LoginPageLocators
from conftest import driver

class TestRecoveryPassword:

    @allure.step("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_redirect_to_recovery_page_by_recovery_btn(self, driver):
        driver.get(Urls.LOGIN_PAGE_URL)
        recovery_link = driver.find_element(*LoginPageLocators.RECOVERY_PSW_LINK)
        recovery_link.click()
        assert 'forgot-password' in driver.current_url

    @allure.step("Ввод почты и клик по кнопке «Восстановить»")
    def test_recovery_password_email_submit(self, driver):
        driver.get(Urls.RECOVERY_PSW_PAGE_URL)
        recovery_page = RecoveryPage(driver)
        test_email = 'test@example.com'
        recovery_page.enter_email(test_email)
        recovery_page.click_recovery_btn()

        recovery_page.wait_visibility_of_element(LoginPageLocators.SAVE_NEW_PSW_BTN)

        assert 'reset-password' in driver.current_url

    @allure.step("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_show_password_icon_activates_password_input(self, driver):
        driver.get(Urls.RECOVERY_PSW_PAGE_URL)
        recovery_page = RecoveryPage(driver)
        test_email = 'test@example.com'
        recovery_page.enter_email(test_email)
        recovery_page.click_recovery_btn()

        recovery_page.wait_visibility_of_element(LoginPageLocators.SAVE_NEW_PSW_BTN)

        recovery_page.click_show_password_icon()
        assert recovery_page.is_password_input_active(), 'Поле пароля не стало активным после клика по иконке'
