def solution(phone_book):
    answer = True
    temp = phone_book[0]
    for i in phone_book:
        count = 0
        for j in range(len(phone_book)):
            if phone_book[j].startswith(i) == True:
                count += 1
            if count >= 2:
                answer = False
                break
        return answer
