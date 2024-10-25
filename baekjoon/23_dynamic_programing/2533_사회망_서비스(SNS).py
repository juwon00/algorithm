# 다시 풀어볼 문제
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node):
    print("node", node)
    for next in graph[node]:
        if not visited[next]:
            visited[next] = True
            dfs(next)
            print(next)
            for d in dp:
                print(d)
            print()
            dp[node][0] += dp[next][1]
            dp[node][1] += min(dp[next])
            for d in dp:
                print(d)
            print()


dp = [[0, 1] for _ in range(n + 1)]
visited = [False] * (n + 1)
visited[1] = True
dfs(1)
for d in dp:
    print(d)
print(min(dp[1]))

# 처음 제출한 코드 - 왜 틀렸을까?
# from collections import deque
#
# n = int(input())
# graph = [[] for _ in range(n + 1)]
# indegree = [0] * (n + 1)
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#     indegree[a] += 1
#     indegree[b] += 1
# print(graph)
# print(indegree)
#
# sorted_indegree = sorted(range(len(indegree)), key=lambda x: (indegree[x], x), reverse=True)
# q = deque(sorted_indegree)
# print(q)
#
# cnt = 0
# while q:
#     now = q.popleft()
#     print("now:", now)
#     if graph[now]:
#         for node in graph[now]:
#             print(node)
#             graph[node].remove(now)
#     else:
#         break
#     graph[now] = []
#     print(graph)
#     print()
#     cnt += 1
# print(graph)
# print(cnt)


# 이런 느낌으로 했어야 됐나봄
# 리프노드부터 찾기
# 나는 indegree가 가장 높은거 부터 찾기 - 실패
#
# leaf_nodes = []
# for i, nodes in enumerate(adj_list):
#   if len(nodes) == 1:
#     leaf_nodes.append(i)
#
# answer = 0
#
# # 리프노드가 없으면 끝
# while leaf_nodes:
#   leaf_node = leaf_nodes.pop()
#   # 부모노드가 존재하면
#   if adj_list[leaf_node]:
#     parent_node = adj_list[leaf_node][0]
#     # 부모노드와 다른 노드와의 연결 삭제
#     for node in adj_list[parent_node]:
#       adj_list[node].remove(parent_node)
#       # 부모노드와 인접한 다른 노드와 연결된 노드가 1개면 리프노드에 추가
#       if len(adj_list[node]) == 1:
#         leaf_nodes.append(node)
#       # 리프노드와 부모노드 제거
#       adj_list[parent_node] = []
#     answer += 1
#     adj_list[leaf_node] = []
#
# print(answer)
