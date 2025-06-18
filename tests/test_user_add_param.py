import pytest
import os
import yaml
import allure
from api.common.request_util import RequestUtil

# 加载测试数据
def load_test_data():
    current_dir = os.path.dirname(__file__)
    data_path = os.path.abspath(os.path.join(current_dir, "../data/user_data.yaml"))
    with open(data_path, encoding='utf-8') as f:
        return yaml.safe_load(f)["add_user"]

@allure.feature("用户模块")
@allure.story("添加用户")
@pytest.mark.parametrize("user_data", load_test_data())
@allure.title("添加用户参数化用例 - {user_data[name]}")
def test_add_user_param_with_fixture(user_data, token_fixture):
    url = "http://127.0.0.1:5000/user/add"

    with allure.step("准备请求对象并注入 token"):
        req = RequestUtil(use_token=False)
        req.headers["Authorization"] = f"Bearer {token_fixture}"

    with allure.step("发送添加用户请求"):
        allure.attach(str(user_data), "请求数据", allure.attachment_type.JSON)
        resp = req.post(url, json=user_data)
        allure.attach(str(resp.status_code), "响应状态码", allure.attachment_type.TEXT)
        allure.attach(resp.text, "响应内容", allure.attachment_type.JSON)

    with allure.step("断言响应结果是否符合预期"):
        if not user_data["name"] or not user_data["email"]:
            assert resp.status_code == 400
            assert "Missing" in resp.text
        else:
            assert resp.status_code == 201
            assert "User added successfully" in resp.text
