import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def dfs(graph, start, visited, group):
    visited[start] = group

    for v in graph[start]:
        if visited[v] == 0:  # 아직 방문하지 않은 노드
            result = dfs(graph, v, visited, -group)
            if not result:
                return False
        else:
            if visited[v] == group:  # 방문한 곳 중에서 현재 그룹과 같을 때
                return False
    return True


t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if visited[i] == 0:
            result = dfs(graph, i, visited, 1)
            if not result:
                break

    if result:
        print("YES")
    else:
        print("NO")
