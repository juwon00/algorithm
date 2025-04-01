from itertools import combinations

n = int(input())
result = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = ''.join(list(map(str, reversed(list(j)))))
        result.append(int(num))

result.sort()

if n >= len(result):
    print(-1)
else:
    print(result[n])

# # 다시 볼 문제 - 시간초과 (combinations, 백트래킹 방법으로)
#
# def get_decreasing_number(N):
#     if N >= 1023:  # 감소하는 수는 최대 1023개 존재
#         return -1
#
#     count = 0
#     num = 0
#
#     while True:
#         if is_decreasing(num):  # 감소하는 수인지 확인
#             count += 1
#             if count == N + 1:  # N번째 감소하는 수 찾기
#                 return num
#         num += 1
#
#
# def is_decreasing(n):
#     str_n = str(n)
#     return all(str_n[i] > str_n[i + 1] for i in range(len(str_n) - 1))
#
#
# n = int(input())
# print(get_decreasing_number(n))
