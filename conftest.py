import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")  # ✅ 使用新版无头模式
    options.add_argument("--no-sandbox")  # ✅ 禁用沙箱，适配 CI
    options.add_argument("--disable-dev-shm-usage")  # ✅ 避免内存共享问题

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
