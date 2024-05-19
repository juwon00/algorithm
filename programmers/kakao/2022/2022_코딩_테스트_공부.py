# 다시 풀어볼 문제

def solution(alp, cop, problems):
    INF = int(1e9)
    max_alp, max_cop = [0, 0]

    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
    print(max_alp, max_cop)

    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    print(alp, cop)
    dp[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            print(i, j)
            if i < max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i + alp_rwd, max_alp)
                    new_cop = min(j + cop_rwd, max_cop)
                    print("new", alp_req, cop_req, alp_rwd, cop_rwd, cost)
                    print(new_alp, new_cop)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)

            for d in dp:
                print(d)
            print()

    for d in dp:
        print(d)
    return dp[max_alp][max_cop]


alp = 0
cop = 0
problems = [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]
answer = solution(alp, cop, problems)
print("answer:", answer)
