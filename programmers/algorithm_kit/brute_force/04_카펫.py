def solution(brown, yellow):
    answer = []

    print(int(brown / 2) + 2)
    row_col_sum = int(brown / 2) + 2
    for i in range(3, int(row_col_sum / 2) + 1):
        print(i, row_col_sum - i)
        w = row_col_sum - i
        h = i

        if (w - 2) * (h - 2) == yellow:
            answer.append(w)
            answer.append(h)
            break
    print(answer)
    return answer


brown = 24
yellow = 24
solution(brown, yellow)
