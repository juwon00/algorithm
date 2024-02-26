from itertools import permutations


def solution(k, dungeons):
    answer = -1
    can_go = list(permutations(dungeons, len(dungeons)))
    print(can_go)
    for i in range(len(can_go)):
        cnt = 0
        _k = k
        print(can_go[i])
        for j in range(len(dungeons)):
            print(can_go[i][j])
            if _k >= can_go[i][j][0]:
                print("go")
                _k -= can_go[i][j][1]
                cnt += 1
            print(_k)
        answer = max(answer, cnt)
        print()
    print(answer)
    return answer


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
solution(k, dungeons)
