from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))
print(numbers)
print(operator)

operators = []
for i in range(4):
    for j in range(operator[i]):
        operators.append(i)
print(operators)

max_result = int(-1e10)
min_result = int(1e10)

for c in list(permutations(operators, len(operators))):
    print(c)
    tmp = 0
    for i in range(n - 1):
        if i == 0:
            if c[i] == 0:
                tmp = numbers[i] + numbers[i + 1]
            elif c[i] == 1:
                tmp = numbers[i] - numbers[i + 1]
            elif c[i] == 2:
                tmp = numbers[i] * numbers[i + 1]
            elif c[i] == 3:
                tmp = numbers[i] // numbers[i + 1]
        else:
            if c[i] == 0:
                tmp = tmp + numbers[i + 1]
            elif c[i] == 1:
                tmp = tmp - numbers[i + 1]
            elif c[i] == 2:
                tmp = tmp * numbers[i + 1]
            elif c[i] == 3:
                if tmp < 0:
                    tmp = abs(tmp) // numbers[i + 1]
                    tmp = tmp * (-1)
                else:
                    tmp = tmp // numbers[i + 1]

    print(tmp)
    max_result = max(max_result, tmp)
    min_result = min(min_result, tmp)
print(max_result)
print(min_result)



# 다른사람의 백트래킹 풀이 방법
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# num = list(map(int, input().split()))
# op = list(map(int, input().split()))  # +, -, *, //
#
# maximum = -1e9
# minimum = 1e9
#
#
# def dfs(depth, total, plus, minus, multiply, divide):
#     global maximum, minimum
#     if depth == N:
#         maximum = max(total, maximum)
#         minimum = min(total, minimum)
#         return
#
#     if plus:
#         dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
#     if minus:
#         dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
#     if multiply:
#         dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
#     if divide:
#         dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)
#
#
# dfs(1, num[0], op[0], op[1], op[2], op[3])
# print(maximum)
# print(minimum)