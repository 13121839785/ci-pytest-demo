import allure
from api.common.request_util import RequestUtil

@allure.feature("用户模块")
@allure.story("用户生命周期：添加 → 查询 → 自动清理")
def test_create_and_get_user(add_user_fixture, token_fixture):
    user_id = add_user_fixture

    with allure.step("使用用户 ID 查询用户信息"):
        url = f"http://127.0.0.1:5000/user/{user_id}"
        req = RequestUtil(use_token=False)
        req.headers["Authorization"] = f"Bearer {token_fixture}"
        resp = req.get(url)

        allure.attach(str(resp.status_code), "响应状态码", allure.attachment_type.TEXT)
        allure.attach(resp.text, "响应内容", allure.attachment_type.JSON)

    with allure.step("断言返回的用户 ID 正确"):
        assert resp.status_code == 200
        assert resp.json()["id"] == user_id

    with allure.step("✅ 测试结束后，用户将自动被删除（由夹具完成）"):
        pass  # 删除逻辑在夹具的 yield 后执行
