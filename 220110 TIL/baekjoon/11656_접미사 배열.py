S = input()
index = 0
dict = []
for i in range(len(S)):
    dict.append(S[index:])
    index += 1

dict.sort()
for word in dict:
    print(word)