def koong(n):
    fibonacchi_fake = [1,1,2,4]
    for i in range(4,n+1):
        fibonacchi_fake.append(fibonacchi_fake[i-1]+fibonacchi_fake[i-2]+fibonacchi_fake[i-3]+fibonacchi_fake[i-4])
    return fibonacchi_fake[n]
t = int(input())
for i in range(t):
    n = int(input())
    print(koong(n))