K = int(input('과자 한 개 가격 : '))
N = int(input('사려고 하는 과자의 개수 : '))
M = int(input('현재 가진 돈 : '))

change = (K * N) - M

print('부모님께 받아야 하는 모자란 돈 : ',change)