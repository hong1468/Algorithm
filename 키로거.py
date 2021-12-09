n = int(input())
for i in range(n):
    tc = list(input())
    left = []
    right = []
    for j in range(len(tc)):
        if tc[j] == '-':
            if left:
                left.pop()
        elif tc[j] == '<':
            if left:
                right.append(left.pop())
        elif tc[j] == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(tc[j])
    left.extend(reversed(right))
    print(''.join(left))