test = int(input())
for _ in range(test):
    candy, children = map(int,input().split(' '))
    per = int(candy/children)
    dad = candy%children
    print(f'You get {per} piece(s) and your dad gets {dad} piece(s).')