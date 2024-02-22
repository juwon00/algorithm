# 플로이드 워셜 알고리즘을 사용한 풀이

def solution(n, results):
    answer = 0
    board = [[0] * n for _ in range(n)]
    print(board)

    for a, b in results:
        board[a - 1][b - 1] = 1
        board[b - 1][a - 1] = -1
    print(board)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                print(k, i, j)
                if board[i][k] == board[k][j] == 1:
                    print("find")
                    board[i][j] = 1
                    board[j][i] = board[k][i] = board[j][k] = -1
    print(board)

    for row in board:
        print(row)
        if row.count(0) == 1:
            answer += 1
    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

solution(n, results)
