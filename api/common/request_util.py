import requests
from api.common.auth_util import AuthUtil
from utils.logger import logger
from utils.exceptions import ApiRequestError

class RequestUtil:
    def __init__(self, use_token=True):
        self.headers = {}
        if use_token:
            token = AuthUtil.get_token()
            self.headers["Authorization"] = f"Bearer {token}"

    def get(self, url, params=None, headers=None):
        headers = headers or self.headers
        try:
            logger.info(f"📤 [GET] 请求 URL: {url} | Params: {params}")
            resp = requests.get(url, params=params, headers=headers)
            logger.info(f"📥 [GET] 响应状态码: {resp.status_code}")
            logger.debug(f"📄 响应内容: {resp.text}")

            if resp.status_code >= 400:
                raise ApiRequestError("GET 请求失败", url, resp.status_code)
            return resp
        except Exception as e:
            logger.error(f"❌ GET 请求异常: {e}")
            raise

    def post(self, url, json=None, headers=None):
        headers = headers or {}
        merged = {**self.headers, **headers}
        try:
            logger.info(f"📤 [POST] 请求 URL: {url} | JSON: {json}")
            resp = requests.post(url, json=json, headers=merged)
            logger.info(f"📥 [POST] 响应状态码: {resp.status_code}")
            logger.debug(f"📄 响应内容: {resp.text}")

            if resp.status_code >= 400:
                raise ApiRequestError("POST 请求失败", url, resp.status_code)
            return resp
        except Exception as e:
            logger.error(f"❌ POST 请求异常: {e}")
            raise

    def put(self, url, json=None, headers=None):
        headers = headers or self.headers
        try:
            logger.info(f"📤 [PUT] 请求 URL: {url} | JSON: {json}")
            resp = requests.put(url, json=json, headers=headers)
            logger.info(f"📥 [PUT] 响应状态码: {resp.status_code}")
            logger.debug(f"📄 响应内容: {resp.text}")

            if resp.status_code >= 400:
                raise ApiRequestError("PUT 请求失败", url, resp.status_code)
            return resp
        except Exception as e:
            logger.error(f"❌ PUT 请求异常: {e}")
            raise

    def delete(self, url, headers=None):
        headers = headers or self.headers
        try:
            logger.info(f"📤 [DELETE] 请求 URL: {url}")
            resp = requests.delete(url, headers=headers)
            logger.info(f"📥 [DELETE] 响应状态码: {resp.status_code}")
            logger.debug(f"📄 响应内容: {resp.text}")

            if resp.status_code >= 400:
                raise ApiRequestError("DELETE 请求失败", url, resp.status_code)
            return resp
        except Exception as e:
            logger.error(f"❌ DELETE 请求异常: {e}")
            raise
