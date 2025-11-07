s = 'abc123456'

# 获取字符串长度
n = len(s)
print(f"字符串 '{s}' 的长度是: {n}")

# 正向索引示例
print("\n正向索引:")
for i in range(n):
    print(f"s[{i}] = '{s[i]}'")

# 负向索引示例
print("\n负向索引:")
for i in range(-1, -n-1, -1):
    print(f"s[{i}] = '{s[i]}'")

# 特殊情况：s[0] 和 s[-n] 指向同一元素
print(f"\n特殊情况:")
print(f"s[0] = '{s[0]}'")
print(f"s[-n] = '{s[-n]}'")
print(f"它们是否相等: {s[0] == s[-n]}")

# 可视化对应关系
print("\n索引对应关系:")
for i in range(n):
    print(f"正向索引 {i} <--> 负向索引 {i-n} (都指向字符 '{s[i]}')")