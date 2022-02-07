## ver.함수로 구현(재귀함수) -> 동작을 함수로 짜놓으면 시간이 조금 단축될까 싶어 함수로 구현해보았습니다.
#### 틀린이유 : 0이 입력으로 들어오면 출력하지 않고 프로그램이 종료되어야 하는데 0이 입력으로 들어오면 0을 출력하고 프로그램을 종료하도록 되어있어서 틀렸음
# def multi_self(data):
#     global num
#     if len(data) == 1:
#         print(data)
#     else:
#         print(int(data), end=' ')
#         for i in data:
#             num *= int(i)
#             data = str(num)
#         if len(str(num)) == 1:
#             print(num)
#             num = 1
#     while len(str(num)) != 1:
#         num = 1
#         multi_self(data)
#
# num = 1
# S = '1'
# while S != '0':
#     S = input()
##### 밑의 두 줄을 넣지 않아서 틀렸..
#     if S=='0':
#         break
#     else:
#         multi_self(S)

################################################################################################
## ver.단순구현
# while True:
#     s = input()
#     if s == '0':
#         break
#     if len(s) == 1:
#         print(s)
#     else:
#         while len(s) != 1:
#             print(s, end=' ')
#             num = 1
#             for i in s:
#                 num *= int(i)
#             s = str(num)
#         print(s)

################################################################################################