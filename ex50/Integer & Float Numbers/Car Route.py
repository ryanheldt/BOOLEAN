import math

n = int(input())
m = int(input())

dis = m / n
dis2 = m // n
if dis > dis2:
    finDis = math.ceil(dis)
else:
    finDis = math.floor(dis)

print(finDis)