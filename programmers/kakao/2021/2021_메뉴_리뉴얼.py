from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:
        print(c)
        cnt = defaultdict(int)
        for order in orders:
            order = sorted(order)
            # print(list(combinations(order, c)))
            for o in list(combinations(order, c)):
                cnt[o] += 1
        print(cnt)

        if len(cnt) > 0:
            print("max ->", max(cnt.values()))
            if max(cnt.values()) > 1:
                for key, value in cnt.items():
                    if value == max(cnt.values()):
                        answer.append("".join(key))

        print()
    print(answer)
    answer.sort()
    return answer


orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
answer = solution(orders, course)
print("answer:", answer)
