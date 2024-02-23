def solution(name):
    answer = 0

    # 좌우 이동 횟수 세기
    min_move = len(name) - 1

    for i, char in enumerate(name):
        print(i, char)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            print(next, len(name), name[next])
            next += 1
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])  # 일반, 왼쪽먼저, 오른쪽먼저
        print("min", min_move)
    answer += min_move

    # 상하 이동 횟수 세기
    for i in range(len(name)):
        if name[i] != 'A':
            print(name[i], ord(name[i]), ord(name[i]) - 65)
            if ord(name[i]) - 65 <= 13:
                print("answer +=", ord(name[i]) - 65)
                answer += ord(name[i]) - 65
            else:
                print("answer +=", 26 - (ord(name[i]) - 65))
                answer += 26 - (ord(name[i]) - 65)
    print(answer)

    return answer


name = "JAZ"
solution(name)
