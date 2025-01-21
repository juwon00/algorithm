for _ in range(int(input())):
    n = int(input())
    dp = [[0, 0] + list(map(int, input().split())) for _ in range(2)]
    print(dp)

    for i in range(2, n + 2):
        dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
    print(dp)
    print(max(dp[0][-1], dp[1][-1]))
