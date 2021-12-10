N, K = map(int,input().split(" "))
stk = [i for i in range(1,N+1)]
answer = []
num = K-1
for i in range(N):
    if len(stk) > num:
        answer.append(stk.pop(num))
        num += K-1
    elif len(stk) <= num:
        num = num % len(stk)
        answer.append(stk.pop(num))
        num += K-1

print("<",", ".join(str(i) for i in answer),">",sep='')
