from time import *

print('====================注册阶段=====================')
sleep(1)
zhanghao = input('请输入账号：')
mima = input('请输入密码：')

a = False

while not a:
    print('====================登录阶段=====================')
    sleep(1)
    yanzhengzhanghao = input('请输入账号：')
    yanzhengmima = input('请输入密码：')

    if yanzhengzhanghao == zhanghao and yanzhengmima == mima:
        print('账号密码正确，', '登录成功！')
        a = True
    elif yanzhengzhanghao != zhanghao:
        print('账号错误')
    elif yanzhengmima != mima:
        print('密码错误')
    else:
        print('账号和密码错误')