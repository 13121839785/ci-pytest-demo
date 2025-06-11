
from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_by_name(self, product_name):
        # 通过商品名定位对应的“Add to cart”按钮并点击
        xpath = f'//div[text()="{product_name}"]/ancestor::div[@class="inventory_item"]//button'
        self.driver.find_element(By.XPATH, xpath).click()

    def go_to_cart(self):
        # 点击右上角购物车图标
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
