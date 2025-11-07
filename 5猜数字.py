import random
secret = random.randint(1, 10)
num = input("猜猜我现在心里想的是哪个数字？")
guess = int(num)
times = 1
while guess != secret and times < 4:
    if guess > secret:
        print("你猜大了哦,杂鱼")
    else:
        print("你猜小了哦,杂鱼")
    num = input("真是，废物！")
    guess = int(num)
    times = times + 1
if times < 4 and guess == secret:
    print("哎呀，你真厉害，那就给你点奖励吧，糖果")
else:
    print("给你三次机会都猜不中，垃圾，废物，杂鱼！")
