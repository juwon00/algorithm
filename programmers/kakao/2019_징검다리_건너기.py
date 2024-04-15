from collections import deque
from math import inf


def solution(stones, k):

    # 1. Deque 에 뒤에서부터 집어 넣습니다.
    # 2. Deque의 마지막 원소가 집어넣을 원소보다 작다면, pop 해줍니다.
    # 3. Deque의 첫번째 원소가 현재 index - k 를 벗어났다면, pop 해줍니다.

    answer = inf
    print(stones, len(stones))

    q = deque()

    for i in range(len(stones)):
        print(i, "->", stones[i])
        print(q)

        if len(q) > 0 and q[0] < i - k + 1:
            print("popleft")
            q.popleft()

        while len(q) > 0 and stones[q[-1]] < stones[i]:
            print("pop")
            q.pop()
        q.append(i)

        print(q)
        if i >= k - 1 and stones[q[0]] < answer:
            answer = stones[q[0]]
            print("update", answer)
        print()

    # 13번 효율성 테스트에서만 시간초과
    # 최악의 경우 [10,9,8,7,6,5,4,3,2,1] 같이 거꾸로 정렬되어있을 때 48번째 줄의 max()를 계속 수행하기에
    # max_value = max(stones[:k])
    # answer = max_value
    #
    # for i in range(k, len(stones)):
    #     print(i)
    #     print("max", max_value)
    #     if stones[i - k] == max_value:
    #         print(stones[i - k + 1: i + 1])
    #         max_value = max(stones[i - k + 1:i + 1])
    #     else:
    #         print(stones[i])
    #         max_value = max(max_value, stones[i])
    #     print("max", max_value)
    #
    #     answer = min(answer, max_value)
    #     print()

    return answer


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

answer = solution(stones, k)
print(answer)
