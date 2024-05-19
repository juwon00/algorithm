# 다시 플어볼 문제

from itertools import combinations


def solution(relation):
    answer = 0

    row = len(relation)
    col = len(relation[0])
    print(row, col)

    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))
    print(combi)

    unique = []
    for i in combi:
        tmp = [tuple(item[key] for key in i) for item in relation]
        if len(set(tmp)) == row:
            unique.append(i)
    print(unique)

    answer = set(unique)
    print(answer)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            print(i, j)
            print(unique[i])
            print(set(unique[i]) & set(unique[j]))
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                print("discard")
                answer.discard(unique[j])
            print(answer)
            print()

    return len(answer)


relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
answer = solution(relation)
print("answer:", answer)
