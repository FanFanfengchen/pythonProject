import time

ck = 0
qq = 0
aa = True
while aa:
    print('=======================================================================')
    xz = str(input("输入你的选择（1.存钱 2.查看存款 3.取钱 4.退出）："))
    if xz == '1':
        ck = int(input("请输入要存入的钱："))
        print("现在已存：", ck)
    elif xz == '2':
        print("当前的存款：", ck)
    elif xz == '3':
        qq = int(input("输入想取出的钱："))
        for i in range(10):
            ck -= qq
        print("已取出：", qq, "\n剩余：", ck)
    elif xz == '4':
        print('已退出。。。。。。')
        aa = False
    for i in range(10):
        ck += 1
    time.sleep(0.5)
    print('\n')

