len = int(input())
stk = []
answer = []
cnt = 1
flag = True
for i in range(len):
    num = int(input())
    while cnt <= num:
        stk.append(cnt)
        answer.append('+')
        cnt += 1
    if stk[-1] == num:
        stk.pop()
        answer.append('-')
    else:
        flag = False
if flag == False:
    print('NO')
else:
    for i in answer:
        print(i)
