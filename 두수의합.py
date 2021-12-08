num = int(input())
lst = input()
lst = sorted(list(map(int,lst.split(" "))))

result = int(input())
answer = 0
left = 0
right = num-1
while left < right:
    tmp = lst[left] + lst[right]
    if tmp == result:
        answer += 1
        left += 1
    elif tmp < result:
        left += 1
    else:
        right -= 1
print(answer)