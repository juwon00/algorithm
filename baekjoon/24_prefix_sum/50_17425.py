import sys

input = sys.stdin.readline

# 내가 처음에 작성한 코드 - 시간 초과
#
# def get_devisor_sum(n):
#     data = 0
#     for i in range(1, int(n ** (1 / 2)) + 1):
#         if n % i == 0:
#             data += i
#             data += (n // i)
#     return data
#
#
# prefix_sum = [0]
# for i in range(1, 1000001):
#     prefix_sum.append(get_devisor_sum(i) + prefix_sum[i - 1])
# print(prefix_sum)

max_num = 1000000

prefix_sum = [0 for _ in range(max_num + 1)]
m = [0 for _ in range(max_num + 1)]

for i in range(1, max_num + 1):
    j = 1
    while i * j <= max_num:
        print(i, j, i * j)
        m[i * j] += i
        j += 1
    prefix_sum[i] = m[i] + prefix_sum[i - 1]

for _ in range(int(input())):
    n = int(input())
    print(prefix_sum[n])
