from collections import deque

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
q = deque(arr)
print(q)

result = 0
while q:
    now = q.popleft()
    print("now", now)
    if q:
        if now > 1:
            next = q.popleft()
            if next > 1:
                result += now * next
            else:
                result += now
                q.appendleft(next)

        elif now == 1:
            result += now

        elif now == 0:
            if len(q) >= 2:
                l4 = q.pop()
                l5 = q.pop()
                result += l4 * l5
                q.appendleft(now)
            else:
                last = q.pop()
                result += now * last

        else:
            print(q)
            if len(q) >= 2:
                l1 = q.pop()
                l2 = q.pop()
                q.appendleft(now)
                result += l1 * l2
            elif len(q) == 1:
                l3 = q.pop()
                result += now * l3

    else:
        result += now

    print("result", result)
    print()
print(result)

# 다른분 블로그에서 본 깔끔한 풀이
# 기본 풀이 과정은 같다
# import sys
#
# input = sys.stdin.readline
# N = int(input())
#
# arr = []
# m_arr = []
# res = 0
# for _ in range(N):
#     x = int(input())
#     if x <= 0:
#         m_arr.append(x)
#     elif x == 1:
#         res += 1
#     else:
#         arr.append(x)
#
# m_arr.sort()
# arr.sort(reverse=True)
#
# if len(arr) % 2 != 0:
#     arr.append(1)
# if len(m_arr) % 2 != 0:
#     m_arr.append(1)
# for i in range(0, len(arr), 2):
#     res += (arr[i] * arr[i + 1])
# for i in range(0, len(m_arr), 2):
#     res += (m_arr[i] * m_arr[i + 1])
# print(res)
