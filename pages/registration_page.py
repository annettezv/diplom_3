from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.registration_page_locators import RegistrationPageLocators

class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Зарегистрировать пользователя")
    def register_user(self, user):
        self.click_on_element(RegistrationPageLocators.LOGIN_TO_ACC_BTN)
        self.wait_visibility_of_element(RegistrationPageLocators.LOGIN_HEADER)
        self.click_on_element(RegistrationPageLocators.REGISTER_LINK)
        self.wait_visibility_of_element(RegistrationPageLocators.REGISTER_HEADER)
        self.fill_input(RegistrationPageLocators.USER_NAME, user['name'])
        self.fill_input(RegistrationPageLocators.EMAIL, user['email'])
        self.fill_input(RegistrationPageLocators.PASSWORD, user['password'])
        self.click_on_element(RegistrationPageLocators.REGISTER_BTN)
