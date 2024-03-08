import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr)

# 푸는 생각은 같지만 엉뚱하게 생각한 코드
# if arr[0] != 1:
#     print(1)
#     exit()
#
# s = list()
# s.append(1)
# print(s)
#
# for i in range(1, n):
#     print("---", arr[i])
#     if arr[i] > max(s):
#         break
#     for j in range(len(s)):
#         print(i, j)
#         s.append(arr[i] + s[j])
#     s = list(set(s))
#     print(s)
# print()
# print(s)
# print(max(s) + 1)

target = 1
for num in arr:
    print(num, target)
    if target < num:
        break

    target += num
print(target)
