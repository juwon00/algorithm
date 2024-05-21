# 다시 풀어볼 문제

from bisect import bisect_left
from collections import defaultdict
from itertools import combinations


def solution(info, query):
    answer = []
    info_hash = defaultdict(list)

    for i in info:
        splited_info = i.split()
        score = splited_info.pop()
        for r in range(5):
            combs = combinations(range(4), r)

            for comb in combs:
                key = splited_info[:]
                for elem in comb:
                    key[elem] = "-"

                info_hash[" ".join(key)].append(int(score))
    for item in info_hash:
        info_hash[item].sort()

    for q in query:
        splited_q = q.replace(" and", "").split()
        target_score = int(splited_q.pop())

        target_key = " ".join(splited_q)

        matched_score_list = info_hash[target_key]

        if not matched_score_list:
            answer.append(0)
            continue

        score_len = len(matched_score_list)

        start = bisect_left(matched_score_list, target_score)

        answer.append(score_len - start)

    return answer


# 다른사람이 푼 정석적인 풀이
# def solution(info, query):
#     data = dict()
#     for a in ['cpp', 'java', 'python', '-']:
#         for b in ['backend', 'frontend', '-']:
#             for c in ['junior', 'senior', '-']:
#                 for d in ['chicken', 'pizza', '-']:
#                     data.setdefault((a, b, c, d), list())
#     for i in info:
#         i = i.split()
#         for a in [i[0], '-']:
#             for b in [i[1], '-']:
#                 for c in [i[2], '-']:
#                     for d in [i[3], '-']:
#                         data[(a, b, c, d)].append(int(i[4]))
#
#     for k in data:
#         data[k].sort()
#
#         # print(k, data[k])
#
#     answer = list()
#     for q in query:
#         q = q.split()
#
#         pool = data[(q[0], q[2], q[4], q[6])]
#         find = int(q[7])
#         l = 0
#         r = len(pool)
#         mid = 0
#         while l < r:
#             mid = (r + l) // 2
#             if pool[mid] >= find:
#                 r = mid
#             else:
#                 l = mid + 1
#             # print(l, r, mid, answer)
#         # answer.append((pool, find, mid))
#         answer.append(len(pool) - l)
#
#     return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
answer = solution(info, query)
print("answer:", answer)
