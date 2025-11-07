c = True
while c:
    print("欢迎来到数字大小比较，114514👇")
    a = float(input("输入第一个数："))
    b = float(input("输入第二个数："))
    if a >= b:
        print("两个数中较大的数:{}", format(a))
    elif a == 114514:
        c = False
    else:
        print("两个数中较大的数:{}", format(b))
