import hashlib
import os

def hash_password(password):
    """对密码进行哈希处理"""
    return hashlib.sha256(password.encode()).hexdigest()

# 从环境变量获取配置，若不存在则使用默认值（仅用于演示）
CORRECT_ACCOUNT = os.getenv("APP_ACCOUNT", "abc")
# 使用哈希值存储，避免明文密码
CORRECT_PASSWORD_HASH = os.getenv("APP_PASSWORD_HASH", hash_password("Small_Jie"))

account = input("请输入账号：")
password = input("请输入密码：")

# 验证时使用哈希比较
if account == CORRECT_ACCOUNT and hash_password(password) == CORRECT_PASSWORD_HASH:
    print("登录成功")
else:
    print("登录失败")
