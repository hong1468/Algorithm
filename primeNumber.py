import itertools

def check(num):                                 #소수 찾기
    sosoo = False
    count = 0
    if num > 1:
        for i in range(2, int(num / 2) + 1):    #나누어 떨어지면 break
            if num % i == 0:
                count += 1
                break
    if num > 1 and count == 0:
        print(num)
        sosoo = True
    return sosoo                                 #소수인지 아닌지 bool 값으로 return


def solution(numbers):
    answer = 0
    num_list = []
    for i in range(len(numbers)):
        num_list.append(numbers[i])
    permuted = []

    for j in range(1, len(num_list) + 1):
        permute = list(map(''.join, itertools.permutations(num_list, j)))
        print(permute)
        permuted += permute
    permuted = list(set(map(lambda x: int(x), permuted)))                    #string -> int & unique 값

    for x in permuted:
        if check(x) == True:
            answer += 1

    return answer