import pytest
import yaml
import os
from api.common.request_util import RequestUtil

def load_login_test_data():
    file_path = os.path.join(os.path.dirname(__file__), '../data/user_data.yaml')
    with open(file_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data['login_test']

@pytest.mark.parametrize("case", load_login_test_data())
def test_login(case):
    username = case["username"]
    password = case["password"]
    expected_code = case["expected_code"]

    print(f"\n🧪 测试登录用户：{username}，预期状态码：{expected_code}")

    url = "http://127.0.0.1:5000/login"
    payload = {
        "username": username,
        "password": password
    }

    response = RequestUtil(use_token=False).post(url, json=payload)

    print("📄 实际状态码：", response.status_code)
    print("📄 响应体：", response.json())

    assert response.status_code == expected_code
