color_list =['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
color_value_dict = {}
color_mul_dict = {}
x = 0
y = 1
for color in color_list:
    color_value_dict[color] = x
    x += 1
    color_mul_dict[color] = y
    y *= 10

print(color_value_dict)
print(color_mul_dict)

color1 = color_value_dict[input()]
color2 = color_value_dict[input()]
color3 = color_mul_dict[input()]

value = (color1*10+color2)*color3
print(value)
