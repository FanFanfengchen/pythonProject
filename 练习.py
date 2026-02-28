# number_list = [56, 23, -5, 96]
# number_list[4]


# print(56 /(12 - 15 + 3))


# f = open("./hi.txt", "r")


# "yoo" * "hi"
"""
while True:
    try:
        user_weight = float(input("请输入您的体重（单位：kg）："))
        user_height = float(input("请输入您的身高（单位：m）："))
        user_BMI = user_weight / user_height ** 2
    except ValueError:
        print("输入内容不合理。")
    except ZeroDivisionError:
        print("身高不能为0。")
    except:
        print("发生未知错误...")
    else:
        print(f"您的BMI值为{user_BMI}")
        break
    finally:
        print("该回合结束")
"""
def calculate_and_print(num, calculator):
    result = calculator(num)
    print(f""" 
    | 数字参数 | {num} |
    | 计算结果 | {result} | """)

def calculate_square(num):
    return num * num

def calculate_cube(num):
    return num ** 3

def calculate_plus_10(num):
    return num + 10

# 错误的调用示例（注释掉）
# calculate_and_print(3, 2)  # 错误：第二个参数应该是函数，不是整数
# calculate_and_print(3, 3)  # 错误：第二个参数应该是函数，不是整数
# calculate_and_print(3, 4)  # 错误：第二个参数应该是函数，不是整数

# 正确地调用示例：使用已定义的函数
calculate_and_print(3, calculate_plus_10)
# 正确用法示例：
# calculate_and_print(5, lambda arguments: arguments ** 2)  # 计算5的平方

# 或者修改函数定义使其只接受一个参数（计算函数），然后在函数内部使用默认数字
# def calculate_and_print(calculator):
#     num = 3  # 默认数字
#     result = calculator(num)
#     print(f"""
#     | 数字参数 | {num} |
#     | 计算结果 | {result} | """)

# 然后可以这样调用：
# calculate_and_print(lambda arguments: arguments ** 2)

# 测试正确用法示例
calculate_and_print(5, lambda arguments: arguments ** 2)  # 计算5的平方
calculate_and_print(10, lambda x: x * 2)  # 计算10的2倍
calculate_and_print(7, lambda n: n + 5)  # 计算7加5
