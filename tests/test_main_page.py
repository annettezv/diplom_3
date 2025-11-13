import allure

from pages.home_page import HomePage
from configs.urls import Urls
from conftest import driver, user

class TestMainPage:

    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor_tab(self, driver):
        home_page = HomePage(driver)
        home_page.open_url(Urls.HOME_PAGE_URL)
        home_page.click_feed_tab()
        home_page.click_constructor_tab()
        assert 'constructor' in home_page.get_current_url() or 'stellarburgers' in home_page.get_current_url()

    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_feed_tab(self, driver):
        home_page = HomePage(driver)
        home_page.open_url(Urls.HOME_PAGE_URL)
        home_page.click_feed_tab()
        assert '/feed' in home_page.get_current_url()

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_ingredient_modal_open_and_close(self, driver):
        home_page = HomePage(driver)
        home_page.open_url(Urls.HOME_PAGE_URL)
        home_page.click_first_ingredient()
        assert home_page.is_ingredient_modal_open()
        home_page.close_ingredient_modal()
        assert not home_page.is_ingredient_modal_open()

    @allure.title("при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_ingredient_counter_increases(self, driver):
        home_page = HomePage(driver)
        home_page.open_url(Urls.HOME_PAGE_URL)
        before = home_page.get_first_ingredient_counter()
        home_page.add_first_ingredient_to_order()
        after = home_page.get_first_ingredient_counter()
        assert after == before + 2

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_order_button_for_logged_in_user(self, driver, user):
        home_page = HomePage(driver)
        home_page.open_url(Urls.HOME_PAGE_URL)
        assert home_page.is_order_button_displayed()
