classA = int(input())
classB = int(input())
classC = int(input())

NumDesksA = ((classA // 2) + (classA % 2))
NumDesksB = ((classB // 2) + (classB % 2))
NumDesksC = ((classC // 2) + (classC % 2))
TotNumDesks = NumDesksA + NumDesksB + NumDesksC

print(TotNumDesks)