# ## 15:53 ~ 16:35
#
# def solution(name):
#     answer = 0
#     min_move = len(name) - 1
#     next = 0
#
#     while name[min_move] == 'A' and min_move > 0:
#         min_move -= 1
#
#     if (min_move < 0):
#         return answer
#
#     for i, char in enumerate(name):
#         answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
#
#         next = i + 1
#         while next < len(name) and name[next] == 'A':
#             next += 1
#
#         min_move = min(min_move, i + (i + len(name)) - next)
#     answer += min_move
#     return answer



# files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
# def solutions(files):
#     answer = []
#     for f in files:
#         HEAD, NUMBER, TAIL = '', '', ''
#         flag = 0
#         for i in range(len(f)):
#             if f[i].isdigit():
#                 NUMBER += f[i]
#                 flag = 1
#             elif not flag:
#                 HEAD += f[i]
#             else:
#                 TAIL = f[i:]
#                 break
#         answer.append((HEAD,NUMBER,TAIL))
#
#     answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
#     return [''.join(file) for file in answer]

