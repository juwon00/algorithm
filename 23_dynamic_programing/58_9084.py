t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m + 1)
    dp[0] = 1

    print(dp)
    print(coins)

    for coin in coins:
        for i in range(1, m + 1):
            print(coin, i)
            if i >= coin:
                print(dp[i - coin])
                dp[i] += dp[i - coin]
                print(dp)
        print(dp)
    print(dp[-1])
