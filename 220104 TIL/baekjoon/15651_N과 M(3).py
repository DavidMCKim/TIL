def suyeol(depth,N,M):
    global out

    if depth == M:
        print(' '.join(map(str, out)))
        return

    for i in range(1,N+1):
        out.append(i)
        suyeol(depth+1,N, M)
        out.pop()



N,M = map(int,input().split(' '))
out = []
suyeol(0,N,M)
