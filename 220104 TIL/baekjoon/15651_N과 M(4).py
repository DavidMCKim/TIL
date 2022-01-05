def dfs(start):
    global out
    if len(out) == m:
        print(' '.join(map(str, out)))
        return

    for i in range(start, n + 1):
        out.append(i)
        dfs(i)
        out.pop()

n, m = map(int, input().split())
out = []
dfs(1)