from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    
    LOGIN_TO_ACC_BTN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    LOGIN_HEADER = (By.XPATH, ".//h2[text()='Вход']")
    REGISTER_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")
    REGISTER_HEADER = (By.XPATH, "//h2[contains(text(),'Регистрация')]")
    REGISTER_BTN = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    USER_NAME = (By.XPATH, ".//label[contains(text(), 'Имя')]/following-sibling::input")
    EMAIL = (By.XPATH, ".//label[contains(text(), 'Email')]/following-sibling::input")
    PASSWORD = (By.XPATH, ".//label[contains(text(), 'Пароль')]/following-sibling::input")
