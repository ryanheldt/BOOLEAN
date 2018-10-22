h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

s1total = ((h1 * 60 * 60) + (m1 * 60) + s1)
s2total = ((h2 * 60 * 60) + (m2 * 60) + s2)

if s1total > s2total:
    sTotal = s1total - s2total
else:
    sTotal = s2total - s1total
    
print(sTotal)
