def find_sosu(x,y,z):
    sum = x + y + z
    for _ in range(2,sum):
        if sum % _ == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for x in range(0,len(nums)-2):
        for y in range(x+1,len(nums)-1):
            for z in range(y+1,len(nums)):
                if find_sosu(nums[x],nums[y],nums[z]):
                    answer += 1
    print(answer)
    return answer

nums = list(map(int,input().split(' ')))
solution(nums)
