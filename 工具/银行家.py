import time

deposit = 0
takeMoney = 0
state = True
while state:
    print('=======================================================================')
    now = str(input("输入你的选择（1.存钱 2.查看存款 3.取钱 4.退出）："))
    if now == '1':
        deposit = int(input("请输入要存入的钱："))
        print("现在已存：", deposit)
    elif now == '2':
        print("当前的存款：", deposit)
    elif now == '3':
        takeMoney = int(input("输入想取出的钱："))
        for i in range(10):
            deposit -= takeMoney
        print("已取出：", takeMoney, "\n剩余：", deposit)
    elif now == '4':
        print('已退出。。。。。。')
        state = False
    else:
        print('该选项不在选择中，请重新输入。')
    for i in range(10):
        deposit += 1
    time.sleep(0.5)
    print('\n')

