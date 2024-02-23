def solution(n, lost, reserve):
    answer = n

    lost = sorted(lost)
    reserve = sorted(reserve)

    lost_get = [False] * n
    borrow = [False] * n

    answer = answer - len(lost)
    print(answer)

    for i in range(len(lost)):
        for j in range(len(reserve)):
            print(i, j)
            if lost[i] == reserve[j]:
                answer += 1
                borrow[j] = True
                lost_get[i] = True

    for i in range(len(lost)):
        for j in range(len(reserve)):
            print(i, j)
            if (lost[i] == reserve[j] - 1 or lost[i] == reserve[j] + 1) and borrow[
                j] == False and lost_get[i] == False:
                print("borrow", lost[i], reserve[j])
                answer += 1
                borrow[j] = True
                lost_get[i] = True
    print(answer)

    return answer


n = 4
lost = [2, 3]
reserve = [3, 4]
solution(n, lost, reserve)
