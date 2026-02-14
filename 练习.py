print("你好，我是一个收集数字的爱好者，喜欢给你收集到的数字的整合的平均值")
user_input = input("好了，请输入数字，方便收藏：")
total, count = 0, 0
while user_input != "q" and user_input.isdigit():
    total += float(user_input)
    count += 1
    user_input = input("还有吗？\n：")
if count > 0:
    print(f"好了，给你：{total / count:.2f}")
else:
    print("请给我数字！其它的我不要！")
