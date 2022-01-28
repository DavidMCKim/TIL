def unit_convert(data):
    if data.split()[1] == 'kg':
        return print('%.4f %s' %(float(data.split()[0]) * 2.2046, 'lb'))

    elif data.split()[1] == 'lb':
        return print('%.4f %s' % (float(data.split()[0]) * 0.4536, 'kg'))

    elif data.split()[1] == 'l':
        return print('%.4f %s' % (float(data.split()[0]) * 0.2642, 'g'))

    elif data.split()[1] == 'g':
        return print('%.4f %s' % (float(data.split()[0]) * 3.7854, 'l'))

T = int(input())
for i in range(T):
    data = input()
    unit_convert(data)
