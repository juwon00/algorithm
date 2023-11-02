# 양 끝의 문자가 다르면 -> 팰린드롬 아님
# 양 끝의 문자가 같을 때, 가운데 문자열이
#   - 팰린드롬이라면 -> 팰린드롬
#   - 팰린드롬이 아니라면 -> 팰린드롬 아님
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for a in range(n):
        print(dp[a])
    for start in range(n - i):

        end = start + i
        print(start, end, "===", num[start], num[end])

        if start == end:
            print(1)
            dp[start][end] = 1

        # 시작점의 글자와 끝점의 글자가 같다면
        elif num[start] == num[end]:
            print(2)
            # 두 글자짜리 문자열이라면 무조건 팰린드롬
            if start + 1 == end:
                print(3)
                dp[start][end] = 1
            # 가운데 문자열이 팰린드롬이라면 팰린드롬
            elif dp[start + 1][end - 1] == 1:
                print(4)
                dp[start][end] = 1

    print()

for a in range(n):
    print(dp[a])

# 정답출력하기
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
