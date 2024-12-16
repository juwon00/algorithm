n = int(input())
big = [list(map(int, input().split())) for _ in range(n)]
ranking = [1] * n
print(big)
print(ranking)

for i in range(n):
    print("i =", i, big[i])
    for j in range(n):
        if i == j:
            continue
        print(big[j])

        if big[i][0] < big[j][0] and big[i][1] < big[j][1]:
            ranking[i] += 1

print(*ranking)
