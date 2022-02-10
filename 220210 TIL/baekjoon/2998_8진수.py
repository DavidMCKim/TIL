quad_dict = {'000':'0','001':'1','010':'2','011':'3','100':'4','101':'5','110':'6','111':'7'}
three = ''
n = ''
num = input()
while len(num)%3!=0:
    if len(num)%3 == 0:
        break
    else:
        num = '0'+num
for i in range(len(num)):
    if i%3 == 2 and i != 0:
        three += num[i]
        n += quad_dict[three]
        three = ''
    else:
        three += num[i]
print(int(n))