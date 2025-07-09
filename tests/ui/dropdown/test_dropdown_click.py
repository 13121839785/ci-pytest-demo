# test_dropdown_click.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestDropdownClick:
    def test_click_dropdown(self, driver):
        driver.get("https://www.baidu.com")

        # 1. 点击“设置”按钮，触发下拉
        driver.find_element(By.ID, "s-usersetting-top").click()

        # 2. 等待“搜索设置”选项出现（显示在下拉菜单中）
        el = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='搜索设置']"))
        )

        # 3. 点击“搜索设置”
        el.click()
        time.sleep(2)
