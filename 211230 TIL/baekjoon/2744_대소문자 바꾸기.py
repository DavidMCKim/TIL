word = input()
new_word = ''
for _ in word:
    if _.islower():
        new_word += _.upper()
    elif _.isupper():
        new_word += _.lower()
print(new_word)