import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
switch_input = 24
led_output = 25
GPIO.setup(switch_input, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_output, GPIO.OUT)


def led(channel):
    time.sleep(0.01)
    input_state = GPIO.input(switch_input)
    if input_state == 0:
        print("输入状态是%d按键按下，led灯点亮！" % input_state)
        GPIO.output(led_output, GPIO.HIGH)
    else:
        print('输入状态是%d按键释放，led灯点亮' % input_state)
        GPIO.output(led_output, GPIO.LOW)


GPIO.add_event_detect(switch_input, GPIO.BOTH, callback=led, bouncetime=5)

i = 0
try:
    while True:
        time.sleep(1)
        i = i + 1
        print('程序已经运行了%d秒！' % i)
except KeyboardInterrupt:
    print('Bye!LED is OFF!')
finally:
    GPIO.remove_event_detect(switch_input)
