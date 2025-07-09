import requests
import allure

@allure.feature("用户模块")
@allure.story("获取用户信息（缺少 token，应返回 401）")
def test_user_profile_without_token():
    url = "http://127.0.0.1:5000/user/profile"

    with allure.step("直接发送 GET 请求，不携带 token"):
        resp = requests.get(url)
        allure.attach(str(resp.status_code), name="响应状态码", attachment_type=allure.attachment_type.TEXT)
        allure.attach(resp.text, name="响应内容", attachment_type=allure.attachment_type.TEXT)

    with allure.step("断言状态码为 401（未授权）"):
        assert resp.status_code == 401

    with allure.step("断言响应内容中包含 Unauthorized"):
        assert "Unauthorized" in resp.text
