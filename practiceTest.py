def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count1 = 0;
    count2 = 0;
    count3 = 0
    for idx in range(len(answers)):
        if answers[idx] == first[idx % 5]:
            count1 += 1
        if answers[idx] == second[idx % 8]:
            count2 += 1
        if answers[idx] == third[idx % 10]:
            count3 += 1

    tot = [count1, count2, count3]
    for i, s in enumerate(tot):
        if s == max(tot):
            answer.append(i + 1)

    return answer