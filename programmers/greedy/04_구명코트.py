# 처음 생각했던 풀이 - 시간초과
# def solution(people, limit):
#     answer = 0
#     print(people)
#
#     while sum(people) > 0:
#
#         people = sorted(people, reverse=True)
#         tmp = 0
#         remove_index = []
#
#         for i in range(len(people)):
#             if tmp + people[i] <= limit:
#                 tmp += people[i]
#                 remove_index.append(i)
#                 if len(remove_index) == 2:
#                     break
#
#         for r in remove_index:
#             people[r] = 0
#
#         answer += 1
#
#     return answer

from collections import deque


def solution(people, limit):
    count = 0  # 구명보트 개수
    people = deque(sorted(people))  # 오름차순, 사람들의 몸무게 기준

    # 모든 사람이 구출될 때 까지
    while people:
        # 몸무게가 가장 큰 사람 구출
        person = people.pop()
        # 아직 남은사람이 있고, 가장 가벼운 사람이 무거운 사람과 같이타도 무게 제한에 안걸리면 같이 구출
        if len(people) > 0 and person + people[0] <= limit:
            people.popleft()

        count += 1

    return count


people = [20, 40, 40, 40, 40]
limit = 100
solution(people, limit)
