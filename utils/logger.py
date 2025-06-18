# utils/logger.py
from loguru import logger
import os
import yaml

# 日志目录
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# 读取配置
def load_log_config():
    default = {"level": "INFO", "rotation": "10 MB", "retention": "7 days"}
    try:
        with open("config/config.yaml", encoding="utf-8") as f:
            conf = yaml.safe_load(f)
            return conf.get("log", default)
    except Exception:
        return default

log_config = load_log_config()

# 清除默认控制台 logger，避免重复打印
logger.remove()

# 添加新的日志 sink（输出）
logger.add(
    os.path.join(log_dir, "log_{time:YYYYMMDD_HHmmss}.log"),
    rotation=log_config["rotation"],
    retention=log_config["retention"],
    encoding="utf-8",
    level=log_config["level"],
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{module}</cyan> - <level>{message}</level>"
)

# 控制台输出（可选）
logger.add(
    sink=lambda msg: print(msg, end=""),  # 控制台输出格式
    level=log_config["level"],
    format="<light-blue>{time:HH:mm:ss}</light-blue> | <level>{level}</level> | <cyan>{message}</cyan>"
)
