from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

n = int(input())
num_card = list(map(int, input().split()))
num_card.sort()

m = int(input())
find = list(map(int, input().split()))

print(n, num_card)
print(m, find)

for f in find:
    count = bisect_right(num_card, f) - bisect_left(num_card, f)
    print(count, end=" ")
