"""
    内存燃烧器（来源：火柴人vs编程）
"""
import string  # 后面的递归要用


def fire(n, c=1):
    # 递归函数，n为层数，c为当前层数,def定义一个函数，使用这个函数时需要传入参数，若参数在定义时有默认值则可以省略
    if c > n:  # 递归结束条件，是则返，否则跳
        return  # 返回
    print(' ' * (c - 1) + '*' * (2 * (n - c) + 1))  # 输出层数
    fire(n, c + 1)  # 递归调用，层数加1,什么，居然没有输出？


fire(5)


def fire(n, c=1):
    if c > len(n):
        return
    print([ch for ch in n])
    fire(n, c + 1)


fire(string.digits)  # （重复了两遍）
fire(string.ascii_letters)  # ascii码是由美国国家标准化办制定的一种字符编码标准，它将文字符号（英文字母、阿拉伯数字、标点符号等）编码为二进制数，并使用计算机的存储和传输设备进行传输。


def nuke(n):
    a = []
    for i in range(1000):
        if n > 1:
            a.append(nuke(n - 1))
        else:
            a.append(i)
    return a


# print(nuke(10))  # 该递归不要随便执行
