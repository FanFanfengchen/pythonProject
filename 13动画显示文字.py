import time

"""a = int(input("a请输入一个任意数:"))
b = int(input("b请输入一个任意数:"))


def liangshuzhihe(a, b):
    i = a + b
    return i


print(liangshuzhihe(a, b))

"""
"""

def fand(year, mouth, day):
    sum = 0
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        lst = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(mouth - 1):
            sum += lst[i]
        return sum + day
    else:
        lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31]
        for i in range(mouth - 1):
            sum += lst[i]
        return sum + day


year = int(input("请输入年："))
mouth = int(input("月："))
day = int(input("日："))
sum = fand(year, mouth, day)
print(sum)
"""
'''
def fdd(a):
    if

chr(21521)
chr(27426)
'''


def qdd(spk):
    for _ in spk:
        print('===', flush=True, end='')
        time.sleep(0.35)
    for i in spk:
        print(i, flush=True, end='')
        time.sleep(0.36)
    for _ in spk:
        print('===', flush=True, end='')
        time.sleep(0.35)
    print('')


def print_ak47(spkk):
    print(ord(spkk))


c = chr(26361)
b = chr(21338)
d = c + b
qdd(d)
zho = chr(21608)
zhi = chr(24535)
wei = chr(20255)
zhozhiwei = zho + zhi + wei
qdd(zhozhiwei)
hu = chr(32993)
yu = chr(23431)
xuan = chr(36713)
qdd(hu + yu + xuan)
yu = chr(20313)
xun = chr(33600)
qdd(yu + xun)
zhang = chr(24352)
fa = chr(21457)
biao = chr(26631)
qdd(zhang + fa + biao)
