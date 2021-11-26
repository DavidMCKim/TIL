# 03_set연산.py

A = {1, 2, 3}
B = {3, 4, 5, 6}
# 합집합
# a | b
print(A|B)
# a.union(b)
print(A.union(B))

# 교집합 - 반환결과 집합
# a & b
print(A&B)
# a.intersection(b)
print(A.intersection(B))

# 차집합
# a - b
print(A-B)
# a.difference(b)
print(A.difference(B))