from selenium.webdriver.common.by import By

class RecoveryPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//label[contains(text(), 'Email')]/following-sibling::input")
    RECOVERY_BTN = (By.XPATH, ".//button[text()='Восстановить']")
    PASSWORD_INPUT = (By.XPATH, ".//label[contains(text(), 'Пароль')]/following-sibling::input")
    SHOW_PASSWORD_ICON = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::div[contains(@class,'input__icon')]")
