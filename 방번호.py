num = input()
answer = [0] * 10
for i in range(len(num)):
    n = int(num[i])
    if n == 6 or n == 9:
        if answer[6] <= answer[9]:
            answer[6] += 1
        else:
            answer[9] += 1
    else:
        answer[n] += 1
print(max(answer))
