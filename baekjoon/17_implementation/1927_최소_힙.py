import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) > 0:
            print("here")
            print(heappop(heap))
        else:
            print("here")
            print(0)
    else:
        heappush(heap, x)
    print(heap)
    print()
