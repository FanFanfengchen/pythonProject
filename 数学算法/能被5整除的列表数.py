import random
lst1 = [random.randint(1, 20) for _ in range(10)]
print(f"lst1为: {lst1}")
lst2 = []
for _ in lst1:
    if _ % 5 == 0:
        lst2.append(_)
print(f"lst2 (能被5整除的数字)为: {lst2}")
