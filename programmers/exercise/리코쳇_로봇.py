from collections import deque


def find(x, y, nx, ny, dx, dy, board):
    print(">>", x, y, nx, ny)
    if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
        if nx - dx != x or ny - dy != y:
            return nx - dx, ny - dy
    elif board[nx][ny] == "D":
        if nx - dx != x or ny - dy != y:
            return nx - dx, ny - dy

    return find(x, y, nx + dx, ny + dy, dx, dy, board)


def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0

    for i in range(n):
        print(board[i])
        for j in range(m):
            if board[i][j] == "R":
                start_x, start_y = i, j
            elif board[i][j] == "G":
                end_x, end_y = i, j
    print(start_x, start_y, end_x, end_y)
    print()

    q = deque()
    q.append((start_x, start_y, 0))
    visited = [[False] * m for _ in range(n)]
    visited[start_x][start_y] = True

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y, dist = q.popleft()
        visited[x][y] = True
        print(x, y, dist)

        if x == end_x and y == end_y:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and (board[nx][ny] == "." or board[nx][ny] == "G"):
                fx, fy = find(x, y, nx, ny, dx[i], dy[i], board)
                if not visited[fx][fy]:
                    print(fx, fy)
                    q.append((fx, fy, dist + 1))
        print()

    return -1


# board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
board = ["..R", "...", "...", "..D", "DG."]
answer = solution(board)
print("answer:", answer)
