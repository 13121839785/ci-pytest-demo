import allure
from api.common.request_util import RequestUtil

@allure.feature("用户模块")
@allure.story("获取用户信息（使用有效 token）")
def test_user_profile_with_token():
    url = "http://127.0.0.1:5000/user/profile"

    with allure.step("通过封装工具类发起 GET 请求，自动携带 token"):
        resp = RequestUtil().get(url)
        allure.attach(str(resp.status_code), name="响应状态码", attachment_type=allure.attachment_type.TEXT)
        allure.attach(resp.text, name="响应内容", attachment_type=allure.attachment_type.JSON)

    with allure.step("断言状态码为 200"):
        assert resp.status_code == 200

    with allure.step("断言响应中包含 username 和 email 字段"):
        resp_json = resp.json()
        assert "username" in resp_json
        assert "email" in resp_json
