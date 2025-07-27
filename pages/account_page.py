import allure

from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators

class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AccountPageLocators()

    @allure.step("Перейти в раздел 'История заказов'")
    def go_to_order_history(self):
        self.wait_visibility_of_element(self.locators.ORDER_HISTORY_BTN)
        self.click_on_element(self.locators.ORDER_HISTORY_BTN)

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.wait_visibility_of_element(self.locators.LOGOUT_BTN)
        self.click_on_element(self.locators.LOGOUT_BTN)
