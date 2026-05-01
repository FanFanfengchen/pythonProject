import time

# 获取当前时间戳（秒级时间戳）
timestamp = time.time()
print("当前时间戳（秒）:", timestamp)

# 获取当前时间戳（毫秒级时间戳）
timestamp_ms = int(round(time.time() * 1000))
print("当前时间戳（毫秒）:", timestamp_ms)


import time
from datetime import datetime

# 将秒级时间戳转换为日期时间
timestamp = time.time()
dt = datetime.fromtimestamp(timestamp)
print("从时间戳转换为日期时间:", dt)

# 将毫秒级时间戳转换为日期时间
timestamp_ms = 1672531200000  # 示例毫秒级时间戳
dt_ms = datetime.fromtimestamp(timestamp_ms / 1000)
print("从毫秒级时间戳转换为日期时间:", dt_ms)


from datetime import datetime

# 将日期时间转换为秒级时间戳
dt = datetime.now()
timestamp = dt.timestamp()
print("从日期时间转换为时间戳（秒）:", timestamp)

# 将日期时间转换为毫秒级时间戳
timestamp_ms = int(dt.timestamp() * 1000)
print("从日期时间转换为时间戳（毫秒）:", timestamp_ms)


import time
from datetime import datetime

# 获取当前时间戳并格式化为日期时间字符串
timestamp = time.time()
formatted_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
print("格式化的时间:", formatted_time)


from datetime import datetime

# 计算两个时间戳之间的时间差
timestamp1 = time.time()
time.sleep(2)  # 模拟等待2秒
timestamp2 = time.time()

# 计算时间差（秒）
time_diff = timestamp2 - timestamp1
print("时间差（秒）:", time_diff)


from datetime import datetime, timedelta

# 创建一个日期时间对象
dt = datetime.now()
print("当前日期时间:", dt)

# 添加时间
new_dt = dt + timedelta(days=1, hours=2, minutes=30)
print("添加时间后:", new_dt)

# 减去时间
old_dt = dt - timedelta(days=1)
print("减去时间后:", old_dt)


from datetime import datetime

# 定义两个日期时间
start_time = datetime(2024, 1, 1)
end_time = datetime(2024, 1, 15)

# 计算时间戳差
time_diff = (end_time - start_time).total_seconds()
print("两个日期之间的时间戳差（秒）:", time_diff)

# 使用 time.time() 来控制循环时间
import time

# 设置循环的最大运行时间（秒）
max_duration = 5  # 例如，让循环运行 5 秒

# 记录循环开始的时间
start_time = time.time()

while True:
    # 检查是否超过时间限制
    if time.time() - start_time > max_duration:
        print("循环运行时间已超过限制，停止循环。")
        break

    # 循环内的代码
    print("我是time.time()")
    time.sleep(1)  # 模拟每次循环耗时 1 秒

# 使用 datetime.timedelta 来控制循环时间
from datetime import datetime, timedelta

# 设置循环的最大运行时间（秒）
max_duration = 5  # 例如，让循环运行 5 秒

# 记录循环开始的时间
start_time = datetime.now()

while True:
    # 检查是否超过时间限制
    if (datetime.now() - start_time).total_seconds() > max_duration:
        print("循环运行时间已超过限制，停止循环。")
        break

    # 循环内的代码
    print("我是datetime.timedelta")
    time.sleep(1)  # 模拟每次循环耗时 1 秒


# # 使用 signal 模块（仅限 Unix 系统）
# import signal
# import time
#
# # 定义一个标志变量，用于控制循环
# stop_loop = False
#
# # 定义信号处理函数
# def handle_timeout(signum, frame):
#     global stop_loop
#     print("时间限制已到，停止循环。")
#     stop_loop = True
#
# # 设置信号处理
# signal.signal(signal.SIGALRM, handle_timeout)
# signal.alarm(5)  # 设置 5 秒后发送 SIGALRM 信号
#
# try:
#     while not stop_loop:
#         print("循环正在运行...")
#         time.sleep(1)  # 模拟每次循环耗时 1 秒
# finally:
#     signal.alarm(0)  # 取消定时信号

# 使用多线程
import threading
import time

# 定义一个标志变量，用于控制循环
stop_loop = False

# 定义一个函数来控制循环时间
def stop_after_timeout(timeout):
    global stop_loop
    time.sleep(timeout)
    stop_loop = True
    print("时间限制已到，停止循环。")

# 设置时间限制
timeout = 5  # 例如，让循环运行 5 秒

# 启动一个线程来控制时间
thread = threading.Thread(target=stop_after_timeout, args=(timeout,))
thread.start()

# 主循环
while not stop_loop:
    print("注意，我是多线程")
    time.sleep(1)  # 模拟每次循环耗时 1 秒

thread.join()  # 等待线程结束


# 使用 asyncio（异步方式）
import asyncio

async def main():
    # 设置循环的最大运行时间（秒）
    max_duration = 5  # 例如，让循环运行 5 秒

    # 记录循环开始的时间
    start_time = asyncio.get_event_loop().time()

    while True:
        # 检查是否超过时间限制
        if asyncio.get_event_loop().time() - start_time > max_duration:
            print("循环运行时间已超过限制，停止循环。")
            break

        # 循环内的代码
        print("我是asyncio")
        await asyncio.sleep(1)  # 模拟每次循环耗时 1 秒

# 运行异步主函数
asyncio.run(main())
