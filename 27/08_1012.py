import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 2
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


T = int(input())

for _ in range(T):
    
    M, N, K = map(int, input().split())
    
    graph = [[0]*M for _ in range(N)];

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    # print(graph)
    
    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                result+= 1
    # print(graph)
    print(result)
    