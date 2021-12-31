# b-a가 가장 큰 값을 출력

def find_sosu(num):
    yaksu_list = []
    sosu_list = []
    for _ in range(2,num+1):
        for x in range(1,_+1):
            if _%x == 0:
                yaksu_list.append(x)
        if len(yaksu_list) <= 2:
            if _%2 != 0:
                sosu_list.append(_)
        yaksu_list = []
    return sosu_list


while True:
    n = int(input())
    if n == 0:
        break
    else:
        sosu_list = find_sosu(n)
        print(sosu_list)
        start = 0
        end = -1
        sosu_sum = ''
        diff = []
        temp = []
        for x in sosu_list:
            for y in sosu_list[1:]:
                if x+y == n:
                    temp.append([x,y])
        if len(temp) >= 2:
            print(f'{n} = {temp[0][0]} + {temp[0][1]}')
        else:
            print("Goldbach's conjecture is wrong.")
        # if len(temp) >= 2:
        #     for _ in temp:
        #         diff.append(temp[1] - temp[2])
        #     print()
        # elif len(temp) == 0:
        #     print("Goldbach's conjecture is wrong.")




        # if len(sosu) != 1:
        #     print(f'{n} = {sosu}')
        # else:
        #     print("Goldbach's conjecture is wrong.")











# def find_yaksu(num):
#     yaksu_list = []
#     for _ in range(1,num):
#         if num % _ == 0 :
#             yaksu_list.append(_)
#     return yaksu_list

# def find_sosu(yaksu_list):
#     sosu_list = []
#     for yaksu in yaksu_list:
#         for x in range(1, yaksu):
#             if yaksu % x == 0:
#                 sosu_list.append(x)
#     return sosu_list