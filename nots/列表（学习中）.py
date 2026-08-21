# 定义：能装东西的东西
# 在python中用[]来表示一个列表。列表中的元素通过， 来隔开
a = ["张三", "李四", "王五", "赵六", [1, 2, 3, True]]
# 特性：
#   1.也像字符串一样也有索引和切片
#   2.索引如果超过范围就会抛出IndexError异常
#   3.可以用for循环遍历列表
#   4.可以用len获得列表的长度
lst = ["张三", "李四", "王五", "赵六"]
#
# print(lst[0])  # 张三
# print(lst[1:3])  # ['李四', '王五']
# print(lst[::-1])  # ['赵六', '王五', '李四', '张三']
# print(lst[3652])  # IndexError: list index out of range
# for item in lst:
#     print(item)
# print(len(lst))

# 4.2====================================================
# 列表的增删改查
# lst = []
# 向列表中添加内容
# append()  追加
lst.append("李四")
lst.append("王五")
lst.append("赵六")
# insert()  插入
lst.insert(0, "张三")
# extend()  可以合并两个列表，批量的添加
lst.extend(['武则天', '嬴政', ' 马超'])
print(lst)

# 删除列表中的内容
# pop()  删除列表末尾的元素，并返回该元素
ret = lst.pop(3)
print(lst)
print(ret)
# remove()  删除列表中指定的元素
lst.remove("张三")
print(lst)

# 修改
lst[0] = "张三"
print(lst)  # 直接用索引进行修改
