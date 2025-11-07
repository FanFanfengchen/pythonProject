from time import *

print('====================注册阶段=====================')
sleep(1)
account = input('请输入账号：')
password = input('请输入密码：')

a = False

while not a:
    print('====================登录阶段=====================')
    sleep(1)
    verifyYourAccount = input('请输入账号：')
    verifyThePassword = input('请输入密码：')

    if verifyYourAccount == account and verifyThePassword == password:
        print('账号密码正确，', '登录成功！')
        a = True
    elif verifyYourAccount != account:
        print('账号错误')
    elif verifyThePassword != password:
        print('密码错误')
    else:
        print('账号和密码错误')
