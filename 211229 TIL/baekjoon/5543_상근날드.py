sangduck = int(input())
jungduck = int(input())
haduck = int(input())
coke = int(input())
cider = int(input())

burger = [sangduck, jungduck, haduck]
drink = [coke,cider]

set = []
for x in burger:
    for y in drink:
        set.append(x+y-50)
print(min(set))