from collections import deque


def similar(x, y):
    count = 0
    length = len(x)

    for i in range(length):
        if x[i] == y[i]:
            count += 1

    if count == length - 1:
        return True
    else:
        return False


def solution(begin, target, words):
    answer = 0
    if target not in words:
        print("no words")
        return answer

    visited = [False] * (len(words))
    cnt = [0] * (len(words))

    q = deque()
    q.append((begin, 0))

    print(q)
    print(visited)
    print(cnt)

    while q:
        now, dist = q.popleft()
        print(now)

        if now == target:
            print(cnt)
            return max(cnt)

        for i in range(len(words)):
            if not visited[i] and similar(now, words[i]):
                visited[i] = True
                cnt[i] = dist + 1
                q.append((words[i], cnt[i]))


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
solution(begin, target, words)
