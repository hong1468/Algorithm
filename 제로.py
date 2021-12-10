k = int(input())
answer = []
for i in range(k):
    new = int(input())
    if new == 0:
        answer.pop()
    else:
        answer.append(new)
if answer:
    print(sum(answer))
else:
    print(0)