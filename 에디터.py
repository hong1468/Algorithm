word = list(input())
print(word)
n = int(input())
answer = []
for i in range(n):
    cmd = input().split(" ")
    if cmd[0] == 'L':
        if word:
            answer.append(word.pop())
        else:
            continue
    elif cmd[0] == 'D':
        if answer:
            word.append(answer.pop())
        else:
            continue
    elif cmd[0] == 'B':
        if word:
            word.pop()
        else:
            continue
    elif cmd[0] == 'P':
        word.append(cmd[1])
print(''.join(word+list(reversed(answer))))
