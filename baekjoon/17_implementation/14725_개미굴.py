n = int(input())
graph = []
for _ in range(n):
    tmp = list(input().split())
    graph.append(tmp[1:])
graph.sort()

dash = "--"
answer = []
for i in range(n):
    print(graph[i])
    if i == 0:
        for j in range(len(graph[i])):
            answer.append(dash * j + graph[i][j])
    else:
        idx = 0
        for j in range(len(graph[i])):
            # 이전 리스트와 현재 리스트가 겹치지 않거나, 이전 리스트의 원소가 없을 때
            if graph[i - 1][j] != graph[i][j] or len(graph[i - 1]) <= j:
                break
            # 겹치는 원소가 존재한다면 해당 원소를 출력할 필요가 없으므로 idx를 조정
            else:
                idx = j + 1
        for j in range(idx, len(graph[i])):
            answer.append(dash * j + graph[i][j])


print(answer)
for ans in answer:
    print(ans)
