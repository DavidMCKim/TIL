for _ in range(3):
    n = input()
    count, max_value = 1, 1

    for i in range(len(n)):
        if int(n[i]) == int(n[i - 1]):
            count += 1
            if count > max_value:
                max_value = count
        else:
            count = 1
