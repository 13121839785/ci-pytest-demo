import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

@pytest.mark.usefixtures("driver")
class TestHandleAlert:

    def setup_class(self):
        from conftest import driver as driver_fixture  # 临时引用
        self.driver = driver_fixture  # 显式绑定 driver
        print("🔧 打开一次网站")
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(1)

    def test_alert_accept(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
        alert = Alert(self.driver)
        print("弹窗内容：", alert.text)
        alert.accept()
        time.sleep(1)

    def test_alert_dismiss(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
        alert = Alert(self.driver)
        print("弹窗内容：", alert.text)
        alert.dismiss()
        time.sleep(1)

    def test_prompt_input(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        alert = Alert(self.driver)
        alert.send_keys("测试一下")
        alert.accept()
        time.sleep(1)

    def test_prompt_dismiss(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        alert = Alert(self.driver)
        alert.dismiss()
        time.sleep(1)
