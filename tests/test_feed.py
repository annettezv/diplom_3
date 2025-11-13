import allure
import pytest
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from configs.urls import Urls
from conftest import driver, user
from selenium.webdriver.support.ui import WebDriverWait
from locators.feed_page_locators import FeedPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

class TestFeed:

    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_order_modal_opens_on_click(self, driver):
        home_page = HomePage(driver)
        home_page.open_url(Urls.HOME_PAGE_URL)
        home_page.click_feed_tab()
        home_page.click_first_order_in_feed()
        assert home_page.is_order_modal_displayed()

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_orders_appear_in_feed(self, driver):
        home_page = HomePage(driver)
        home_page.open_url(Urls.HOME_PAGE_URL)
        # Оформляем заказ
        home_page.add_first_ingredient_to_order()
        home_page.click_order_button()
        order_number = home_page.get_order_number_from_modal()
        home_page.close_order_modal()
        home_page.click_feed_tab()
        assert order_number in home_page.get_latest_order_number_in_feed()


    @pytest.mark.parametrize(
        "counter_locator, description",
        [
            (FeedPageLocators.ORDER_FEED_NUMBER, "total orders"),
            (FeedPageLocators.ORDER_FEED_TODAY_NUMBER, "today's orders"),
        ]
    )
    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_counter_increases(self, driver, counter_locator, description):
        home_page = HomePage(driver)
        home_page.open_url(Urls.HOME_PAGE_URL)
        home_page.click_feed_tab()
        before = home_page.get_order_feed_counter_value(counter_locator)

        home_page.open_url(Urls.HOME_PAGE_URL)
        # Оформляем заказ
        home_page.add_first_ingredient_to_order()
        home_page.click_order_button()
        home_page.wait_for_order_modal_to_load()
        home_page.close_order_modal()

        home_page.click_feed_tab()
        after = home_page.get_order_feed_counter_value(counter_locator)
        assert after > before, f"{description} counter did not increase: before={before}, after={after}"

    @allure.title("Gосле оформления заказа его номер появляется в разделе В работе")
    def test_order_number_in_work(self, driver):
        home_page = HomePage(driver)
        # Оформляем заказ
        home_page.add_first_ingredient_to_order()
        home_page.click_order_button()
        order_number = home_page.get_order_number_from_modal()
        home_page.close_order_modal()
        home_page.click_feed_tab()
        assert order_number in home_page.get_order_number_in_work_section()
