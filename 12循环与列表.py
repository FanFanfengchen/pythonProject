for i in range(25):
    print("老师我错了，我再也不偷偷藏手机了")
a = []
print(type(a))
for _ in range(0, 10):
    b = a.append(_)
print(a)
an = False
a = 0
while not an:
    a += 1
    if a > 10:  # 添加退出条件避免无限循环
        an = True
print(a)