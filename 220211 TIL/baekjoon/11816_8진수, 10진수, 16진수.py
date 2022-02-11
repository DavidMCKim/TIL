dict_8 = {}
dict_16 = {}
list_8 = ['0','1','2','3','4','5','6','7','8']
list_16 = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
for i in list_8:
    dict_8[i] = int(i)
for i,n in enumerate(list_16):
    dict_16[n] = i

X = input()
answer = 0
if X[:2] == '0x':
    for i,n in enumerate(X[:1:-1]):
        answer += dict_16[n]*(16**i)
elif X[:1] == '0':
    for i,n in enumerate(X[:0:-1]):
        answer += dict_8[n]*(8**i)
else:
    answer += int(X)
print(answer)