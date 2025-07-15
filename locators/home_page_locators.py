import By


class HomePageLocators:
    LOGIN_TO_ACC_BTN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    BURGER_CONSTRUCTOR_HEADER = (By.XPATH, ".//h1[text()='Соберите бургер']")
    LOGO_BUTTON = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")