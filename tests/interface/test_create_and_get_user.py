
# test_create_and_get_user.py

import allure  # 用于生成测试报告步骤和标题
from utils.db_util import DBUtil  # 导入我们刚写的数据库工具类
from utils.logger import logger  # ✅ 不是 import logger



@allure.feature("用户模块")  # 在报告中归类为“用户模块”
@allure.story("添加并查询用户")  # 报告中的子模块名称
@allure.title("添加用户并通过数据库验证是否写入成功")  # 用例标题
def test_create_and_get_user(add_user_fixture, token_fixture):  # 自动接收夹具返回的用户 ID 和 token
    user_id = add_user_fixture  # 获取夹具返回的 user_id

    with allure.step("数据库校验：验证新增用户已写入数据库"):  # Allure 报告中标注的测试步骤
        db = DBUtil()  # 实例化数据库操作类，连接数据库
        result = db.fetch_user_by_id(user_id)  # 查询数据库中是否存在该 ID 的用户
        db.close()  # 查询完毕后关闭连接，防止连接泄露

        logger.info(f"📊 数据库查询结果: {result}")  # 打印数据库返回值，方便调试和查看

        assert result is not None, "❌ 数据库中未查到该用户"  # 校验查询结果非空
        assert result[0] == user_id, "❌ 用户 ID 与数据库不一致"  # 校验 ID 是否匹配
