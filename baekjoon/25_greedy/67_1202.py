# 무게가 a인 가방 -> a 이하인 보석 heap에 다 넣기 -> 그중 제일 큰거 하나 선택 (pop)
# 무게가 b인 가방 -> b 이하인 보석 heap에 다 넣기 -> 그중 제일 큰거 하나 선택 (pop)
# (a < b) 이면 가능

import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
jewel = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(jewel, (a, b))
bags = []
for _ in range(k):
    bags.append(int(input()))
bags.sort()

print(jewel)
print(bags)

result = 0
tmp = []
for bag in bags:
    print(bag)
    while jewel and jewel[0][0] <= bag:
        heapq.heappush(tmp, -heapq.heappop(jewel)[1])
        print(jewel)
    if tmp:
        result -= heapq.heappop(tmp)

print(result)
