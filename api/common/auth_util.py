import requests
from api.common.config_util import ConfigUtil

class AuthUtil:
    _cached_token = None  # 缓存

    @staticmethod
    def get_token():
        if AuthUtil._cached_token:
            print("✅ 使用缓存 token")
            return AuthUtil._cached_token

        print("🔐 正在发起登录请求...")
        config = ConfigUtil.load_config()
        url = config["base_url"] + "/login"
        payload = {
            "username": config["username"],
            "password": config["password"]
        }
        headers = {"Content-Type": "application/json"}

        resp = requests.post(url, json=payload, headers=headers)
        resp.raise_for_status()
        AuthUtil._cached_token = resp.json()["token"]
        return AuthUtil._cached_token
