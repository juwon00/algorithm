from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(place):
    for pl in place:
        print(pl)

    for i in range(5):
        # print(place[i])
        for j in range(5):
            # print(place[i][j])
            if place[i][j] == "P":
                print("find", i, j)
                q = deque()
                q.append((i, j, 0))
                visited = [[False] * 5 for _ in range(5)]
                visited[i][j] = True
                # print(visited)

                while q:
                    x, y, cost = q.popleft()

                    print("x, y, cost", x, y, cost)

                    if cost == 2:
                        continue

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                            continue

                        if place[nx][ny] == "P" and not visited[nx][ny]:
                            print("return 0")
                            return 0

                        if place[nx][ny] == "O" and not visited[nx][ny]:
                            print(nx, ny)
                            q.append((nx, ny, cost + 1))
                            visited[nx][ny] = True

    return 1


def solution(places):
    answer = []

    for place in places:
        print(place)
        result = bfs(place)
        answer.append(result)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
answer = solution(places)
print("answer", answer)
