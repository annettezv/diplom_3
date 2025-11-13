from locators.recovery_page_locators import RecoveryPageLocators
from pages.base_page import BasePage
import allure

class RecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RecoveryPageLocators()

    @allure.step('Ввести email для восстановления пароля')
    def enter_email(self, email):
        self.fill_input(self.locators.EMAIL_INPUT, email)

    @allure.step("Кликнуть по кнопке 'Восстановить'")
    def click_recovery_btn(self):
        self.wait_visibility_of_element(self.locators.RECOVERY_BTN)
        self.click_on_element(self.locators.RECOVERY_BTN)

    @allure.step("Кликнуть по иконке показать/скрыть пароль")
    def click_show_password_icon(self):
        self.click_on_element(self.locators.SHOW_PASSWORD_ICON)

    @allure.step("Проверить, что поле пароля активно (в фокусе)")
    def is_password_input_active(self):
        element = self.find_element(self.locators.PASSWORD_INPUT)
        return element == self.get_active_element()

    @allure.step("Дождаться появления кнопки сохранения нового пароля")
    def wait_for_save_new_password_button(self):
        self.wait_visibility_of_element(self.locators.SAVE_NEW_PSW_BTN)
