from api.common.request_util import RequestUtil

def test_user_profile_with_fixture_token(token_fixture):
#自动运行 token_fixture()；

# 获取返回的 token 值；
#
# 然后把它当作参数传给你的测试函数。
    url = "http://127.0.0.1:5000/user/profile"

    # 使用 token_fixture 构造带 token 的请求工具
    req = RequestUtil()
    req.headers["Authorization"] = f"Bearer {token_fixture}"

    resp = req.get(url)

    print("\n📄 状态码：", resp.status_code)
    print("📄 响应体：", resp.json())

    assert resp.status_code == 200
    assert "username" in resp.json()
