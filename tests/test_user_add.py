from api.common.request_util import RequestUtil

from api.common.auth_util import AuthUtil

def test_token():
    token = AuthUtil.get_token()
    print("当前获取到的 token 是：", token)

def test_add_user_success():
    url = "http://127.0.0.1:5000/user/add"
    payload = {
        "name": "Charlie",
        "email": "charlie@example.com"
    }
    headers = {"Content-Type": "application/json"}
    resp = RequestUtil().post(url, json=payload,headers=headers)
    print("\n状态码：", resp.status_code)
    print("响应体：", resp.text)

    assert resp.status_code == 201
    assert "user" in resp.json()
    assert resp.json()["user"]["name"] == "Charlie"

def test_add_user_missing_field():
    url = "http://127.0.0.1:5000/user/add"
    payload = {
        "name": "NoEmail"  # 缺 email
    }
    headers = {"Content-Type": "application/json"}
    resp = RequestUtil().post(url, json=payload,headers=headers)
    print("\n状态码（缺字段）：", resp.status_code)
    print("响应体：", resp.text)

    assert resp.status_code == 400
    assert "Missing" in resp.json()["message"]

def test_add_user_without_token():
    url = "http://127.0.0.1:5000/user/add"
    payload = {
        "name": "NoAuth",
        "email": "noauth@example.com"
    }
    headers = {"Content-Type": "application/json"}

    # 不带 token，设置 use_token=False
    resp = RequestUtil(use_token=False).post(url, json=payload,headers=headers)
    print("\n状态码（未登录）：", resp.status_code)
    print("响应体：", resp.text)

    assert resp.status_code == 401
    assert "Unauthorized" in resp.json()["message"]
