n, d, k, c = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(int(input()))
graph.extend(graph)
print(graph)

result = 0
for i in range(n):
    print(i, i + k)
    print(graph[i:i + k])
    tmp = graph[i:i + k]
    tmp.append(c)
    tmp = set(tmp)
    result = max(result, len(tmp))
print(result)
