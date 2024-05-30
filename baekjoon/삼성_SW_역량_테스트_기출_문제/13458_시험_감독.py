n = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0
for i in range(n):
    if students[i] - b < 0:
        cnt += 1
    else:
        cnt += 1
        rest = students[i] - b
        if rest % c != 0:
            cnt += rest // c + 1
        else:
            cnt += rest // c
    print(cnt)
print()
print(cnt)
