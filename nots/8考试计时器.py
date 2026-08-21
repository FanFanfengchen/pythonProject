import time
import turtle
from datetime import datetime, timedelta

# 存储所有考试信息的列表
exams = []


def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculate_time_difference(target_time):
    try:
        current_time = datetime.now()
        target = datetime.strptime(target_time, "%Y-%m-%d %H:%M:%S")
        return (target - current_time).total_seconds()
    except ValueError:
        return None


def load_sample_data():
    """加载预设的测试数据"""
    global exams
    # 清空现有数据
    exams = []

    # 获取当前时间
    now = datetime.now()

    # 添加几个测试考试信息
    exams.append({
        "subject": "数学",
        "start_time": (now + timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S"),
        "duration": 120
    })

    exams.append({
        "subject": "英语",
        "start_time": (now + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S"),
        "duration": 90
    })

    exams.append({
        "subject": "语文",
        "start_time": (now - timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S"),
        "duration": 120
    })

    print("已加载预设测试数据:")
    for exam in exams:
        print(f"  {exam['subject']}: {exam['start_time']} (时长: {exam['duration']}分钟)")


def format_time(seconds):
    """将秒数格式化为 HH:MM:SS 格式"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def draw_countdowns(t):
    t.clear()
    current_time = get_current_time()
    t.penup()
    t.goto(-200, 200)
    t.pendown()
    t.write(f"当前时间: {current_time}", font=("Arial", 12, "normal"))
    t.penup()
    t.goto(-200, 180)
    t.pendown()
    t.write("-" * 50, font=("Arial", 12, "normal"))
    t.penup()
    t.goto(-200, 160)
    t.pendown()
    t.write("科目\t开始时间\t距离开始倒计时\t考试倒计时", font=("Arial", 12, "normal"))
    t.penup()
    t.goto(-200, 140)
    t.pendown()
    t.write("-" * 50, font=("Arial", 12, "normal"))
    y = 120
    for exam in exams:
        subject = exam["subject"]
        start_time = exam["start_time"]
        duration = exam["duration"]
        time_diff = calculate_time_difference(start_time)

        if time_diff is None:
            countdown = "时间格式错误"
            exam_countdown = "时间格式错误"
        elif time_diff > 0:
            countdown = format_time(time_diff)
            exam_countdown = "未开始"
        else:
            elapsed_time = abs(time_diff)
            if elapsed_time < duration * 60:
                remaining_time = duration * 60 - elapsed_time
                exam_countdown = format_time(remaining_time)
                countdown = "已开始"
            else:
                countdown = "已结束"
                exam_countdown = "已结束"
        t.penup()
        t.goto(-200, y)
        t.pendown()
        t.write(
            f"{subject}\t{start_time}\t{countdown}\t\t{exam_countdown}",
            font=("Arial", 12, "normal"),
        )
        y -= 20
    t.penup()
    t.goto(-200, y)
    t.pendown()
    t.write("-" * 50, font=("Arial", 12, "normal"))
    t.penup()
    t.goto(-200, y - 20)
    t.pendown()
    t.write("按 'q' 键退出", font=("Arial", 12, "normal"))


def input_exam_info():
    while True:
        subject = input("请输入科目（输入 'q' 退出，输入 'test' 加载测试数据）: ")
        if subject.lower() == "q":
            return False
        elif subject.lower() == "test":
            load_sample_data()
            return True

        start_date = input("请输入考试开始日期（YYYY-MM-DD）: ")
        start_time = input("请输入考试开始时间（HH:MM:SS）: ")
        try:
            duration = int(input("请输入考试时长（分钟）: "))
            # 处理中文冒号问题
            start_time = start_time.replace("：", ":")
            full_start_time = f"{start_date} {start_time}"
            # 验证时间格式
            datetime.strptime(full_start_time, "%Y-%m-%d %H:%M:%S")
            exams.append(
                {"subject": subject, "start_time": full_start_time, "duration": duration}
            )
            print(f"已添加考试: {subject}")
        except ValueError as e:
            print("输入格式错误，请重新输入！")
            print("请确保日期格式为 YYYY-MM-DD，时间格式为 HH:MM:SS")
            print(f"错误详情: {e}")


def main():
    print("欢迎使用考场倒计时系统")
    if not input_exam_info():
        return

    # 设置turtle屏幕
    screen = turtle.Screen()
    screen.title("考场倒计时")
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    # 设置屏幕监听
    screen.onkey(screen.bye, "q")
    screen.listen()

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("black")

    # 使用tracer和update来改善刷新体验，减少闪烁
    screen.tracer(0)  # 关闭自动刷新

    try:
        while True:
            draw_countdowns(t)
            screen.update()  # 手动刷新屏幕
            time.sleep(1)
    except turtle.Terminator:
        print("程序已退出")


if __name__ == "__main__":
    main()