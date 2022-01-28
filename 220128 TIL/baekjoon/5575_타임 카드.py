for i in range(3):
    employee = list(map(int,input().split()))
    sec = employee[5] - employee[2]
    min = employee[4] - employee[1]
    hour = employee[3] - employee[0]

    if sec < 0:
        min -= 1
        sec += 60
    if min < 0 :
        hour -= 1
        min += 60
    if hour < 0:
        hour += 23

    print(hour, min, sec)
