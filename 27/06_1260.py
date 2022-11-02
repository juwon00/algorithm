import sys
sys.setrecursionlimit(10000)

from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)] # 그래프 초기화
visited_dfs=[False]*(n+1) # 방문한 컴퓨터인지 표시
visited_bfs=[False]*(n+1) # 방문한 컴퓨터인지 표시

for _ in range(m): # 그래프 생성
    a,b=map(int,input().split())
    graph[a].append(b) # a에 b 연결
    graph[b].append(a) # b에 a 연결 -> 양방향
    
for j in range(n + 1):
    graph[j].sort()


def dfs(graph, v, visited_dfs):
    visited_dfs[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)


def bfs(graph, start, visited_bfs):
    queue = deque()
    queue.append(start)
    visited_bfs[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True
                
            
dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)