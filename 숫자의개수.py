num=1
for i in range(3):
    num *= int(input())
num = str(num)
answer = [0]*10
for j in range(len(answer)):
    print(num.count(str(j)))
