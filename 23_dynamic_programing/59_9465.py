# 그림, case 참고 - https://beyond-common-sense.tistory.com/10

t = int(input())
for _ in range(t):
    n = int(input())
    sticker = []
    score = [0, 0]
    score.extend(list(map(int, input().split())))
    sticker.append(score)
    score2 = [0, 0]
    score2.extend(list(map(int, input().split())))
    sticker.append(score2)

    for a in range(2):
        print(sticker[a])

    dp = [[0] * (n + 2) for _ in range(2)]

    for i in range(2, n + 2):
        print(i)
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + sticker[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + sticker[1][i]
        for a in range(2):
            print(dp[a])

    print(max(dp[0][-1], dp[1][-1]))
