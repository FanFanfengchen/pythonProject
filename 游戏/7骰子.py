"""s = "只因你实在是太美"
s0 = s[0:2]
s1 = s[2]
s2 = s[6:9]
s3 = f"{s0}{s1}{s2}"
print(s3)
import math

a = float(input("请输入直角边a的长度: "))
b = float(input("请输入直角边b的长度: "))
c = math.sqrt(a ** 2 + b ** 2)
print("斜边c的长度为:", c)
height = float(input('身高(cm)：'))
weight = float(input('体重(kg)：'))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if 18.5 <= bmi < 24:
    print('你的身材很棒！')
status_code = int(input('响应状态码: '))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)
status_code = int(input('响应状态码: '))
match status_code:
    case 400 | 405: description = 'Invalid Request'
    case 401 | 403 | 404: description = 'Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'{y = }')"""
"""
从1到100的偶数求和

Version: 1.2
Author: 骆昊
"""
# print(sum(range(2, 101, 2)))
"""
打印乘法口诀表

Version: 1.0
Author: 骆昊
"""
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}×{j}={i * j}', end='\t')
    print()"""
"""
猜数字小游戏

Version: 1.0
Author: 骆昊
"""
"""import random

answer = random.randrange(1, 101)
counter = 0
while True:
    counter += 1
    num = int(input('请输入: '))
    if num < answer:
        print('大一点.')
    elif num > answer:
        print('小一点.')
    else:
        print('猜对了.')
        break
print(f'你一共猜了{counter}次.')"""
"""
百钱百鸡问题

Version: 1.1
Author: 骆昊
"""
"""
for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')"""
"""
Craps赌博游戏

Version: 1.0
Author: 骆昊
"""
import random
import time

money = 10000000
number_of_times = 0
game_player = 0
dealer = 0
while True:
    while money > 0:
        number_of_times += 1
        print(f'第{number_of_times}局\n你的总资产为: {money}元')
        # time.sleep(2)
        # 下注金额必须大于0且小于等于玩家的总资产
        while True:
            # debt = int(input('请下注: '))
            debt = random.randint(1, money)
            # debt = money
            print(f'你下注了{debt}元')
            time.sleep(0.5)
            if 0 < debt <= money:
                break
        # 用两个1到6均匀分布的随机数相加模拟摇两颗色子得到的点数
        first_point = random.randrange(1, 7) + random.randrange(1, 7)
        print(f'\n玩家摇出了{first_point}点')
        if first_point == 7 or first_point == 11 or first_point == 5:
            print('玩家胜!\n')
            money += debt
            game_player += 1
        elif first_point == 2 or first_point == 3 or first_point == 12:
            print('庄家胜!\n')
            money -= debt
            dealer += 1
        else:
            # 如果第一次摇色子没有分出胜负，玩家需要重新摇色子
            while True:
                current_point = random.randrange(1, 7) + random.randrange(1, 7)
                print(f'玩家摇出了{current_point}点')
                if current_point == 7:
                    print('庄家胜!\n')
                    money -= debt
                    dealer += 1
                    break
                elif current_point == first_point:
                    print('玩家胜!\n')
                    money += debt
                    game_player += 1
                    break
    print(f'你破产了, 游戏结束!\n已自动进行了{number_of_times}局游戏\n你胜利了{game_player}局, 失败了{dealer}局')
    anan = input('是否继续游戏(an): ')
    if anan == 'an':
        money = 10000000
        number_of_times = 0
        game_player = 0
        dealer = 0
    else:
        break
