import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
import random as r

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть URL")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Кликнуть на эелемент")
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Заполнить поле")
    def fill_input(self, locator, text):
        self.wait_visibility_of_element(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step("Выбрать любой элемент из списка")
    def select_random_element_from_list(self, locator):
        elements = self.driver.find_elements(*locator)
        random_element = r.choice(elements)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", random_element)
        random_element.click()

    @allure.step("Подождать видимости элемента")
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Прокрутить страницу до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Сравнить текущий URL страницы с ожидаемым")
    def check_current_page_url(self, expected_url):
        assert self.driver.current_url == expected_url

    @allure.step("Перейти на новую вкладку")
    def switch_to_tab(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    @allure.step("Подождать видимости элемента")
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Подождать пока элемент видим")
    def wait_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver, 50).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Перетащить элемент")
    def drag_and_drop(self, element, target):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(element, target).perform()

    @allure.step("Получить активный элемент")
    def get_active_element(self):
        return self.driver.switch_to.active_element

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверить видимость элемента")
    def is_element_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    @allure.step("Получить текст элемента")
    def get_element_text(self, locator):
        return self.find_element(locator).text
