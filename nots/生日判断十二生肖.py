# 正确的生肖列表（索引4对应鼠年）
sheng_xiao = ["猴", "鸡", "狗", "猪", "鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊"]

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

id_card = input("请输入18位身份证号码：")

if len(id_card) != 18:
    print("错误：身份证必须是18位！")
else:
    year = int(id_card[6:10])
    month = int(id_card[10:12])
    day = int(id_card[12:14])

    if month < 1 or month > 12:
        print("错误：月份必须是1-12！")
    else:
        # 闰年判断（2月）
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                max_day = 29
            else:
                max_day = 28
        else:
            max_day = days_in_month[month - 1]

        if day < 1 or day > max_day:
            print(f"错误：{year}年{month}月最多有{max_day}天！")
        else:
            print(f"您的生日：{year}年{month}月{day}日")
            print(f"生肖：{sheng_xiao[year % 12]}")