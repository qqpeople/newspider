# 一元二次方程自动计算

import math

print("请输入一元二次方程的三个系数：")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    print("此一元二次方程无解")
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("此一元二次方程无实数解")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("此一元二次方程的解为：")

        if x1 == x2:
            print(f"x1 = x2 = {x1}")
        else:
            print("x1 = ", x1)
            print("x2 = ", x2)