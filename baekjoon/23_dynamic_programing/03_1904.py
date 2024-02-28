n = int(input())
if n == 1:  # 인덱스 에러 방지
    print(1)
    exit()
graph = [0] * (n + 1)
graph[1] = 1
graph[2] = 2

for i in range(3, n + 1):
    graph[i] = (graph[i - 1] + graph[i - 2]) % 15746  # 메모리 초과 방지
print(graph)
print(graph[n])
