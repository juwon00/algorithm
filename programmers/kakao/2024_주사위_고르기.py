# 중첩된 for문이 너무 많음 - 이 문제 해결 필요

import bisect


def count_greater_elements(A, B):
    count = 0
    for a in A:
        count += bisect.bisect_left(B, a)
    return count


def solution(dice):
    answer = []
    n = len(dice)
    print(n)

    li = [i for i in range(n)]
    print(li)

    vs = []
    if n // 2 == 1:
        vs = [[[0], [1]], [[1], [0]]]

    elif n // 2 == 2:
        for i in range(n):
            for j in range(i + 1, n):
                A = [i, j]
                B = [x for x in li if x not in A]
                vs.append([A, B])

    elif n // 2 == 3:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    A = [i, j, k]
                    B = [x for x in li if x not in A]
                    vs.append([A, B])

    elif n // 2 == 4:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for m in range(k + 1, n):
                        A = [i, j, k, m]
                        B = [x for x in li if x not in A]
                        vs.append([A, B])
    elif n // 2 == 5:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for m in range(k + 1, n):
                        for o in range(m + 1, n):
                            A = [i, j, k, m, o]
                            B = [x for x in li if x not in A]
                            vs.append([A, B])

    print("vs", vs)

    max_win_cnt = 0
    for a, b in vs:
        print(a, b)
        l = len(a)

        a_li = []
        for i1 in range(6):
            if l > 1:
                for i2 in range(6):
                    if l > 2:
                        for i3 in range(6):
                            if l > 3:
                                for i4 in range(6):
                                    if l > 4:
                                        for i5 in range(6):
                                            # print(i1, i2, i3, i4, i5)
                                            a_li.append(
                                                dice[a[0]][i1] + dice[a[1]][i2] + dice[a[2]][i3] + dice[a[3]][i4] +
                                                dice[a[4]][i5])
                                    else:
                                        # print(i1, i2, i3, i4)
                                        a_li.append(dice[a[0]][i1] + dice[a[1]][i2] + dice[a[2]][i3] + dice[a[3]][i4])
                            else:
                                # print(i1, i2, i3)
                                a_li.append(dice[a[0]][i1] + dice[a[1]][i2] + dice[a[2]][i3])
                    else:
                        # print(i1, i2)
                        a_li.append(dice[a[0]][i1] + dice[a[1]][i2])
            else:
                # print(i1)
                a_li.append(dice[a[0]][i1])

        b_li = []
        for i1 in range(6):
            if l > 1:
                for i2 in range(6):
                    if l > 2:
                        for i3 in range(6):
                            if l > 3:
                                for i4 in range(6):
                                    if l > 4:
                                        for i5 in range(6):
                                            # print(i1, i2, i3, i4, i5)
                                            b_li.append(
                                                dice[b[0]][i1] + dice[b[1]][i2] + dice[b[2]][i3] + dice[b[3]][i4] +
                                                dice[b[4]][i5])
                                    else:
                                        # print(i1, i2, i3, i4)
                                        b_li.append(dice[b[0]][i1] + dice[b[1]][i2] + dice[b[2]][i3] + dice[b[3]][i4])
                            else:
                                # print(i1, i2, i3)
                                b_li.append(dice[b[0]][i1] + dice[b[1]][i2] + dice[b[2]][i3])
                    else:
                        # print(i1, i2)
                        b_li.append(dice[b[0]][i1] + dice[b[1]][i2])
            else:
                # print(i1)
                b_li.append(dice[b[0]][i1])

        print(a_li)
        print(b_li)
        print(sorted(a_li))
        print(sorted(b_li))

        # 여기에서 2중 for문이 아니라 정렬 후 bisect을 사용
        win_cnt = count_greater_elements(sorted(a_li), sorted(b_li))
        print("win_cnt:", win_cnt)

        if max_win_cnt < win_cnt:
            max_win_cnt = win_cnt
            answer = [ans + 1 for ans in a]

        print()

    return answer


dice = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
answer = solution(dice)
print("answer:", answer)
