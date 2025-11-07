import time
from datetime import datetime

# 记录程序开始时间
start_time = time.time()
# 设置运行时长（秒）
duration = 10  # 运行10秒后自动结束

print(f"程序开始运行，将持续 {duration} 秒...")

while True:
    # 获取当前时间并显示
    current_time = time.time()
    formatted_time = datetime.fromtimestamp(current_time).strftime("%Y-%m-%d %H:%M:%S")
    print("时间:", formatted_time)

    # 计算已经运行的时间
    elapsed_time = current_time - start_time

    # 如果超过设定时长则退出
    if elapsed_time >= duration:
        print(f"程序已运行 {duration} 秒，自动退出。")
        break

    time.sleep(1)