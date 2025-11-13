from selenium.webdriver.common.by import By

class LoginPageLocators:

    LOGIN_HEADER = (By.XPATH, ".//h2[text()='Вход']")
    LOGIN_BTN = (By.XPATH, ".//button[text()='Войти']")
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")
    INVALID_PSW_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")
    RECOVERY_PSW_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")
    SAVE_NEW_PSW_BTN = (By.XPATH, "//button[contains(@class, 'button_button_type_primary') and text()='Сохранить']")
    RECOVERY_PSW_HEADER = (By.XPATH, ".//h2[contains(text(),'Восстановление пароля')]")
    RECOVERY_PSW_BTN = (By.XPATH, ".//button[text()='Восстановить']")
    ACCOUNT_BTN = (By.XPATH, ".//a[@href='/account']")
    PSW_FROM_MAIL = (By.XPATH, ".//label[contains(text(), 'Введите код из письма')]/following-sibling::input")
    SAVE_BTN = (By.XPATH, ".//button[text()='Сохранить']")
    LOGOUT_BTN = (By.XPATH, ".//button[text()='Выход']")
    EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")
    LOGIN_SUBMIT_BTN = (By.XPATH, ".//button[text()='Войти']")
    LOGIN_SUCCESS_BUTTON = (By.XPATH, "//button[text()='Личный Кабинет'] | //p[text()='Личный Кабинет']")
