# A 10
# B 01
# BA 11
# BAB 12
# BABBA 23
# BABBABAB 35
# BABBABABBABBA 5 8
#
#
# 1 0 1 1 2 3 5
# 0 1 1 2 3 5 8
A,B = [1],[0]
K = int(input())
for i in range(1,K+1):
    if i == 1:
        A.append(0)
        B.append(1)
    else:
        A.append(A[-1]+A[-2])
        B.append(B[-1]+B[-2])
print(A[-1],B[-1])