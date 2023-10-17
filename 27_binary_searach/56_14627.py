s, c = map(int, input().split())

l = []
for i in range(s):
    l.append(int(input()))

# print(s, c, l)

left = 0
right = max(l)
result = 0

while left <= right:
    print()
    print("left, right", left, right)

    mid = (left + right) // 2
    print(mid)

    if mid == 0:  # ZeroDivisionError 해결
        break

    tmp = 0
    rest = 0
    for length in l:
        tmp += length // mid
        rest += length % mid
        print("tmp", tmp)
        print("rest", rest)

    if tmp >= c:
        result = rest + (tmp - c) * mid  # (tmp - c) * mid 이유 :  반례  3,5  10  10  10
        left = mid + 1
        print("result", result)

    else:
        right = mid - 1

print(result)
