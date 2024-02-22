import sys

input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))

start, end = 0, 0
part_sum = array[start]
min_len = sys.maxsize

while True:
    print(start, end)
    print(part_sum)
    if start == n - 1 and end == n - 1:
        if part_sum >= s and end - start + 1 < min_len:
            min_len = end - start + 1
            print("found 3", min_len)
        break

    if end == n - 1:
        print("end", start, end)

        if part_sum >= s and end - start + 1 < min_len:
            min_len = end - start + 1
            print("found 2", min_len)
        part_sum -= array[start]
        start += 1
        continue

    if part_sum < s:
        end += 1
        part_sum += array[end]
    else:
        if end - start + 1 < min_len:
            min_len = end - start + 1
            print("found", min_len)

        part_sum -= array[start]
        start += 1

if min_len == sys.maxsize:
    print(0)
else:
    print(min_len)

# 초반에 생각지 못한 반례들

# 3 9
# 1 1 10

# 3 9
# 10 1 1

# 4 7
# 4 1 2 3

# 10 10
# 1 1 1 1 1 1 1 1 1 1

# 깔끔해보이는 다른 블로그 풀이
# while True:
#     if sum >= s:
#         min_length = min(min_length, right - left)
#         sum -= nums[left]
#         left += 1
#     elif right == n:
#         break
#     else:
#         sum += nums[right]
#         right += 1
