"""
    顺序：从左到右，从上到下
"""
# 第一个，try语句，除零错误
try:
    m1 = int(input("请输入第一个分子："))
    m2 = int(input("请输入第一个分母："))
    result = m1 / m2
    print(result)  # 打印结果(补全)
except ZeroDivisionError:
    print("出错了，分母不能为0")

# 第二个，一切的开始，打印字符串
print("hello world!")

# 第三个，for循环判断，范围11次，判断成绩等级
a = -1
for i in range(11):
    if a == 10:
        print("{}：优秀".format(a))
    elif 10 > a >= 8:
        print("{}：良好".format(a))
    elif 8 > a >= 6:
        print("{}：合格".format(a))
    else:
        print("{}：继续努力".format(a))

# 第四个（不完整）
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(20, 2), columns=["A", "B"])
df.plot.scatter(x="A", y="B", color="red", s=40)
ax1 = plt.gca(y='B', color='blue', s=40)
df.plot.line(x="A", y="B", color="blue", s=40)
label = plt.gca(y='B', color='blue', ax=ax1)

# 第五个
def printap(n, a0, d):
    an = 0
    dn = list()
    for i in range(n):
        an = a0 + i * d
        dn.append(an)
    return dn

print(printap(3, 5, 10))
print(printap(a0=5, n=10, d=2))
