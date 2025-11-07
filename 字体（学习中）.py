"""
    古代的称一斤是16两 33 二斤    一两
    练习：在控制台中获取两，计算是几斤几两。
        显示几斤几两

"""
"""
weight_liang = int(input("请输入两："))
jin = weight_liang // 16
liang = weight_liang % 16
print("{}两 = {}斤{}两".format(weight_liang, jin, liang))
"""
"""
company_num = 66
avg_salary = 10000
message = "公司人数是%s，平均工资是%s" % (company_num, avg_salary)  # 当有多个变量占位时，变量要用括号括起来并按照占位的顺序填入
print(message)
"""
# 字符串格式化
# ==========================================
# 格式符号    转化
# %s         将内容转化为字符串，放入占位位置
# %d         将内容转化为整数，放入占位位置
# %f         将内容转化为浮点数，放入占位位置
"""
name = "水果苹果"
born_year = 1900
pre_price = 10.5
print(f"我是{name}，我出生在{born_year}年，我的今天的均价是{pre_price}元")
print("1 * 1的结果是：%d" % (1*1))
print(f"1 * 1的结果是：{1 * 1}")
print("字符串在python中的类型是：%s" % type('字符串'))
"""
'''
name = "橙子"
good_name = 1008
pre_price = 19.99
pre_price_daily_group_factor = 1.2
growth_days = 7
reached = pre_price*pre_price_daily_group_factor**growth_days
print1 = f"产品：{name}，商品编号：{good_name}，当前均价：{pre_price}"
print2 = "每日增长系数：%.1f，经过%d天的增长后，均价到达了：%.2f" % (pre_price_daily_group_factor, growth_days, reached)
print(print1)
print(print2)
print("""当时年少掷春光，花马踏蹄酒溅香。
爱恨情仇随浪来，夏蝉歌醒夜未央。
光阴长河种红莲，韶光重回泪以干。
今刻沧桑登舞榭，万灵且待命无缰。
    """)
'''
'''
result = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1
print(result)
'''
'''
row = 1
while row <= 5:
    print("*" * row)
    row += 1
'''
'''
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print("")
    row += 1
'''
'''
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print('%d * %d = %d' % (row, col, row * col), end="\t")
        col += 1
    print("")
    row += 1
'''
'''
列表定义
list.insert(index, elements)  # 在指定位置插入元素
list.append(elements)  # 在末尾追加元素
list.extend()  # 将列表2的元素追加到列表1中
list[index] = elements  # 修改指定索引的元素
dellist[index]  # 删除指定索引的元素
list.remove(elements)  # 删除指定索引的元素
list.pop()  # 删除末尾的元素
list.pop(index)  # 删除指定索引的元素，并返回该元素
list.clear()  # 清空列表
len(list)  # 列表长度
list.count(elements)  # 列表中元素出现的次数
list.sort()  # 列表升序排序
list.sort(reverse=True)  # 列表降序排序
list.reverse()  # 列表逆序、翻转
'''
''''
# 定义一个列表
name_list = ["张三", "李四", "王五", "赵六", "孙七", "周八", "吴九", "郑十"]
print(name_list)

# 在指定位置插入元素
name_list.insert(0, "夏洛")
print(name_list)
name_list.insert(2, "顾安")
print(name_list)

# 在列表末尾添加一个元素
name_list.append("大海")
print(name_list)

# 在指定位置修改元素
name_list[1] = "木木"
print(name_list)

# 删除指定元素
del name_list[4]
print(name_list)

# 删除列表中出现的第一个元素
name_list.append("张三")
print(name_list)
name_list.remove("张三")
print(name_list)

# pop 删除
name_list.pop()
print(name_list)
name_list.pop(0)
print(name_list)


# 清除整个列表
# name_list.clear()
# print(name_list)

# 统计 索引计数，从0开始；列表长度计算从1开始
print(len(name_list))

# 统计列表中元素出现的次数
name_list.append("木木")
print(name_list)
print(name_list.count("木木"))

# 列表排序
number_list = [1, 5, 3, 9, 7, 2, 4, 6, 8]

# 升序
number_list.sort()
print(number_list)

# 降序
number_list.sort(reverse=True)
print(number_list)

# 逆序
number_list.reverse()
print(number_list)

# 循环取值
print(number_list)
for i in number_list:
    print(i)
    print(type(i))


for i in name_list:
    print(i)
    print(type(i))

# ============extend 添加一个列表或合并============
text_1 = [1, 2, 3]
text_2 = [4, 5, 6]
text_1.extend(text_2)
print(text_1)
'''
"""
# 定义一个元组
info_data = ("张三", "男", 18)
print(type(info_data))
info_data_1 = ()
print(type(info_data_1))

# 在声明元组时，如果元组中的值只有一个，那么必须在这个值后面添加一个逗号
info_data_2 = (1)
print(type(info_data_2))
info_data_2 = (1,)
print(type(info_data_2))

# 统计元组中元素出现的次数
info_data = (1, 2, 1, 5, 4, 6, 3, 2, 1)
print(info_data.count(1))

# index 指当前元素的下标
print(info_data.index(5))

print("============循环遍历=============")
for i in info_data:
    print(i)

print(type(info_data))
print(type(list(info_data)))
print(type(tuple(info_data)))
"""
""""
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "sex": "男",
            "height": 1.75}
print(type(xiaoming))
'''
字典定义
len(字典) 获取字典的 键值对数量
----------+--------- 
| key     +  values |
----------+---------  
| name    +   小明   | 
| age     +   18    |
| gender  +   True  | 
| sex     +   男    |
| height  +   1.75  |
----------+--------- 
字典.keys()所有 key 列表
字典.values() 所有 value 列表
字典.items() 所有（key.value）元组列表
字典[key] 可以从字典中取值， key 不存在会报错
字典.get(key) 可以从字典中取值， key 不存在不会报错
del 字典[key] 删除指定键值对， key 不存在会报错
字典.pop(key) 删除指定键值对， key 不存在会报错
字典.popitem() 随机删除一个键值对
字典.clear() 清空字典
字典.copy() 复制字典
字典.fromkeys() 创建一个字典

字典[key] = value
  如果 key 存在，修改数据
  如果 key 不存在，新建键值对

字典.setdefault(key, value) 
  如果 key 存在，不会修改数据
  如果 key 不存在，新建键值对

字典.update(字典2) 将字典 2 的数据合并到字典1 
'''
# 字典取值
print(xiaoming['name'])
# print(xiaoming['address'])
print(xiaoming.get('address'))
print(xiaoming.keys())
print(xiaoming.values())
print(xiaoming.items())

del xiaoming['gender']
print(xiaoming)
# 打印要删除的值
print(xiaoming.pop('age'))
# 打印当前处理过的字典
print(xiaoming)

# 随机删除
# print(xiaoming.popitem())
# 修改键的值
xiaoming['name'] = 'xiaohong(小红)'
print(xiaoming)

# 循环遍历
for k, v in xiaoming.items():
    print(k, v)

for k in xiaoming:
    print("%s: %s" % (k, xiaoming[k]))
"""
"""
string = "hello python"

for c in string:
    print(c)

print(string[1])

# 切片
print(string[3:9])
'''
1)判断类型
方法                 说明
string.isspace()    如果 string 中只包含空格，则返回 True
string.isalnum()    如果 string 至少有一个字符串并且所有字符都是字母或数字则返回 True
string.isalpha()    如果 string 至少有一个字符串并且所有字符都是字母则返回 True
string.isdecimal()  如果 string 只包含数字则返回 True，全角数字
string.isdigit()    如果 string 只包含数字则返回 True，全角数字、（1）、\o00b2
string.isnumeric()  如果 string 只包含数字则返回 True，全角数字，汉字数字
string.istitle()    如果 string 是标题化的（每个单词的首字母大写）则返回 True
string.islower()    如果 string 中包含至少一个区分大小的字符，并且所有这些（区分大小写的）字符都是小写，则返回 True
string.isupper()    如果 string 中包含至少一个区分大小的字符，并且所有这些（区分大小写的）字符都是大写，则返回 True
'''
s1 = "hello word"
print(s1.capitalize())

s1.title()
print(s1.title())

s1.upper()
print(s1.upper())

s2 = "Hello Word"

s2.lower()
print(s2.lower())
"""

s = "hello word!"

print(s.find("or"))
print(s.rfind("shit"))
print(s.index("or"))
print(s.index("shit"))








