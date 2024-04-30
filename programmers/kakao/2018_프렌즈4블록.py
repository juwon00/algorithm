def squareCheck(i, j, boards):
    stand = boards[i][j]
    if stand == ".":
        return False
    if boards[i + 1][j] == stand and boards[i][j + 1] == stand and boards[i + 1][j + 1] == stand:
        return True
    return False


def down(i, j, boards):
    print(i - 1)
    if i - 1 < 0:
        return (".", -1, -1)
    if boards[i - 1][j] != ".":
        return (boards[i - 1][j], i - 1, j)
    else:
        return down(i - 1, j, boards)


def solution(m, n, board):
    answer = 0

    boards = []
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(board[i][j])
        boards.append(tmp)
    for b in boards:
        print(b)
    print()

    while True:

        squares = []
        for i in range(m - 1):
            for j in range(n - 1):
                if squareCheck(i, j, boards):
                    squares.append((i, j))

        if len(squares) == 0:
            break

        for s in squares:
            (boards[s[0]][s[1]], boards[s[0] + 1][s[1]], boards[s[0]][s[1] + 1],
             boards[s[0] + 1][s[1] + 1]) = ".", ".", ".", "."
        for b in boards:
            print(b)
        print()

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                print(i, j)
                if boards[i][j] == ".":
                    print("find")
                    char, di, dj = down(i, j, boards)
                    print(char, di, dj)
                    print()
                    if char != ".":
                        boards[i][j], boards[di][dj] = char, "."

        for b in boards:
            print(b)
        print()

    for i in range(m):
        for j in range(n):
            if boards[i][j] == ".":
                answer += 1

    return answer


m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
answer = solution(m, n, board)
print("answer:", answer)
