
import time
from time import sleep

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

def test_add_items_to_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    # 登录
    login.open()
    login.login("standard_user", "secret_sauce")

    # 添加两个商品
    inventory.add_product_by_name("Sauce Labs Backpack")
    driver.save_screenshot("after_add_to_cart_1.png")
    time.sleep(2)
    inventory.add_product_by_name("Sauce Labs Bike Light")
    driver.save_screenshot("after_add_to_cart_2.png")
    time.sleep(2)

    # 进入购物车
    inventory.go_to_cart()
    sleep(2)

    # 获取购物车中的商品名称
    cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    cart_names = [item.text for item in cart_items]

    # 断言商品存在
    assert "Sauce Labs Backpack" in cart_names
    assert "Sauce Labs Bike Light" in cart_names
