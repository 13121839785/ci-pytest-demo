# conftest.py
import pytest
from api.common.auth_util import AuthUtil

@pytest.fixture(scope="session") #把一个函数标记为夹具
def token_fixture():
    print("🌐 获取测试用 token（来自 fixture）")
    return AuthUtil.get_token()

# conftest.py 中追加（放在 token_fixture 下方）

import pytest
from api.common.request_util import RequestUtil

@pytest.fixture
def add_user_fixture(token_fixture):
    print("🚀 准备创建用户（自动带清理）")
    url = "http://127.0.0.1:5000/user/add"
    user_data = {
        "name": "test_user_fixture",
        "email": "fixture@example.com"
    }

    # 创建用户
    req = RequestUtil(use_token=False)
    req.headers["Authorization"] = f"Bearer {token_fixture}"
    resp = req.post(url, json=user_data)
    assert resp.status_code == 201
    user_id = resp.json().get("id")
    print("✅ 创建响应：", resp.status_code, resp.text)
    print(f"✅ 用户创建成功，ID：{user_id}")

    yield user_id  # 返回给测试用例使用

    # 清理：删除用户
    print(f"🧹 测试结束，开始删除用户 ID：{user_id}")
    del_url = f"http://127.0.0.1:5000/user/delete/{user_id}"
    del_resp = req.delete(del_url)
    print(f"🗑️ 删除响应：{del_resp.status_code} - {del_resp.text}")


# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # 初始化 Chrome 浏览器
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')  # 启动最大化
    options.add_argument('--headless')       # 如需无界面执行，可启用此行
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver  # 返回 driver 实例给测试用例

    # 测试结束后关闭浏览器
    driver.quit()

