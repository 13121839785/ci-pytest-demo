# utils/exceptions.py
class ApiRequestError(Exception):
    def __init__(self, message, url=None, status_code=None):
        self.url = url
        self.status_code = status_code
        super().__init__(f"{message} | URL: {url} | 状态码: {status_code}")
