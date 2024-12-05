n, x, p = map(int, input().split())
if n != 0:
    score = list(map(int, input().split()))
    score.append(x)
    score.sort(reverse=True)
    idx = score.index(x) + 1
    if idx > p:
        print(-1)
    else:
        if n == p and x == score[-1]:
            print(-1)
        else:
            print(idx)
else:
    print(1)
