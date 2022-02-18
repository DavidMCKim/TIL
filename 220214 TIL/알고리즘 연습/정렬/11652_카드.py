N = int(input())
cnt = 1
mxval = -2**62-1
mxcnt = 0

num = [int(input()) for i in range(N)]
num.sort()
print(num)
# for i,n in enumerate(num):
    # if