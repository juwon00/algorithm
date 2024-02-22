import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [i for i in range(n + 1)]
print(parent)

for i in range(n - 2):
    a, b = map(int, input().split())
    print(a, b)
    union_parent(parent, a, b)
    print(parent)

# 처음에는 코드를 아래와 같이 작성했지만 시간초과가 생겼다.
# 이중 for문을 쓰는거와 같은 느낌?
# result = []
# for i in range(1, n+1):
#     if parent[i] not in result:
#         result.append(i)

result = []
for i in range(1, n + 1):
    if i == parent[i]:
        result.append(i)
print(*result)
