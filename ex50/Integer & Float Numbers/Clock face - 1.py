h = int(input())
m = int(input())
s = int(input())

hangle = h * 30

MtoHangle = (m / 60) * 30
StoHangle = (s / 3600) * 30

print(hangle + MtoHangle + StoHangle)