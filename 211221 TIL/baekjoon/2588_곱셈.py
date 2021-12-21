A = int(input())
B = int(input())

for _ in range(len(str(B))-1,-1,-1):
    print(A*int((str(B)[_])))
print(A*B)