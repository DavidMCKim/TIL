# 06_split_ex.py

# 그림과 같이 입력 받고 split()을 사용하여 분리

# 생일 입력 (연/월/일) : 1997/10/15
# 당신은 1997년에 태어났고
# 생일은 10월 15일 이군요

birth = input('생일 입력 (연/월/일) : ')
print(birth)

year = birth.split('/')[0]
month = birth.split('/')[1]
day = birth.split('/')[2]
print('당신은 %s년에 태어났고\n생일은 %s월 %s일 이군요' %(year, month, day))


