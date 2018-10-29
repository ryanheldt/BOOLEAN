num = int(input())
ones = num % 10
tens = num % 100
tens = int(tens / 10)
hundreds = num % 1000
hundreds = int(hundreds / 100)
finNum = ones + tens + hundreds
print(finNum)