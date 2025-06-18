import pytest
from api.common.request_util import RequestUtil

# 🔐 更新成功：使用夹具提供 token
def test_update_user_success(token_fixture):
    url = "http://127.0.0.1:5000/user/1"
    payload = {
        "name": "Alice Updated",
        "email": "alice.new@example.com"
    }

    req = RequestUtil(use_token=False)
    req.headers["Authorization"] = f"Bearer {token_fixture}"
    resp = req.put(url, json=payload)

    print("\n✅ 更新成功：", resp.json())
    assert resp.status_code == 200
    assert resp.json()["user"]["name"] == "Alice Updated"


# ❌ 用户不存在：也需要 token
def test_update_user_not_found(token_fixture):
    url = "http://127.0.0.1:5000/user/999"
    payload = {
        "name": "Ghost",
        "email": "ghost@example.com"
    }

    req = RequestUtil(use_token=False)
    req.headers["Authorization"] = f"Bearer {token_fixture}"
    resp = req.put(url, json=payload)

    print("\n❌ 用户不存在：", resp.json())
    assert resp.status_code == 404
    assert resp.json()["message"] == "User not found"


# 🔒 未授权更新（无 token）
def test_update_user_unauthorized():
    url = "http://127.0.0.1:5000/user/1"
    payload = {
        "name": "Hack",
        "email": "hack@example.com"
    }

    resp = RequestUtil(use_token=False).put(url, json=payload)

    print("\n🔒 未授权更新：", resp.json())
    assert resp.status_code == 401
