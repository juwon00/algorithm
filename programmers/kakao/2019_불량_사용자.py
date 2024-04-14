def similar(ban, user):
    if len(ban) != len(user):
        return False
    for i in range(len(ban)):
        if ban[i] != user[i] and ban[i] != '*':
            return False
    return True


def get_combi(com):
    print(com)

    def backtrack(start, path, selected):
        if len(com) == len(path):
            result.append(path[:])
        print()
        print(start)
        print("selected", selected)
        print("path", path)
        for i in range(start, len(com)):
            print(i)
            for num in com[i]:
                print("num:", num)
                if num not in path:
                    path.append(num)
                    selected.append(i)
                    backtrack(i + 1, path, selected)
                    path.pop()
                    selected.pop()

    result = []
    backtrack(0, [], [])
    return result


def solution(user_id, banned_id):
    answer = 0

    com = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        # print(banned_id[i])
        for j in range(len(user_id)):
            # print(user_id[j])
            if similar(banned_id[i], user_id[j]):
                com[i].append(j)
    print(com)

    combi = get_combi(com)
    print(combi)

    combi_sort = set()
    for c in combi:
        c = sorted(c)
        print(c)
        combi_sort.add(tuple(c))
    print(combi_sort)
    answer = len(combi_sort)

    return answer


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
result = solution(user_id, banned_id)
print("answer:", result)
