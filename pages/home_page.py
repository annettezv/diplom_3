from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Нажать на кнопку 'Личный кабинет'")
    def click_order_button(self):
        self.click_on_element(self.locators.LOGIN_TO_ACC_BTN)

    @allure.step("Кликнуть на вкладку 'Конструктор'")
    def click_constructor_tab(self):
        self.click_on_element(self.locators.CONSTRUCTOR_TAB)

    @allure.step("Кликнуть на вкладку 'Лента'")
    def click_feed_tab(self):
        self.wait_visibility_of_element(self.locators.FEED_TAB)
        self.click_on_element(self.locators.FEED_TAB)

    @allure.step("Кликнуть на первый ингредиент")
    def click_first_ingredient(self):
        self.click_on_element(self.locators.INGREDIENT)

    @allure.step("Модальное окно ингредиента открыто")
    def is_ingredient_modal_open(self):
        return self.find_element(self.locators.INGREDIENT_MODAL).is_displayed()

    @allure.step("Модальное окно ингредиента закрыто")
    def close_ingredient_modal(self):
        self.click_on_element(self.locators.MODAL_CLOSE_BTN)

    @allure.step("Получить значение счётчика ингредиента")
    def get_first_ingredient_counter(self):
        try:
            return int(self.find_element(self.locators.INGREDIENT_COUNTER).text)
        except Exception:
            return 0

    @allure.step("Добавить первый ингредиент в заказ")
    def add_first_ingredient_to_order(self):
        self.wait_visibility_of_element(self.locators.INGREDIENT)

        ingredient = self.find_element(self.locators.INGREDIENT)
        drop_area = self.find_element(self.locators.BURGER_CONSTRUCTOR_DROP_AREA)
        self.drag_and_drop(ingredient, drop_area)
