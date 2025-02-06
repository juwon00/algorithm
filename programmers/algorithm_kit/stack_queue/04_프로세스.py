from collections import deque


def solution(priorities, location):
    answer = 1
    q = deque()
    max_list = sorted(priorities, reverse=True)
    print(max_list)
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    print(q)

    while q:
        cost, dist = q.popleft()
        print(cost, dist)
        if cost == max_list[0]:
            print("out")
            if dist == location:
                return answer
            else:
                answer += 1
                max_list.pop(0)
        else:
            q.append((cost, dist))


priorities, locations = [1, 1, 9, 1, 1, 1], 0
print(solution(priorities, locations))
