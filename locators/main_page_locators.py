from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_TO_ACC_BTN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    CONSTRUCTOR_TAB = (By.XPATH, ".//p[text()='Конструктор']")
    FEED_TAB = (By.XPATH, ".//p[text()='Лента Заказов']")
    INGREDIENT = (By.XPATH, "//ul[contains(@class, 'burger-ingredients') or contains(@class, 'BurgerIngredients_ingredients__')]/a[1]")  # первый ингредиент
    INGREDIENT_MODAL = (By.XPATH, ".//section[contains(@class, 'Modal_modal__')]")
    MODAL_CLOSE_BTN = (By.XPATH, ".//section[contains(@class, 'Modal_modal__')]//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_COUNTER = (By.XPATH, "((//a[starts-with(@href, '/ingredient/')])[1]//p[contains(@class, 'counter')])[1]")
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    BURGER_CONSTRUCTOR_DROP_AREA = (By.XPATH, "//span[contains(text(), 'Перетяните булочку сюда (верх)')]/ancestor::div[contains(@class, 'constructor') or contains(@class, 'BurgerConstructor_basket__')]") 