# 다시 생각하고 풀어보자

from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    weak_size = len(weak)
    for i in range(len(weak)):
        weak.append(weak[i] + n)
    print(weak)

    for start in range(weak_size):
        print("start", start)
        for friends in list(permutations(dist, len(dist))):
            print("friends", friends)
            count = 0
            position = weak[start] - friends[count - 1]
            print("count", count)
            print("position", position)
            for index in range(start, start + weak_size):
                print("index", index)
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            print()
            answer = min(answer, count)
        print()

    if answer > len(dist):
        return -1

    return answer


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
answer = solution(n, weak, dist)
print("answer:", answer)
