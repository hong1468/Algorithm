n = 9
n1, n2 = 0, 0
arr = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            n1 = arr[i]
            n2 = arr[j]

arr.remove(n1)
arr.remove(n2)

print('\n'.join(map(str, sorted(arr))))