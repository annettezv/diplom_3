from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators

class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Зарегистрировать пользователя")
    def register_user(self, user):
        self.click_on_element(MainPageLocators.LOGIN_TO_ACC_BTN)
        self.wait_visibility_of_element(LoginPageLocators.LOGIN_HEADER)
        self.click_on_element(LoginPageLocators.REGISTER_LINK)
        self.wait_visibility_of_element(LoginPageLocators.REGISTER_HEADER)
        self.fill_input(LoginPageLocators.USER_NAME, user['name'])
        self.fill_input(LoginPageLocators.EMAIL, user['email'])
        self.fill_input(LoginPageLocators.PASSWORD, user['password'])
        self.click_on_element(LoginPageLocators.REGISTER_BTN)
