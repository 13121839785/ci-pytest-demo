from time import sleep

from selenium.webdriver.common.by import By
import time

class TestBaiduLocators:
    def test_by_id(self, driver):
        driver.get("https://www.baidu.com")
        el = driver.find_element(By.ID, "kw")
        el.send_keys("自动化测试")

    def test_by_name(self, driver):
        driver.get("https://www.baidu.com")
        el = driver.find_element(By.NAME, "tn")
        print("按钮 name 属性：", el.get_attribute("value"))

    def test_by_tag_name(self, driver):
        driver.get("https://www.baidu.com")
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"页面上共有 {len(links)} 个链接标签")

    def test_by_link_text(self, driver):
        driver.get("https://www.baidu.com")
        driver.find_element(By.LINK_TEXT, "新闻").click()
        time.sleep(2)

    def test_by_partial_link_text(self, driver):
        driver.get("https://www.baidu.com")
        driver.find_element(By.PARTIAL_LINK_TEXT, "图").click()
        time.sleep(2)

    def test_by_class_name(self, driver):
        driver.get("https://www.baidu.com")
        driver.find_element(By.CLASS_NAME, "s_ipt").send_keys("By class name")
        sleep(2)

    def test_by_css_selector(self, driver):
        driver.get("https://www.baidu.com")
        driver.find_element(By.CSS_SELECTOR, "input#su").click()
        sleep(2)

    def test_by_xpath(self, driver):
        driver.get("https://www.baidu.com")
        el = driver.find_element(By.XPATH, "//input[@id='su']")
        assert el.get_attribute("value") == "百度一下"
