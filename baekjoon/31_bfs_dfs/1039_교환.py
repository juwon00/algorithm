from collections import deque

n, k = map(int, input().split())
n = str(n)
m = len(n)
q = deque()
q.append((n, 0))
visited = set()
visited.add((n, 0))
answer = 0

while q:
    now, depth = q.popleft()
    print(now, depth)

    if depth == k:
        answer = max(answer, int(now))
        continue

    for i in range(m):
        for j in range(i + 1, m):
            print(i, j)
            n_list = list(now)
            n_list[i], n_list[j] = n_list[j], n_list[i]
            result = "".join(n_list)
            print(result)
            if result[0] == "0":
                continue
            if (result, depth + 1) not in visited:
                visited.add((result, depth + 1))
                q.append((result, depth + 1))
        print()

print(visited)
print(answer if answer else -1)
