from selenium.webdriver.common.by import By

class FeedPageLocators:
    FIRST_ORDER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orders__') or contains(@class, 'OrderFeed_list__')]/li[1]")
    ORDER_MODAL = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")
    ORDER_MODAL_LOADING = (By.XPATH, ".//div[contains(@class, 'Modal_modal_opened')]")
    ORDER_MODAL_CLOSE_BTN = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//button")
    ORDER_MODAL_NUMBER = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//h2")
    ORDER_FEED_NUMBER = (By.XPATH, ".//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p[1]")
    ORDER_FEED_TODAY_NUMBER = (By.XPATH, ".//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[1]")
    IN_WORK_FIRST = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__')]/li[1]")