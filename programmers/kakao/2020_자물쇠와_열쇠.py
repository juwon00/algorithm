def rotate(m, d):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    if d % 4 == 1:
        for r in range(N):
            for c in range(N):
                ret[c][N - 1 - r] = m[r][c]
    elif d % 4 == 2:
        for r in range(N):
            for c in range(N):
                ret[N - 1 - r][N - 1 - c] = m[r][c]
    elif d % 4 == 3:
        for r in range(N):
            for c in range(N):
                ret[N - 1 - c][r] = m[r][c]

    return ret


def solution(key, lock):
    answer = False

    n = len(lock)
    m = len(key)

    zero_cnt = 0
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                zero_cnt += 1
    print(zero_cnt)

    big_lock = [[0] * (n + 2 * m - 2) for _ in range(n + 2 * m - 2)]
    for i in range(n):
        for j in range(n):
            big_lock[i + m - 1][j + m - 1] = lock[i][j]
    for b in big_lock:
        print(b)
    print()

    keys = [key]
    for i in range(1, 4):
        keys.append(rotate(key, i))
    for ke in keys:
        for k in ke:
            print(k)
        print()

    for k in keys:

        for i in range(n + m - 1):
            for j in range(n + m - 1):
                print(i, j, k)
                cnt = 0
                flag = False
                for x in range(m):
                    for y in range(m):
                        if flag:
                            break
                        print(x, y, x + i, y + j)
                        if m - 1 <= x + i < m + n - 1 and m - 1 <= y + j < m + n - 1:
                            print("check")
                            if k[x][y] == 1 and big_lock[x + i][y + j] == 1:
                                print("break")
                                flag = True
                            if k[x][y] == 1 and big_lock[x + i][y + j] == 0:
                                cnt += 1
                print("cnt", cnt)
                print()
                if cnt == zero_cnt:
                    return True

        print()

    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
answer = solution(key, lock)
print("answer:", answer)
