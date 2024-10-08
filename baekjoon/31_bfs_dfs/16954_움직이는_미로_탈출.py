def bfs():
    for g in graph:
        print(g)

    while True:
        Okjae = []
        hashs = []
        for i in range(8):
            for j in range(8):
                if graph[i][j] == 'O':
                    Okjae.append((i, j))
                elif graph[i][j] == '#':
                    hashs.append((i, j))
        print(Okjae)
        print(hashs)
        if len(Okjae) == 0:
            return False

        for x, y in Okjae:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 8 and 0 <= ny < 8 and graph[nx][ny] == '.':
                    graph[nx][ny] = 'O'
                    if nx == 0 and ny == 7:
                        return True

        hashs.sort(reverse=True)  # 벽이 세로로 2개 있을때를 처음에 생각하지 못함 -> 아래쪽 벽부터 이동해서 해결
        for x, y in hashs:
            print(x, y)
            if x < 7:
                graph[x + 1][y] = '#'
                graph[x][y] = '.'
            else:
                graph[x][y] = '.'
            for g in graph:
                print(g)

        for g in graph:
            print(g)
        print()


graph = [list(input()) for _ in range(8)]
graph[7][0] = 'O'

if bfs():
    print(1)
else:
    print(0)
