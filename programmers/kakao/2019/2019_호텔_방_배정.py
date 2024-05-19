# 다시 풀이 생각하고 풀어볼 문제
import sys

sys.setrecursionlimit(10000000)


def find(r, room):
    print(r, room)
    if r not in room:
        room[r] = r + 1
        return r
    else:
        tmp = find(room[r], room)
        print("tmp", tmp)
        room[r] = tmp + 1
        return tmp


def solution(k, room_number):
    answer = []

    room = {}
    for r in room_number:
        print("r:", r)
        result = find(r, room)
        print("result:", result, room)
        answer.append(result)
        print()

    return answer


k = 10
room_number = [1, 3, 4, 1, 3, 1]
answer = solution(k, room_number)
print("answer:", answer)
