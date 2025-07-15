import allure

from pages.account_page import AccountPage
from configs.urls import Urls
from helpers import registration
from locators.login_page_locators import LoginPageLocators
from conftest import driver, user

class TestAccount:

    @allure.step("Переход по клику на «Личный кабинет»")
    def test_redirect_to_account_page(self, driver, user):
        registration(driver, user)
        driver.get(Urls.LOGIN_PAGE_URL)
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BTN).click()
        driver.get(Urls.ACCOUNT_PROFILE_URL)
        assert '/account/profile' in driver.current_url

    @allure.step("Переход в раздел «История заказов»")
    def test_redirect_to_order_history(self, driver, user):
        registration(driver, user)
        driver.get(Urls.LOGIN_PAGE_URL)
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BTN).click()

        account_page = AccountPage(driver)
        account_page.wait_visibility_of_element(LoginPageLocators.LOGIN_SUCCESS_BUTTON)
        driver.find_element(*LoginPageLocators.LOGIN_SUCCESS_BUTTON).click()
        account_page.go_to_order_history()
        assert '/account/order-history' in driver.current_url

    @allure.step("Выход из аккаунта")
    def test_logout(self, driver, user):
        registration(driver, user)
        driver.get(Urls.LOGIN_PAGE_URL)
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BTN).click()

        account_page = AccountPage(driver)
        account_page.wait_visibility_of_element(LoginPageLocators.LOGIN_SUCCESS_BUTTON)
        driver.find_element(*LoginPageLocators.LOGIN_SUCCESS_BUTTON).click()
        account_page.logout()

        account_page.wait_visibility_of_element(LoginPageLocators.LOGIN_SUBMIT_BTN)
        assert '/login' in driver.current_url
