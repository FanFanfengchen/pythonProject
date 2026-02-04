s = "物联网241"
print(len(s))

# 角古猜想实现式
n = int(input('请输入：'))
while True:
    if n % 2:
        n = n / 2
    else:
        n = n * 3 + 1
    if n == 1:
        print(n)
        break
