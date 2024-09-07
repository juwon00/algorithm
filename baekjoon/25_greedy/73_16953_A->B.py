a, b = map(int, input().split())

result = 1
while a <= b:
    print(a, b)
    if a == b:
        break
    elif b % 2 == 0:
        b = b // 2
        result += 1
    elif b % 10 == 1:
        b = int(str(b)[:-1])
        result += 1
    else:
        break

print(a, b)
if a == b:
    print(result)
else:
    print(-1)
