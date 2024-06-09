from collections import deque

n, k = map(int, input().split())
graph = deque(list(map(int, input().split())))
belt = deque([False] * n)

answer = 0
while True:
    answer += 1
    print(graph)
    print(belt)

    graph.rotate(1)
    belt.rotate(1)
    belt[n - 1] = False

    for i in range(n - 2, -1, -1):
        print(i)
        if belt[i] and graph[i + 1] > 0 and not belt[i + 1]:
            belt[i] = False
            belt[i + 1] = True
            graph[i + 1] -= 1
            if i + 1 == n - 1:
                belt[i + 1] = False

    if graph[0] > 0:
        belt[0] = True
        graph[0] -= 1

    print("zero", graph.count(0))
    if graph.count(0) >= k:
        break
    print()

print("answer", answer)
print(answer)
