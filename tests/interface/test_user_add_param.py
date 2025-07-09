#test_user_add_param.py
import pytest
import os
import yaml
import allure
from api.common.request_util import RequestUtil
from api.common.config_util import ConfigUtil  # ✅ 新增导入 ConfigUtil
from api.user.user_api import add_user_api


def load_test_data():
    """
    从 data/user_data.yaml 加载参数化数据
    """
    current_dir = os.path.dirname(__file__)
    data_path = os.path.abspath(os.path.join(current_dir, "../data/user_data.yaml"))
    with open(data_path, encoding="utf-8") as f:
        return yaml.safe_load(f)["add_user_param"]


@allure.feature("用户模块")
@allure.story("参数化添加用户")
@pytest.mark.parametrize("user_data", load_test_data())
@allure.title("添加用户 - {user_data[name]}")
def test_add_user_param(user_data, token_fixture):
    config = ConfigUtil.load_config()  # ✅ 加载配置
    url = config["base_url"] + "/user/add"  # ✅ 从配置中获取 base_url

    req = RequestUtil(use_token=False)
    req.headers["Authorization"] = f"Bearer {token_fixture}"

    with allure.step("发送添加用户请求"):
        allure.attach(str(user_data), "请求数据", allure.attachment_type.JSON)
        resp = add_user_api(user_data, token_fixture)
        allure.attach(str(resp.status_code), "响应状态码", allure.attachment_type.TEXT)
        allure.attach(resp.text, "响应内容", allure.attachment_type.JSON)

    with allure.step("校验响应是否成功"):
        assert resp.status_code == 201
        assert "User added successfully" in resp.text
