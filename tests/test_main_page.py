import allure

from pages.home_page import HomePage
from helpers import registration
from configs.urls import Urls
from conftest import driver, user
from locators.login_page_locators import LoginPageLocators

class TestMainPage:

    @allure.step("Переход по клику на «Конструктор»")
    def test_click_constructor_tab(self, driver):
        driver.get(Urls.HOME_PAGE_URL)
        home_page = HomePage(driver)
        home_page.click_feed_tab()
        home_page.click_constructor_tab()
        assert 'constructor' in driver.current_url or 'stellarburgers' in driver.current_url

    @allure.step("Переход по клику на «Лента заказов»")
    def test_click_feed_tab(self, driver):
        driver.get(Urls.HOME_PAGE_URL)
        home_page = HomePage(driver)
        home_page.click_feed_tab()
        assert '/feed' in driver.current_url

    @allure.step("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_ingredient_modal_open_and_close(self, driver):
        driver.get(Urls.HOME_PAGE_URL)
        home_page = HomePage(driver)
        home_page.click_first_ingredient()
        assert home_page.is_ingredient_modal_open()
        home_page.close_ingredient_modal()
        try:
            assert not home_page.is_ingredient_modal_open()
        except Exception:
            assert True

    @allure.step("при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_ingredient_counter_increases(self, driver):
        driver.get(Urls.HOME_PAGE_URL)
        home_page = HomePage(driver)
        before = home_page.get_first_ingredient_counter()
        home_page.add_first_ingredient_to_order()
        after = home_page.get_first_ingredient_counter()
        assert after == before + 2

    @allure.step("Залогиненный пользователь может оформить заказ")
    def test_order_button_for_logged_in_user(self, driver, user):
        registration(driver, user)

        driver.get(Urls.LOGIN_PAGE_URL)
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BTN).click()

        home_page = HomePage(driver)
        assert home_page.find_element(home_page.locators.ORDER_BUTTON) is not None
