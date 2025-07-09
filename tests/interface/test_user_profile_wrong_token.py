import requests


def test_user_profile_with_wrong_token():
    url = "http://127.0.0.1:5000/user/profile"
    headers = {"Authorization": "Bearer wrong-token"}
    resp = requests.get(url, headers=headers)
    print("状态码：", resp.status_code)
    print("响应内容：", resp.text)
    assert resp.status_code == 401
