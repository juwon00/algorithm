import sys

input = sys.stdin.readline

n, m = map(int, input().split())
words = {}
cnt = 0

for _ in range(n):
    words[input().rstrip()] = 1
    cnt += 1

for _ in range(m):
    keyword = list(input().rstrip().split(','))
    for k in keyword:
        if k in words.keys():
            cnt -= 1
            del words[k]
    print(cnt)
