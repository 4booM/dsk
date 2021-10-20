import random
randint=(random.randint(1,10))
print("游戏规则：初始金币为5，当金币大于7时成功通关。")
print("只有三次机会，用完即出局")
print("提示",randint)
x=5
y=3
print("你剩余的金币",x)
while x>=0  :
    if x==7 :
        print("我超？")
        break
    else:
        while 0<= y <= 3:
            print("你还剩下的机会：", y)

            num = int(input("请输入一个数字"))
            if num == randint:
                print("太对了哥，哥太对!")
                x=x+1
                break
            elif num > randint:
                print("大了大了，金币-1")
                y = y - 1
                x = x - 1
                print("你还剩下的金币", x)

                if y==0:
                    break
            elif num < randint:
                print("小了小了,金币-1")
                y = y - 1
                x = x - 1
                print("你还剩下的金币", x)

                if y==0:
                    break
    if y==0:
        print("这里水太深你把握不住")
        print("滚出我们5个9直播间")
        break
    print("你还剩下的金币", x)
    print("你还剩下机会",y)
    randint = (random.randint(1, 10))







