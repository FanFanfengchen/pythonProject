lists = ['What can I say?', 786, 2.23, 'jojo', 70.2]
tiny = [123, 'jojo']
print(lists)
print(lists[0])
print(lists[1:3])
print(lists[2:])
print(tiny * 2)
print(lists + tiny)

a = '就凭你也配直视我！'  # 神
b = '把头低下！'  # 精
list1 = ['诶呀', '真的是你呀', '哈哈', '嗐呦', 'baby']  # 练习生

if a in list1:  # 如果，“神”在“练习生”里。就告诉你，勇敢去做，否则，没有不可能
    print("勇敢去做")  # 对
else:  # 不
    print("没有不可能")  # 对

if b not in list1:  # 如果“神经”在“练习生”里，就偷懒
    print("2 - 变量 b 不在给定的列表中 list 中")  # 懒
else:  # 否则
    print("2 - 变量 b 在给定的列表中 list 中")  # 偷

# 改变了一个东西
a = '真的是你呀'  # 练习时长两年半
if a in list1:  # 如果你有两年半的练习
    print("3 - 变量 a 在给定的列表中 list 中")  # 你就练习了两年半
else:  # 杂鱼
    print("3 - 变量 a 不在给定的列表中 list 中")  # 月色真美，风也温柔

for letter in '一个字，绝':  # 第一个实例
    print("看看看看: %s" % letter)

fruits = ['唱', '跳', 'rap', '篮球']
for fruit in fruits:  # 第二个实例
    print('真的是你呀，哈哈！: %s' % fruit)
print("拜拜!")

fruits = ['鸡', '你', '太美']
for index in range(len(fruits)):
    print('真的是你呀！哈哈 ： %s' % fruits[index])

print("bey bey!")