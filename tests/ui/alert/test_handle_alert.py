import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


# @pytest.mark.usefixtures("driver")  # 自动应用 driver 夹具,在执行这个类里的每一个方法前，先执行名为 driver 的 fixture
class TestHandleAlert:

    def test_alert_accept(self,driver):
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

        alert = Alert(driver)
        print("弹窗内容：", alert.text)
        alert.accept()

        time.sleep(1)

    def test_alert_dismiss(self,driver):
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

        alert = Alert(driver)
        print("弹窗内容：", alert.text)
        time.sleep(2)
        alert.dismiss()

        time.sleep(1)

    def test_prompt_input(self,driver):
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

        alert = Alert(driver)
        print("弹窗内容：", alert.text)
        alert.send_keys("你好，Selenium！")
        alert.accept()

        # 检查页面上是否显示输入内容
        result_text = driver.find_element(By.ID, "result").text
        print("页面结果：", result_text)

        assert "你好，Selenium！" in result_text
        time.sleep(1)

    def test_prompt_dismiss(self,driver):#为了让方法符合类的结构（所有类的方法都需要 self）
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        # 点击“Click for JS Prompt”
        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

        # 弹出 prompt，什么都不输入，点击取消
        alert = Alert(driver)
        print("弹窗内容：", alert.text)
        alert.dismiss()  # 点击“取消”

        # 检查页面上的返回值
        result_text = self.driver.find_element(By.ID, "result").text
        print("页面结果：", result_text)

        # 页面应该显示默认提示，而不是输入的内容
        assert result_text == "You entered: null"
        time.sleep(1)