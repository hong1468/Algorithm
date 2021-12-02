from collections import deque

n = int(input())
deque = deque()

for i in range(n):
    command = input()
    command = list(command.split())
    do = command[0]
    if do == "push_front":
        deque.appendleft(command[1])
    elif do == "push_back":
        deque.append(command[1])
    elif do == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    elif do == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif do == "size":
        print(len(deque))
    elif do =="empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif do == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif do == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
