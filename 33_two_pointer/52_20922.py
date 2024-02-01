import sys

input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))
print(array)

tmp = []
left, right = 0, 0
max_length = 0

# 왜인지 투 포인터 알고리즘이 틀렸다
# while True:
#     print("left right", left, right)
#     if right == n:
#         break
#
#     tmp.append(array[right])
#     if tmp.count(array[right]) > k:
#         max_length = max(max_length, right - left)
#         tmp_pop = left
#         left = left + array.index(array[right]) + 1
#         tmp = tmp[left - tmp_pop:]
#
#     right += 1
# max_length = max(max_length, right - left)

counter = [0] * (max(array) + 1)
while right < n:
    if counter[array[right]] < k:
        counter[array[right]] += 1
        right += 1
    else:
        counter[array[left]] -= 1
        left += 1
    max_length = max(max_length, right - left)

print(max_length)
