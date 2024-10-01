from collections import deque

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
for g in graph:
    print(g)

q = deque()
print(q)

visited = [[False] * c for _ in range(r)]
for v in visited:
    print(v)

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            q.append((i, j, "J", 0))
            visited[i][j] = True

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            q.append((i, j, "F", 0))

while q:
    x, y, char, depth = q.popleft()
    print("=======================")
    print(x, y, char, depth)

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        if char == "J":
            if 0 <= nx < r and 0 <= ny < c:
                print(nx, ny)
                if graph[nx][ny] == '.' and not visited[nx][ny]:
                    print("move")
                    graph[nx][ny] = char
                    q.append((nx, ny, char, depth + 1))
            else:
                if graph[x][y] != 'F':
                    print("find")
                    print(depth + 1)
                    exit()
        elif char == "F":
            if 0 <= nx < r and 0 <= ny < c:
                print(nx, ny)
                if graph[nx][ny] == '.' or graph[nx][ny] == 'J':
                    print("fire")
                    graph[nx][ny] = char
                    q.append((nx, ny, char, depth + 1))

        for g in graph:
            print(g)
        print()
print("IMPOSSIBLE")

# 처음에 생각 못한 예시 - 42줄 (if graph[x][y] != 'F':) 추가로 해결
#4 5
#####
#J..#
#...#
#..F#
