# test_hover_dropdown.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestHoverDropdown:
    def test_hover_and_click(self, driver):
        driver.get("https://www.taobao.com/")

        # 1. 悬停“我的淘宝”按钮（顶部菜单）
        my_taobao = driver.find_element(By.CSS_SELECTOR, "#J_SiteNavMytaobao .site-nav-menu-hd")
        ActionChains(driver).move_to_element(my_taobao).perform()

        # 2. 等待下拉菜单中“已买到的宝贝”出现
        el = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "我的足迹"))
        )

        # 3. 点击该菜单项
        el.click()
        time.sleep(2)
