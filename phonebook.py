def solution(phone_book):
    answer = True
    phone_book.sort()

    for num1, num2 in zip(phone_book[:-1], phone_book[1:]):
        if num1 in num2:
            answer = False
    return answer

if __name__ == '__main__':
    phone_book = ["12", "123", "1235", "567", "88"]
    print(solution(phone_book))