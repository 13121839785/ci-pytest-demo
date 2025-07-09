from api.common.request_util import RequestUtil

def test_get_user_by_valid_id():
    url = "http://127.0.0.1:5000/user/1"
    resp = RequestUtil().get(url)

    print("\n✅ 查询结果：", resp.json())
    assert resp.status_code == 200
    assert resp.json()["name"] == "Alice"

def test_get_user_by_invalid_id():
    url = "http://127.0.0.1:5000/user/999"
    resp = RequestUtil().get(url)

    print("\n❌ 查询结果：", resp.json())
    assert resp.status_code == 404
    assert resp.json()["message"] == "User not found"

def test_get_user_without_token():
    url = "http://127.0.0.1:5000/user/1"
    resp = RequestUtil(use_token=False).get(url)

    print("\n🔒 未登录查询：", resp.json())
    assert resp.status_code == 401
    assert resp.json()["message"] == "Unauthorized"
