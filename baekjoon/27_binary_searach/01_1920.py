n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
find = list(map(int, input().split()))

print(n, a)
print(m, find)

for i in range(len(find)):
    print()
    print(find[i])
    start = 0
    end = n - 1
    while start <= end:

        mid = (start + end) // 2
        print(start, end, mid)
        print(a[mid], find[i])
        if a[mid] == find[i]:
            print("find")
            start = mid
            end = mid
            break

        elif a[mid] > find[i]:
            end = mid - 1

        else:
            start = mid + 1

    print(start, end, mid)
    if start == mid and end == mid:
        print(1)
    else:
        print(0)
