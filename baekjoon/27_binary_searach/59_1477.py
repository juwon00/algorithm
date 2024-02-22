n, m, l = map(int, input().split())
li = list(map(int, input().split()))

li.append(0)
li.append(l)
li.sort()
print(li)

left = 1
right = l - 1
result = 0

while left <= right:
    print(li)
    print(left, right)
    cnt = 0
    mid = (left + right) // 2
    print("mid:", mid)

    for i in range(1, len(li)):
        if li[i] - li[i-1] > mid:
            print("li[i], li[i-1]", li[i], li[i-1], "+cnt:", (li[i] - li[i-1] - 1) // mid)
            cnt += (li[i] - li[i-1] - 1) // mid

    print("cnt:", cnt)

    if cnt > m:
        left = mid + 1
    else:
        result = mid
        print("result:", result)
        right = mid - 1
    print()

print(result)
