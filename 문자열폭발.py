string = input()
bomb = input()
answer = []
bomb = [x for x in bomb]

for i in range(len(string)):
    answer.append(string[i])
    #폭탄 길이보다 길거나 같을 때 마지막 문자가 같은지 확인
    if string[i] == bomb[-1] and len(answer) >= len(bomb):
        if answer[-len(bomb):] == bomb:
            for i in range(len(bomb)):
                answer.pop() #bomb과 같다면 스택에서 제거


if len(answer) == 0:
    print("FRULA")
else:
    print("".join(answer))