x = float(input('第一个数字:'))
y = float(input('第二个数字:'))
op = input('请输入运算方法:')
yu = 0
if op == '加法' or op == '加' or op == '+':
    yu = x+y
elif op == '减法' or op == '减' or op == '-':
    yu = x-y
elif op == '乘法' or op == '乘' or op == '*':
    yu = x*y
elif op == '除法' or op == '除' or op == '/':
    yu = x/y
else:
    print("运算方法输入错误")
if yu == 23.0:
    print('你爸得了MVP！，这个赛季评分是23.0！')
else:
    print('最终得出：', yu)