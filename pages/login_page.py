import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    @allure.step("Кликнуть на кнопку успешного входа")
    def click_login_success_button(self):
        self.wait_visibility_of_element(self.locators.LOGIN_SUCCESS_BUTTON)
        self.click_on_element(self.locators.LOGIN_SUCCESS_BUTTON)

    @allure.step("Кликнуть на ссылку восстановления пароля")
    def click_recovery_password_link(self):
        self.wait_visibility_of_element(self.locators.RECOVERY_PSW_LINK)
        self.click_on_element(self.locators.RECOVERY_PSW_LINK)

    @allure.step("Подождать появления кнопки входа")
    def wait_for_login_button(self):
        self.wait_visibility_of_element(self.locators.LOGIN_BTN)
