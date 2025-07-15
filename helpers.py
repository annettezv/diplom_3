from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from conftest import driver, user

def registration(driver, user):
    driver.find_element(*MainPageLocators.LOGIN_TO_ACC_BTN).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_HEADER))
    driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.REGISTER_HEADER))
    user_name = driver.find_element(*LoginPageLocators.USER_NAME)
    user_name.clear()
    user_name.send_keys(user['name'])
    email = driver.find_element(*LoginPageLocators.EMAIL)
    email.clear()
    email.send_keys(user['email'])
    psw = driver.find_element(*LoginPageLocators.PASSWORD)
    psw.clear()
    psw.send_keys(user['password'])
    driver.find_element(*LoginPageLocators.REGISTER_BTN).click()
