"""
    一开始的代码
    记得，文件名不能用“——”（破折号）来命名，不然你会收到报错，虽然来说对我的影响不大
"""
# 4页 图1-2
print("ab" in "acbd")
print("a" not in "acbd")
print("ac" in "acbd")

# 6页 图1-5
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# 一、变量


spor_1_name = "001"
# 创建了一个由数字“001”组成的变量，并且给它起了一个变量名spor_1_name
print(spor_1_name)

"""
    1.命名规则
    (1) 变量名的首字符必须是下划线、英文字母或Unicode字符。
    (2) 变量名可以包含下划线、英文字母、数字或Unicode字符。
    (3) 变量名区分大小写。
    (4) 变量名不能和Python中的保留关键字重名。
"""

# 2.赋值

# 变量=表达式
# (1) 给一个变量赋值
m = 100
print(m)
# (2) 给多个变量赋值
m,n = 200,300
print(m,n)


# 二、注释


# 1.单行注释
# Python中单行注释使用符号“#”，当前行中#以及后面的内容为注释内容。注释符号可以放在语句开头，也可以放在语句末尾。
m = "abcd", "ef"        # 单行注释

# 2.多行注释

# Python中多行注释使用的符号为三个英文的三个双引号“"""”或单引号“'''”。注释符号放在语句的开始和结束之间，中间的内容为注释内容。
# 多行注释的示例
'''
多行注释开始
逗号分隔字符串，组成元组
多行注释结果
'''
m = "abcd", "ef"


# 三、输入输出


# 1.基本输入
# Python中使用input()函数输入语句，可以带参数，也可以不带参数，所带提示参数为字符串。基本语法格式如下：

# 变量名 = input()
# 变量名 = input("提示字符串")

# 示例1代码：
m = input()  # 不带参数
print(m)

# 示例2代码：
m = input("请输入数据：")  # 带参数
print(m)

# 2.输出
# Python中使用print()函数输出语句，可以带参数，也可以不带参数，所带参数为字符串。基本语法格式如下：
# 不带参数
# m = print()
# 带参数，可以多个参数，用分号作为分隔符
# print('0, 1, 2')
#
