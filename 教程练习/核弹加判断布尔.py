import string
import time

# s1 = "The world!"
# s2 = "Are you OK!"
s3 = "I am atomic"
# print("wo" in s1)
# print("wo" not in s1)
# print("wo" in s1)
# print("you" in s2)
# print("wo" not in s2)
for char in s3:
    print(char, flush=True, end="")
    time.sleep(0.27)
print()


def an(n, c=1):
    if c > n:
        return
    print('!' * (c - 1) + "!" * (2 * (n - c)) + '!' * (c - 1))
    an(n, c + 1)


def fire(n, c=1):
    if c > len(n):
        return
    print([ch for ch in n])
    fire(n, c + 1)


def nuke(n):
    a = []
    for i in range(10):
        if n > 1:
            a.append(nuke(n - 1))
        else:
            a.append(i)
    return a


while True:
    an(100)
    fire(string.digits)  # （重复了两遍）
    fire(string.ascii_letters)  # a
    # print(nuke(10))  # 该递归不要随便执行

