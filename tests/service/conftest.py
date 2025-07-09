# conftest.py
import pytest
from api.common.auth_util import AuthUtil
from api.common.config_util import ConfigUtil


@pytest.fixture(scope="session") #把一个函数标记为夹具,夹具只负责“提供 token”，而具体怎么获取由工具类负责。
def token_fixture():
    print("🌐 获取测试用 token（来自 fixture）")
    return AuthUtil.get_token()

# conftest.py 中追加（放在 token_fixture 下方）

import pytest
from api.common.request_util import RequestUtil

from utils.db_util import DBUtil

# conftest.py 中添加（或单独放一个 fixtures/user_fixtures.py）

import pytest
from utils.db_util import DBUtil
from api.user.user_api import add_user_api

@pytest.fixture
def add_user_fixture(token_fixture):
    """
    添加用户夹具：会先清理同邮箱数据，创建新用户并返回 ID，测试结束后自动删除
    """
    user_data = {
        "name": "test_user_fixture",
        "email": "fixture@example.com"
    }

    # 用 DB 强清理旧数据
    db = DBUtil()
    db.delete_user_by_email(user_data["email"])
    db.close()

    # 添加用户
    resp = add_user_api(user_data, token_fixture)
    assert resp.status_code == 201
    user_id = resp.json().get("id")
    print(f"✅ 用户添加成功，ID：{user_id}")

    yield user_id  # 返回用户 ID 给测试用例使用

    # 测试后清理（删除用户）
    print(f"🧹 测试结束，删除用户 ID：{user_id}")
    from api.user.user_api import delete_user_api
    del_resp = delete_user_api(user_id, token_fixture)
    print(f"🗑️ 删除响应：{del_resp.status_code} - {del_resp.text}")


# tests/conftest/right_fixtures.py

import pytest
from api.service.rights_api import create_rights
from utils.db_util import DBUtil  # 若你想加数据库清理
from api.common.auth_util import AuthUtil

@pytest.fixture
def rights_fixture(token_fixture):
    data = {"name": "自动化权益", "status": "active"}
    resp = create_rights(data, token_fixture)
    assert resp.status_code == 201
    rights_id = resp.json()["id"]
    yield rights_id

    # 可选：自动清理数据库（非必需）
    db = DBUtil()
    db.delete_rights_by_id(rights_id)
    db.close()


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



