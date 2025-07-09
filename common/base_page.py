from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.logger import logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        logger.info(f"🔗 打开页面：{url}")
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        logger.info(f"🔍 查找元素：{locator}")
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def send_keys(self, locator, text):
        logger.info(f"⌨️ 输入文本：{text}")
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        logger.info(f"🖱️ 点击元素：{locator}")
        self.find_element(locator).click()

    def get_text(self, locator):
        text = self.find_element(locator).text
        logger.info(f"📄 获取文本：{text}")
        return text
