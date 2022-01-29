# T = int(input())
# for i in range(T):
#     count = int(input())
#     dict = {}
#
#     for num in range(count):
#         dict[int(input())] = num+1
#     print(dict.keys())
#     print(sum(dict.keys())/2)
#     print(max(dict.keys()))
#
#     if max(dict.keys()) == sum(dict.keys())/len(dict.keys()):
#         print('no winner')
#     elif max(dict.keys()) > sum(dict.keys())/2:
#         print('majority winner %s' %dict[max(dict.keys())])
#     elif max(dict.keys()) <= sum(dict.keys())/2:
#         print('minority winner %s' %dict[max(dict.keys())])



T = int(input())
for i in range(T):
    count = int(input())
    dict = {}
    vote_cnt_list = []
    for num in range(count):
        cnt = int(input())
        vote_cnt_list.append(cnt)

    max_vote = max(vote_cnt_list)
    avg_vote = sum(vote_cnt_list)/len(vote_cnt_list)
    half_vote = sum(vote_cnt_list)/ 2

    if vote_cnt_list.count(max_vote) >= 2:
        print('no winner')
    else:
        if max_vote > half_vote:
            print('majority winner %d' %(vote_cnt_list.index(max_vote)+1) )
        if max_vote <= half_vote:
            print('minority winner %d' %(vote_cnt_list.index(max_vote)+1) )