from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url


def test_login_fail_wrong_password(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "wrong_password")

    wait = WebDriverWait(driver, 5)
    error = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@data-test="error"]'))
    )
    assert "Username and password do not match" in error.text
