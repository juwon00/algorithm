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


g = int(input())
p = int(input())

parent = [0] * (g + 1)
for i in range(1, g + 1):
    parent[i] = i
print(parent)

# x번 게이트로 들어오면 그곳에 정차시키고 이후에는 x-1번 게이트로 가게끔
# 계속해서 -1을 하면서 게이트를 찾다가 0이 나오면 정차시킬 수 없으므로 종료

result = 0
for i in range(p):
    gi = int(input())
    print("gi:", gi)
    gi_p = find_parent(parent, gi)
    print(gi_p, gi_p - 1)
    if gi_p == 0:
        break
    union_parent(parent, gi_p, gi_p - 1)
    print(parent)
    print()
    result += 1

print(result)
