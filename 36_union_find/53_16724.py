import sys

sys.setrecursionlimit(10 ** 7)
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


n, m = map(int, input().split())

parent = [0] * m * n
maze = [[0] * m for _ in range(n)]

for i in range(n):
    x = input()
    for j in range(m):
        maze[i][j] = x[j]

for i in range(len(parent)):
    parent[i] = i

print(parent)
print()
for q in range(n):
    print(maze[q])

for i in range(n):
    for j in range(m):
        print(i, j)
        if maze[i][j] == 'D':
            union_parent(parent, m * i + j, m * (i + 1) + j)
        elif maze[i][j] == 'U':
            union_parent(parent, m * i + j, m * (i - 1) + j)
        elif maze[i][j] == 'L':
            union_parent(parent, m * i + j, m * i + j - 1)
        elif maze[i][j] == 'R':
            union_parent(parent, m * i + j, m * i + j + 1)
        print(parent)
        print()

cnt = set()
for i in range(n):
    for j in range(m):
        cnt.add(find_parent(parent, m * i + j))

print(len(cnt))

# 처음에 생각못한 반례
# 1,1 부분 (부모가 바뀌면 자식도 업데이트? 해야함)

# 3 3
# RLD
# RRU
# RRL
