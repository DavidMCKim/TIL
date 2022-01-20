# clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

## 1차시도 - 정확성 28.6점
# clothes_dict = {}
# for _ in clothes:
#     if _[1] in clothes_dict:
#         clothes_dict[_[1]] += 1
#     else:
#         clothes_dict[_[1]] = 1
# print(clothes_dict)
# count = 1
# for i in clothes_dict.values():
#     if len(clothes_dict.keys()) == 1:
#         answer = len(clothes)
#     else:
#         count *= i
#         answer = count + len(clothes)
# print(answer)

## 2차시도 - 정확성 : 100점
clothes_dict = {}
for _ in clothes:
    if _[1] in clothes_dict:
        clothes_dict[_[1]] += 1
    else:
        clothes_dict[_[1]] = 1
print(clothes_dict)
count = 1
for i in clothes_dict.values():
    count *= (i+1)
answer = count-1
print(answer)