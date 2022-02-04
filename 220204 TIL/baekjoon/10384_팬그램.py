n = int(input())
for i in range(n):
    pangram = ''.join(alpha for alpha in list(input().lower()) if alpha.isalnum() and alpha.isalpha())
    alpha_list = [0 for i in range(26)]

    for word in pangram:
        alpha_list[ord(word) - 97] += 1
    min_value = min(alpha_list)

    if min_value == 0:
        word = 'Not a pangram'
    elif min_value == 1:
        word = 'Pangram!'
    elif min_value == 2:
        word = 'Double pangram!!'
    elif min_value >=3:
        word = 'Triple pangram!!!'

    print(f'Case {i+1}: {word}')
