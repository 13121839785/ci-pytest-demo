import pytest
from api.common.request_util import RequestUtil

def test_delete_user_success(token_fixture):
    url = "http://127.0.0.1:5000/user/delete/3"
    req = RequestUtil(use_token=False)
    req.headers["Authorization"] = f"Bearer {token_fixture}"
    resp = req.delete(url)
    print("✅ 删除成功：", resp.json())
    assert resp.status_code == 200
    assert resp.json()["message"] == "User deleted"

def test_delete_user_not_found(token_fixture):
    url = "http://127.0.0.1:5000/user/delete/999"
    req = RequestUtil(use_token=False)
    req.headers["Authorization"] = f"Bearer {token_fixture}"
    resp = req.delete(url)
    print("❌ 用户不存在：", resp.json())
    assert resp.status_code == 404
    assert resp.json()["message"] == "User not found"

def test_delete_user_unauthorized():
    url = "http://127.0.0.1:5000/user/delete/1"
    resp = RequestUtil(use_token=False).delete(url)
    print("🔒 未登录删除：", resp.json())
    assert resp.status_code == 401
    assert resp.json()["message"] == "Unauthorized"
