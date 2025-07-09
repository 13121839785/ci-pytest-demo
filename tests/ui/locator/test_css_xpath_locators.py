# test_css_xpath_locators.py
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCssXpathLocators:#TestCssXpathLocators

    def test_css_by_id(self, driver):
        driver.get("https://www.baidu.com")
        # CSS Selector: #kw → id="kw"
        # "#" 代表 id，"kw" 是 id 的值
        el = driver.find_element(By.CSS_SELECTOR, "#kw")
        el.send_keys("CSS - id 定位")

    def test_xpath_by_id(self, driver):
        driver.get("https://www.baidu.com")
        # XPath: //input[@id='kw']
        # "//"：任意位置查找
        # "input"：标签名
        # "[@id='kw']"：属性为 id 且值为 kw
        el = driver.find_element(By.XPATH, "//input[@id='kw']")
        el.send_keys("XPath - id 定位")

    def test_css_by_class(self, driver):
        driver.get("https://www.baidu.com")
        # CSS Selector: .s_ipt → class="s_ipt"
        # "." 代表 class，"s_ipt" 是 class 名
        el = driver.find_element(By.CSS_SELECTOR, ".s_ipt")
        el.send_keys("CSS - class 定位")

    def test_xpath_by_class(self, driver):
        driver.get("https://www.baidu.com")
        # XPath: //input[contains(@class, 's_ipt')]
        # "contains()"：包含某值
        # "@class"：class 属性
        el = driver.find_element(By.XPATH, "//input[contains(@class,'s_ipt')]")
        el.send_keys("XPath - class 部分匹配")

    def test_css_by_attr(self, driver):
        driver.get("https://www.baidu.com")
        # CSS Selector: input[name='wd']
        # "[name='wd']" 表示属性 name="wd"
        el = driver.find_element(By.CSS_SELECTOR, "input[name='wd']")
        el.send_keys("CSS - name 属性定位")

    def test_xpath_by_attr(self, driver):
        driver.get("https://www.baidu.com")
        # XPath: //input[@name='wd']
        # "[@name='wd']" 表示属性 name="wd"
        el = driver.find_element(By.XPATH, "//input[@name='wd']")
        el.send_keys("XPath - name 属性定位")

    def test_xpath_text_match(self, driver):
        driver.get("https://www.baidu.com")
        # XPath: //a[text()='新闻']
        # "//a"：任意位置的 <a> 标签
        # "[text()='新闻']"：内容完全等于"新闻"
        el = driver.find_element(By.XPATH, "//a[contains(text(),'新闻')]")
        el.click()
        time.sleep(2)

    def test_xpath_space_text_match(self, driver):
        driver.get("https://www.baidu.com")
        # XPath: //a[text()='新闻']
        # "//a"：任意位置的 <a> 标签
        # "[text()='新闻']"：内容完全等于"新闻"
        el = driver.find_element(By.XPATH, "//a[normalize-space(text())='新闻']")
        el.click()
        time.sleep(2)

    def test_xpath_following_sibling(self, driver):
        driver.get("https://www.baidu.com")
        # 1. 点击“设置”按钮
        driver.find_element(By.XPATH, "//span[@id='s-usersetting-top']").click()

        # 2. 等待“搜索设置”可点击后再点击
        el = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='搜索设置']"))
        )
        el.click()

    def test_xpath_presence(self, driver):
        driver.get("https://www.baidu.com")
        # 1. 点击“设置”按钮
        driver.find_element(By.XPATH, "//span[@id='s-usersetting-top']").click()

        # 2. 等待“搜索设置”可点击后再点击
        el = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='搜索设置']"))
        )
        el.click()

    def test_xpath_in_element(self, driver):
        driver.get("https://www.baidu.com")
        # 1. 点击“设置”按钮
        driver.find_element(By.XPATH, "//span[@id='s-usersetting-top']").click()

        # 2. 等待“搜索设置”可点击后再点击
        el = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "s-usersetting-top"), "设置")
        ) #返回的是：True 或 False
        # 3. 再次查找这个元素并点击
        el = driver.find_element(By.ID, "s-usersetting-top")
        el.click()
