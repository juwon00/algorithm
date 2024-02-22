import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()
print(array)

start = 0
end = n - 1

similar = sys.maxsize
start_point = 0
end_point = n - 1

while start < end:

    print(array[start] + array[end], similar)
    if abs(array[start] + array[end]) < similar:
        print("similar", array[start], array[end])
        similar = abs(array[start] + array[end])
        start_point = start
        end_point = end

    if array[start] + array[end] > 0:
        end -= 1
    else:
        start += 1

print()
print(array[start_point], array[end_point])
