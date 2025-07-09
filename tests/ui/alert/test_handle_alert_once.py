#test_handle_alert_once.py
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

@pytest.mark.usefixtures("driver")
class TestHandleAlert:

    @pytest.fixture(autouse=True) #自动生效的 fixture。用途：autouse=True 表示只要运行类中的测试方法，这个 fixture 就会自动执行
    def init_driver(self, driver): #类中定义的一个方法，接收从外部传入的 driver
        self.driver = driver #Selenium WebDriver 实例保存在类的实例中

    def setup_method(self): #Pytest 支持的钩子函数之一，表示每个测试方法执行前都会调用这个函数;setup_method(self) 是 pytest 的钩子方法，不支持像 def test_xxx(self, driver) 那样自动接收 fixture，所以需要你提前手动绑定 driver 到 self 上
        print("🔧 每次打开网站")
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
