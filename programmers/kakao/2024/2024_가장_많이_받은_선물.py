def solution(friends, gifts):
    table = [[0] * len(friends) for _ in range(len(friends))]
    dic = dict()
    for friend in friends:
        dic[friend] = 0

    for gift in gifts:
        give, receive = gift.split(" ")
        dic[give] += 1
        dic[receive] -= 1
        table[friends.index(give)][friends.index(receive)] += 1
    print(dic)
    for t in table:
        print(t)

    result = dict()
    for friend in friends:
        result[friend] = 0

    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            print(i, j, " - ", j, i)
            if table[i][j] == table[j][i]:
                print("check")
                print(friends[i], friends[j])
                if dic[friends[i]] > dic[friends[j]]:
                    result[friends[i]] += 1
                elif dic[friends[i]] < dic[friends[j]]:
                    result[friends[j]] += 1
            elif table[i][j] > table[j][i]:
                # print("up", i, friends[i])
                result[friends[i]] += 1
            else:
                # print("down", j, friends[j])
                result[friends[j]] += 1
    print(result)
    print(max(result.values()))

    return max(result.values())


friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
answer = solution(friends, gifts)
print("answer:", answer)
