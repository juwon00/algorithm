def cal(row, col, d1, d2):
    global total, answer
    one, two, three, four = 0, 0, 0, 0

    c1 = col + 1
    for r in range(row + d1):
        if r >= row:
            c1 -= 1
        one += sum(graph[r][:c1])

    c2 = col + 1
    for r in range(row + d2 + 1):
        if r > row:
            c2 += 1
        two += sum(graph[r][c2:])

    c3 = col - d1
    for r in range(row + d1, n):
        three += sum(graph[r][:c3])
        if r < row + d1 + d2:
            c3 += 1

    c4 = col + d2 - n
    for r in range(row + d2 + 1, n):
        four += sum(graph[r][c4:])
        if r <= row + d1 + d2:
            c4 -= 1

    five = total - one - two - three - four
    print(one, two, three, four, five)

    answer = min(answer, (max(one, two, three, four, five) - min(one, two, three, four, five)))


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
total = 0
for g in graph:
    total += sum(g)
answer = int(1e9)

for g in graph:
    print(g)

for r in range(n):
    for c in range(n):
        print(">>>", r, c)

        for d1 in range(1, n):
            for d2 in range(1, n):
                xl, yl = r + d1, c - d1
                xr, yr = r + d2, c + d2
                xs, ys = r + d1 + d2, c - (d1 - d2)
                if xl < 0 or xl >= n or yl < 0 or yl >= n or xr < 0 or xr >= n or yr < 0 or yr >= n or xs < 0 or xs >= n or ys < 0 or ys >= n:
                    continue
                print(d1, d2)
                cal(r, c, d1, d2)

        print()

print(answer)
