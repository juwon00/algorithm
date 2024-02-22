import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
answer = sys.maxsize

one = 0

if arr[left] == 1:
    one += 1

while left < len(arr) and right < len(arr):
    if one < k:
        right += 1
        if right < len(arr) and arr[right] == 1:
            one += 1
    else:
        if one == k:
            answer = min(answer, right - left + 1)

        if left < len(arr) and arr[left] == 1:
            one -= 1
        left += 1

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
