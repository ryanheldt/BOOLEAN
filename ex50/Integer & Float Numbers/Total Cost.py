d = int(input())
c = int(input())
n = int(input())

totC = ((d * 100) + c) * n

totD = 0
while totC > 100 or totC == 100:
    totC -= 100
    totD += 1
    
print(str(totD) + " " + str(totC))