import hashlib
from time import sleep

def hash_password(password):
    """对密码进行哈希处理"""
    return hashlib.sha256(password.encode()).hexdigest()

print('====================注册阶段=====================')
sleep(1)
account = input('请输入账号：')
password = input('请输入密码：')

# 使用哈希存储密码
hashed_password = hash_password(password)

a = False

while not a:
    print('====================登录阶段=====================')
    sleep(1)
    verifyYourAccount = input('请输入账号：')
    verifyThePassword = input('请输入密码：')

    # 验证时使用哈希比较
    if verifyYourAccount == account and hash_password(verifyThePassword) == hashed_password:
        print('账号密码正确，登录成功！')
        a = True
    elif verifyYourAccount != account:
        print('账号错误')
    elif hash_password(verifyThePassword) != hashed_password:
        print('密码错误')
    else:
        print('账号和密码错误')
