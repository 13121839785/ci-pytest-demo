import time
from pages.baidu_page import BaiduPage

class TestBaiduSearch:
    def test_baidu_search(self, driver):
        page = BaiduPage(driver)
        page.open()
        page.search("自动化测试")
        time.sleep(2)
        assert "这是一条不存在的内容" in driver.page_source
