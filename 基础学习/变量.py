"""
    变量的基础应用
"""
a1 = 100
b1 = 200
print(a1, b1, '装逼，我让你飞起来')  # 比如说，这是一个简单的代码

a = input("第一个数字：")
b = input("第二个数字：")
# print(type(a))#查看变量类型
a = int(a)
b = int(b)
# print(type(a))
print(a+b)

A = input("请输入一个三位数")
A = int(A)
hundreds_place = A // 100
tens_place = A // 10 - hundreds_place * 10
ones_place = A % 10
print(ones_place, hundreds_place, tens_place)

b = input('请输入：')
c = b[0]
d = b[1]
e = b[2]
print(c, ',', d, ',', e)
# 分别以数学方法和字符串方法来分解一个三位数，并输出其各位数字。


a2 = 50
b2 = 100
c2 = 200
print(a2 * b2 / c2)  # 还可以进行计算
print(a2 + b2)
print("你好，晚上好")

a = 10
b = 15
print(a+b)
print(a-b)
print(a*b)
print(a/b)
if a < b:
    print('a < b')
if a > b:
    print('a > b')
if a == b:
    print('a == b')
if a >= b:
    print('a >= b')
if a <= b:
    print('a <= b')

flag = False
name = 'linux'
if name == 'linux':         # 判断变量是否为 Linux ！
    flag = True             # 如果判断成功，并且运行到这，就会知错就改，改成真的
    print('你好啊，新同学！')   # 然后告诉你成功了
else:
    print(name)             # 你的名字我不认识，程序也是

a = 20
b = 10
c = 15
d = 5

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("(a + b) * c / d 运算结果为：", e)  # 输出上面的式子

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：", e)  # 费手

e = (a + b) * (c / d)  # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：", e)  # 一对对照组

e = a + (b * c) / d  # 20 + (150/5)
print("a + (b * c) / d 运算结果为：", e)  # 看，电灯泡

num = 0
if num == 3:       # 固定思想
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num == 0:
    print('join the club')  # 彼此彼此，一样倒霉
elif num < 0:
    print('error')
else:
    print('i see it')

cai = 9
if 0 <= cai <= 10:
    # 判断值是否在0~10之间
    print('你好，你好，你好！')  # 输出：我不好

cai = 10
if 0 > cai > 10:
    # 判断值是否在小于0或大于10
    print('我上早八')
else:
    print('宝了个贝的，这是给我干那来了，这还是国内吗？')
# 输出结果：孩子，这并不好笑

cai = 8
# 判断值是否在0~5或者10~15之间
if (0 <= cai <= 5) or (10 <= cai <= 15):
    print('我测你温码')
else:
    print('我是丁真，这是我的好朋友芝士雪豹。')
# 输出：嗷呜~ 雪豹别叫!

age1 = input('输入您的年龄: ')  # 输入你的年龄
print(age1)  # 给你买瓜子去

x1 = 10
y1 = 5
s1 = x1 * y1
print(s1)  # 50

result = '我' + '和' + '你'
print(result)

a3, b3, c3 = 1, 2, 'jojo'
print(a3, b3, c3)

a4 = 21
b4 = 10
c4 = 0

if a4 == b4:
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if a4 != b4:
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if a4 != b4:
    print("3 - a 不等于 b")
else:
    print("3 - a 等于 b")

if a4 < b4:
    print("4 - a 小于 b")
else:
    print("4 - a 大于等于 b")

if a4 > b4:
    print("5 - a 大于 b")
else:
    print("5 - a 小于等于 b")

# 修改变量 a 和 b 的值
a5 = 5
b5 = 20
if a5 <= b5:
    print("6 - a 小于等于 b")
else:
    print("6 - a 大于  b")

if b5 >= a5:
    print("7 - b 大于等于 a")
else:
    print("7 - b 小于 a")

money = int(input("交出你的money，哈哈哈: "))
if money >= 500:
    print("太好啦，是钱，我们有救了！")
else:
    print("太好了，让我们进入米奇妙妙屋。")
if money >= 1000:
    if 1000 < money < 5000:
        print('加油加油！')
    elif money == 1000:
        print('有所懈怠了呀。')
    if money == 1000:
        print('刚刚好，是不是故意的？')
if 500 <= money <= 1000:
    if money == 500:
        print('回家吧，你也不希望在外面出丑吧？')
    if money == 1000:
        print('不是故意的，就是有意的！')
    if 500 < money < 1000:
        print('你的想法真是让人捉摸不透啊！')
    else:
        print('嘿，你瞅啥呢，我是你蝶！')

s = "这是真的啊，你不会忘了吧？"
for i in s:
    print("这一次，请确定:",i)

for i in range(10): #从0数到10，但不包含10
    print(i)

for i in range(3,10): #3~9
    print(i)

i = 1
while i <= 10:
    print(i)
    i = i + 2

for i in range(1,10,2):
    print(i)

x = 10
if x > 5:
    pass  # 跳过，下次想好了再补充
print("吹牛逼呢，见过吗，这叫俄罗斯大贝塔，你就只能看着我骑")

a = int(input("来来来："))
b = 0
while b <= 100:  # 用while循环
    print(a)
    b = b + 1
    a = a + b
    print(b)
    a = a - b
    # break 用break直接结束循环

count = 0  # 设定函数值为0
while count < 9:  # 在当函数值小于9的条件下循环输出以下内容
    print('The count is:', count)  # 输出，包含下一个变量
    count = count + 1  # 每一次循环都加1

print("Good bye!")  # 不成熟的解释

var = 1
while var == 1:  # 该条件永远为true，循环将无限执行下去
    num = input("随便 :")  # 随便写一个，回车
    print("写了个寂寞: ", num)  # 输出你刚刚写下的东西
print("拜拜!")  # 友好的再见

count = 0
while count < 5:
    print(count, " is  less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")

flag = 1
while flag:
    print('Given flag is really true!')
print("Good bye!")

for num in range(10, 20):  # 迭代 10 到 20 (不包含) 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print('%d 是一个质数' % num)

i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j = j + 1
    if j > i / j:
        print(i, " 是素数")
    i = i + 1

print("Good bye!")

import time

keep_running = True
start_time = time.time()

while keep_running:
    print('Given flag is really true!')
    # 5 秒后终止循环
    if time.time() - start_time > 5:
        keep_running = False
    time.sleep(0.1)  # 降低 CPU 占用

print("Good bye!")

# float:小数，浮点数
# 比如:
a = 10.57
print(a)
# 但是，有一个无限小数点
# 比如：
print(10 / 3)  # 它的输出的最后一位存在误差，说明关于无穷，计算机也是只能给出不准确的数
# 还有，小数的数据范围是无限的，而整数会在某一个特定区间内是可以清楚表示的
# 就像你与你命中注定的人的距离，处于小数时，距离是可以无限近和无限远的。但是，处于整数时，在一瞬间，你们两个的关系就明确了
# 计算机是一款二进制产品，语言基础就：0,1，人家本来就难，不要强迫别人，所以，计算机在表示一个小数时是会有误差的
bool
