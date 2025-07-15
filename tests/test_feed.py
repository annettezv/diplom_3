import allure
import pytest
from pages.home_page import HomePage
from helpers import registration
from configs.urls import Urls
from conftest import driver, user
from selenium.webdriver.support.ui import WebDriverWait
from locators.feed_page_locators import FeedPageLocators
from locators.login_page_locators import LoginPageLocators

class TestFeed:
    @pytest.fixture(autouse=True)
    def setup(self, driver, user):
        registration(driver, user)
        driver.get(Urls.LOGIN_PAGE_URL)
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BTN).click()

    @allure.step("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_order_modal_opens_on_click(self, driver):
        driver.get(Urls.HOME_PAGE_URL)
        home_page = HomePage(driver)
        home_page.click_feed_tab()
        home_page.wait_visibility_of_element(FeedPageLocators.FIRST_ORDER)
        first_order = driver.find_element(*FeedPageLocators.FIRST_ORDER)
        first_order.click()
        home_page.wait_visibility_of_element(FeedPageLocators.ORDER_MODAL)
        assert driver.find_element(*FeedPageLocators.ORDER_MODAL).is_displayed()

    @allure.step("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_orders_appear_in_feed(self, driver):
        driver.get(Urls.HOME_PAGE_URL)
        home_page = HomePage(driver)
        # Оформляем заказ
        home_page.add_first_ingredient_to_order()
        home_page.wait_visibility_of_element(home_page.locators.ORDER_BUTTON)
        home_page.find_element(home_page.locators.ORDER_BUTTON).click()

        home_page.wait_invisibility_of_element(FeedPageLocators.ORDER_MODAL_LOADING)

        order_number = home_page.find_element(FeedPageLocators.ORDER_MODAL_NUMBER).text

        home_page.find_element(FeedPageLocators.ORDER_MODAL_CLOSE_BTN).click()

        home_page.click_feed_tab()

        home_page.wait_visibility_of_element(FeedPageLocators.ORDER_FEED_NUMBER)
        last_order = home_page.find_element(FeedPageLocators.ORDER_FEED_NUMBER).text
        assert order_number in str(last_order)


    @pytest.mark.parametrize(
        "counter_locator, description",
        [
            (FeedPageLocators.ORDER_FEED_NUMBER, "total orders"),
            (FeedPageLocators.ORDER_FEED_TODAY_NUMBER, "today's orders"),
        ]
    )
    @allure.step("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    @allure.step("при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_counter_increases(self, driver, counter_locator, description):
        driver.get(Urls.HOME_PAGE_URL)
        home_page = HomePage(driver)
        home_page.click_feed_tab()
        home_page.wait_visibility_of_element(counter_locator)
        before = int(home_page.find_element(counter_locator).text)

        driver.get(Urls.HOME_PAGE_URL)
        # Оформляем заказ
        home_page.add_first_ingredient_to_order()
        home_page.wait_visibility_of_element(home_page.locators.ORDER_BUTTON)
        home_page.find_element(home_page.locators.ORDER_BUTTON).click()

        home_page.wait_invisibility_of_element(FeedPageLocators.ORDER_MODAL_LOADING)

        home_page.find_element(FeedPageLocators.ORDER_MODAL_CLOSE_BTN).click()

        home_page.click_feed_tab()
        home_page.wait_visibility_of_element(counter_locator)
        after = int(home_page.find_element(counter_locator).text)
        assert after > before, f"{description} counter did not increase: before={before}, after={after}"

    @allure.step("Gосле оформления заказа его номер появляется в разделе В работе")
    def test_order_number_in_work(self, driver):
        home_page = HomePage(driver)
        # Оформляем заказ
        home_page.add_first_ingredient_to_order()
        home_page.wait_visibility_of_element(home_page.locators.ORDER_BUTTON)
        home_page.find_element(home_page.locators.ORDER_BUTTON).click()

        home_page.wait_invisibility_of_element(FeedPageLocators.ORDER_MODAL_LOADING)

        order_number = home_page.find_element(FeedPageLocators.ORDER_MODAL_NUMBER).text

        home_page.find_element(FeedPageLocators.ORDER_MODAL_CLOSE_BTN).click()

        home_page.click_feed_tab()

        WebDriverWait(driver, 50).until(
            lambda _: home_page.find_element(FeedPageLocators.IN_WORK_FIRST).text.strip().isdigit()
        )

        in_work_first = str(home_page.find_element(FeedPageLocators.IN_WORK_FIRST).text)
        assert order_number in in_work_first
