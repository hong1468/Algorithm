len = int(input())
top = list(map(int, input().split(" ")))
stk = []
answer = []
for i in range(len):
    while stk:
        if stk[-1][1] > top[i]:
            answer.append(stk[-1][0] + 1)
            break
        else:
            stk.pop()
    if not stk:
        answer.append(0)
    stk.append([i, top[i]])

print(" ".join(map(str,answer)))