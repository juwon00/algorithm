# Counter 쓰는게 더 좋았을 듯
from collections import defaultdict


def solution(k, tangerine):
    answer = 0

    count_dict = defaultdict(int)

    for t in tangerine:
        count_dict[t] += 1
    # print(count_dict)

    count = sorted(count_dict.values(), reverse=True)
    # print(count)

    for i in range(len(count)):
        k = k - count[i]
        if k <= 0:
            answer = i + 1
            break

    return answer