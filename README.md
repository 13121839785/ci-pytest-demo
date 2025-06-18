# ci-pytest-demo

本项目是一个集成 **UI 自动化测试** 和 **接口自动化测试** 的综合性测试框架，基于 `pytest` 构建，并支持 **GitHub Actions 持续集成**，可生成 HTML 报告并上传构建产物。

---

## 📁 项目结构说明

ci-pytest-demo/
├── .github/workflows/ # CI 配置
│ └── python-ci.yml
├── api/ # 接口测试封装
│ └── common/
│ └── request_util.py # 封装请求方法的工具类
├── config/
│ └── config.yaml # 接口测试环境基础配置
├── data/
│ └── user_data.yaml # 接口测试数据
├── pages/ # UI 页面对象封装（Page Object）
│ ├── inventory_page.py
│ ├── login_page.py
│ └── init.py
├── tests/ # 所有 UI 与接口测试用例
│ ├── test_user_api.py # 接口自动化测试用例
│ ├── test_login.py # UI 登录测试
│ ├── test_cart.py # UI 添加购物车测试
│ ├── conftest.py # 公共 fixture 和 driver 初始化
│ └── init.py
├── requirements.txt # 所有依赖库
├── pytest.ini # pytest 配置文件
├── README.md # 项目说明文档

---

## 🔧 安装依赖

推荐使用虚拟环境后运行：

```bash
pip install -r requirements.txt

🧪 运行测试
1. 运行所有测试（UI + API）
pytest
2. 仅运行接口测试
pytest -m api
3. 仅运行 UI 测试
pytest -m ui
🖥️ 查看本地 HTML 报告
执行测试后会在项目根目录生成 report.html，可双击打开查看测试报告。

🚀 GitHub Actions 自动化运行
每次 push / PR 时自动触发测试：

生成并上传 HTML 报告

上传为构建产物（artifact）

CI 配置位于 .github/workflows/python-ci.yml

📌 技术栈
Python 3.10+

pytest + selenium

requests + yaml

GitHub Actions CI

pytest-html（HTML 报告）

