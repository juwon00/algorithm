S = input()
T = input()


def recursive(t):
    global result
    print(t)
    if t == S:
        result = 1
        return
    if len(t) == 0:
        return
    if t[-1] == 'A':
        recursive(t[:-1])
    if t[0] == 'B':
        recursive(t[1:][::-1])


result = 0
recursive(T)
print(result)

# 시간 초과 풀이
# def append_a(x):
#     return x + 'A'
#
#
# def append_b(x):
#     x = x + 'B'
#     reverse = ''
#     for i in range(len(x) - 1, -1, -1):
#         reverse += x[i]
#     return reverse
#
#
# S = input()
# T = input()
#
# q = set()
# q.add(S)
# while len(list(q)[0]) < len(T):
#     tmp = set()
#     while q:
#         x = q.pop()
#         tmp.add(append_a(x))
#         tmp.add(append_b(x))
#     q = tmp
#
# result = 0
# for value in q:
#     if value == T:
#         result = 1
#         break
#
# print(result)
