import heapq, sys

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

result = 0
while len(heap) > 1:
    print(heap)

    x1 = heapq.heappop(heap)
    x2 = heapq.heappop(heap)
    print(x1, x2)

    x = x1 + x2
    result += x
    heapq.heappush(heap, x)
print(result)
