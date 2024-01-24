n = int(input())
array = list(map(int, input().split()))
array.sort()
x = int(input())

print(array)

count = 0
start = 0
end = n - 1
while start < end:
    print(start, end, array[start], array[end])
    if array[start] + array[end] == x:
        print("count")
        count += 1
        start += 1
        end -= 1
    elif array[start] + array[end] > x:
        end -= 1
    else:
        start += 1

print(count)
