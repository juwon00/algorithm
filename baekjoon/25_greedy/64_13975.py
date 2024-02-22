import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    file = list(map(int, input().split()))

    heapq.heapify(file)

    result = 0

    while len(file) > 1:
        c1 = heapq.heappop(file)
        c2 = heapq.heappop(file)
        c = c1 + c2
        result += c
        heapq.heappush(file, c)

    print(result)
