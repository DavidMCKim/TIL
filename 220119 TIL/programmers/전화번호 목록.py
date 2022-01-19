### 왜 틀렸을까....

# 1차시도 - 정확성 : 62.5점 / 효율성 : 0점 -> 전체 : 62.5점
# def solution(phone_book):
#     answer = True
#     for _ in phone_book:
#         temp = phone_book
#         temp.remove(_)
#         for phone_num in temp:
#             if _ in phone_num[:len(_)]:
#                 answer = False
#     return answer

# 2차시도 - 정확성 : 66.7점 +효율성 : 0점 -> 전체 : 66.7점
# def solution(phone_book):
#     answer = True
#     i = 0
#     while answer == True:
#         i += 1
#         if answer == False:
#             break
#         if i > len(phone_book):
#             break
#         else:
#             for _ in phone_book:
#                 temp = phone_book
#                 temp.remove(_)
#                 for phone_num in temp:
#                     if len(_) <= len(phone_num):
#                         if _ in phone_num[:len(_)]:
#                             answer = False
#     return answer

# 3차시도 - 정확성 : 83.3 / 효율성 : 0점 -> 전체 : 83.3점
# def solution(phone_book):
#     answer = True
#     for _ in phone_book:
#         tmp = ""
#         for num in _:
#             tmp += num
#             if tmp in phone_book and tmp!=_:
#                 answer = False
#     return answer

# 4차시도 - 정확성 : 83.3 / 효율성 : 0점 -> 전체 : 83.3점
# def solution(phone_book):
#     answer = True
#     dict = {}
#     for _ in phone_book:
#         dict[_] = 1
#         tmp = ""
#         for num in _:
#             tmp += num
#             if tmp in phone_book and tmp!=_:
#                 answer = False
#     return answer

# 5차시도 - 정확성: 70.8 + 효율성: 16.7 -> 전체: 87.5점
def solution(phone_book):
    answer = True
    dict = {}
    for _ in phone_book:
        dict[_] = 1
        tmp = ""
        for num in _:
            tmp += num
            if tmp in dict and tmp != _:
                answer = False
    return answer


# 6차시도 - 정확성: 83.3 + 효율성: 16.7 -> 전체 : 100점
def solution(phone_book):
    answer = True
    dict = {}

    for _ in phone_book:
        dict[_] = 1

    for _ in phone_book:
        tmp = ""
        for num in _:
            tmp += num
            if tmp in dict and tmp != _:
                answer = False
    return answer