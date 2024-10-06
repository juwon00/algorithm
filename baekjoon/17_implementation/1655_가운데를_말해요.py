import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def push_num(num):
    if len(heap_max) == len(heap_min):
        heappush(heap_max, -num)
    else:
        heappush(heap_min, num)

    if heap_min and -heap_max[0] > heap_min[0]:
        tmp1 = heappop(heap_max)
        tmp2 = heappop(heap_min)
        heappush(heap_max, -tmp2)
        heappush(heap_min, -tmp1)


def find_median():
    if len(heap_max) == len(heap_min):
        return -heap_max[0], heap_min[0]
    else:
        return -heap_max[0]


heap_max = []
heap_min = []

n = int(input())

for i in range(1, n + 1):
    x = int(input())
    push_num(x)
    if i % 2 == 0:
        print(min(find_median()))
    else:
        print(find_median())
