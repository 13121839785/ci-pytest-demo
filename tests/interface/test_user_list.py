from api.common.request_util import RequestUtil

def test_user_list_with_params():
    url = "http://127.0.0.1:5000/user/list"
    params = {"page": 2, "size": 3}

    resp = RequestUtil().get(url, params=params)
    json_data = resp.json()
    print("【完整响应信息】")
    print("状态码：", resp.status_code)
    print("头信息：", resp.headers)
    print("响应体（text）：", resp.text)
    print("响应体（json）：", resp.json())
    print("请求URL：", resp.url)

    print("响应内容：", json_data)

    assert resp.status_code == 200
    assert json_data["page"] == 2
    assert json_data["size"] == 3
    assert isinstance(json_data["data"], list) #判断对象的变量类型
    assert len(json_data["data"]) <= 3  # size 限制生效
