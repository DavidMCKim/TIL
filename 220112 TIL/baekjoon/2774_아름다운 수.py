T = int(input())
count = 1
for _ in range(T):
    X = int(input())
    for x in range(len(str(X))-1):
        if str(X)[x] != str(X)[x+1]:
            count += 1
    print(count)