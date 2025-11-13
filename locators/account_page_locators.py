from selenium.webdriver.common.by import By

class AccountPageLocators:

    ACC_LIST = (By.XPATH, ".//ul[@class='Account_list__3KQQf mb-20']")
    CONSTRUCTOR_HEADER = (By.XPATH, ".//p [text()='Конструктор']")
    RECOVERY_PSW_BTN = (By.XPATH, ".//*[@href='/forgot-password']")
    ORDER_HISTORY_BTN = (By.XPATH, ".//a[@href='/account/order-history']")
    LOGOUT_BTN = (By.XPATH, ".//button[text()='Выход']")