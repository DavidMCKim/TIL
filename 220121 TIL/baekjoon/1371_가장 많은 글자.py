import sys

high_alpha = {}
alpha_list = []
# text = [input() for i in range(2)]
first_line = ['0']*50
text = sys.stdin.read().replace('\n','')
print(text)

# print(text)
# for alpha in text:
#     if alpha != ' ':
#         if alpha in high_alpha.keys():
#             high_alpha[alpha] += 1
#         else:
#             high_alpha[alpha] = 1
#
# for _ in high_alpha.keys():
#     if high_alpha[_] == max(high_alpha.values()):
#         alpha_list.append(_)
# alpha_list.sort()
# for _ in alpha_list:
#     print(_,end='')