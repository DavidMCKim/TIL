# 05_while_coutinue.py

# continue 문
# 반복문 수행 중에 continue 문을 만나면
# 현재 시점에서 중단하고(다음 문장을 수행하지 않음)
# 다음 반복 계속 수행

x = 0
while x< 10 :
    x += 1
    if x % 2 == 0 :
        continue
        # break
    print(x)