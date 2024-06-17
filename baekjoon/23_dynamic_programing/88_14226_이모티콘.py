from collections import deque

s = int(input())
visited = [[0] * 1001 for i in range(1001)]
answer = 0
q = deque()
q.append((1, 0))

while q:
    screen, clip, = q.popleft()
    print("now", screen, clip)

    if screen == s:
        answer = visited[screen][clip]
        break

    arr = [
        (screen, screen),
        (screen + clip, clip),
        (screen - 1, clip)
    ]

    for n_screen, n_clip in arr:
        if 0 <= n_screen < 1001 and 0 <= n_clip < 1001 and not visited[n_screen][n_clip]:
            q.append((n_screen, n_clip))
            visited[n_screen][n_clip] = visited[screen][clip] + 1

print(answer)

# 다른 사람이 1차원 dp로 푼 코드
# s = int(input())
# d = list(range(1002))
# for i in range(2, s + 1):
#     j = 2
#     while i * j < 1002:
#         d[i * j] = min(d[i * j], d[i] + j)
#         d[i * j - 1] = min(d[i * j - 1], d[i * j] + 1)
#         j += 1
# print(d[s])
