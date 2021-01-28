def solution(clothes):
    cases = 1
    hash_dict = {}

    for l in clothes:
        if l[1] not in hash_dict.keys():
            hash_dict[l[1]] = 1
        else:
            hash_dict[l[1]] += 1

        value_list = hash_dict.values()

        for n in value_list:
            cases *= n+1                    #조합 계산
    return cases-1                          #모든 옷을 안 입는 경우 빼주기