import heapq
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()
print(arr)

room = []
heapq.heappush(room, arr[0][1])
print(room)

for i in range(1, n):
    print(arr[i])
    if arr[i][0] >= room[0]:
        print("pop")
        heapq.heappop(room)
    heapq.heappush(room, arr[i][1])
    print("room", room)
print(len(room))

# 8
# 1 8
# 9 16
# 3 7
# 8 10
# 10 14
# 5 6
# 6 11
# 11 12
