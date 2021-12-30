names = input()
name = names.split('-')
short_name = ''
for _ in name:
    short_name += _[0]
print(short_name)