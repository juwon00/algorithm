# 메모리 초과 오류 생각할 문제

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
print(arr)

max_dp = [0] * 3
min_dp = [0] * 3
max_dp[0], max_dp[1], max_dp[2] = arr[0], arr[1], arr[2]
min_dp[0], min_dp[1], min_dp[2] = arr[0], arr[1], arr[2]

print(max_dp, min_dp)

for i in range(1, n):
    print(i)
    arr = list(map(int, input().split()))
    a_min = min(min_dp[0], min_dp[1])
    b_min = min(min_dp)
    c_min = min(min_dp[1], min_dp[2])
    min_dp[0] = arr[0] + a_min
    min_dp[1] = arr[1] + b_min
    min_dp[2] = arr[2] + c_min

    a_max = max(max_dp[0], max_dp[1])
    b_max = max(max_dp)
    c_max = max(max_dp[1], max_dp[2])
    max_dp[0] = arr[0] + a_max
    max_dp[1] = arr[1] + b_max
    max_dp[2] = arr[2] + c_max

print(max_dp, min_dp)
print(max(max_dp), min(min_dp))
