p, m = map(int, input().split())
ranks = [[] for _ in range(300)]
for _ in range(p):
    l, n = input().split()
    l = int(l)
    print(l, n)
    for i in range(len(ranks)):
        if len(ranks[i]) == 0:
            ranks[i].append((l, n))
            break
        elif len(ranks[i]) == m:
            continue

        if ranks[i][0][0] - 10 <= l <= ranks[i][0][0] + 10:
            ranks[i].append((l, n))
            break
print(ranks)
for rank in ranks:
    if rank:
        if len(rank) == m:
            print("Started!")
            rank.sort(key=lambda x: x[1])
            for r in rank:
                print(*r)
        else:
            print("Waiting!")
            rank.sort(key=lambda x: x[1])
            for r in rank:
                print(*r)
