from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    graph = [[0 for _ in range(102)] for _ in range(102)]

    for i in range(len(rectangle)):
        x1, y1, x2, y2 = rectangle[i][0] * 2, rectangle[i][1] * 2, rectangle[i][2] * 2, rectangle[i][3] * 2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                graph[x][y] = 1

    remove1 = []
    for x in range(1, len(graph) - 1):
        for y in range(1, len(graph) - 1):
            if graph[x][y] == 1 and graph[x - 1][y] == 1 and graph[x + 1][y] == 1 and graph[x][y - 1] == 1 and graph[x][
                y + 1] == 1 and graph[x - 1][y - 1] == 1 and graph[x - 1][y + 1] == 1 and graph[x + 1][y - 1] == 1 and \
                    graph[x + 1][y + 1] == 1:
                remove1.append((x, y))
    for i in range(len(remove1)):
        graph[remove1[i][0]][remove1[i][1]] = 0

    characterX, characterY, itemX, itemY = characterX * 2, characterY * 2, itemX * 2, itemY * 2
    visited = [[False for _ in range(102)] for _ in range(102)]
    q = deque()
    q.append((characterX, characterY))

    while q:
        x, y = q.popleft()
        print(x, y)
        print()

        if x == itemX and y == itemY:
            answer = graph[x][y] // 2
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    print(answer)

    return answer


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

rectangle = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8
solution(rectangle, characterX, characterY, itemX, itemY)
