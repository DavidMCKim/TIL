N = int(input())
score = list(map(int,input().split(' ')))

new_score = []
for _ in score:
    new_score.append(_/max(score)*100)

mean = sum(new_score)/N
print(mean)