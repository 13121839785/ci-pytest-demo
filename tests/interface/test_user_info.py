import pytest
import allure
from api.common.request_util import RequestUtil

@allure.feature("用户模块")
@allure.story("获取用户信息")
def test_get_user_info():
    user_id = 1
    url = f"https://dummyjson.com/users/{user_id}"

    with allure.step("发送 GET 请求获取用户信息"):
        resp = RequestUtil().get(url)
        allure.attach(str(resp.status_code), name="响应状态码", attachment_type=allure.attachment_type.TEXT)
        allure.attach(resp.text, name="响应内容", attachment_type=allure.attachment_type.JSON)

    with allure.step("断言状态码为 200"):
        assert resp.status_code == 200

    with allure.step("断言返回的用户 ID 正确"):
        json_data = resp.json()
        assert json_data["id"] == user_id

    with allure.step("断言返回结果中包含 firstName 字段"):
        assert "firstName" in json_data
