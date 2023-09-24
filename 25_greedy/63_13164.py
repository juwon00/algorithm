import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kid = list(map(int, input().split()))

ans = []
for i in range(1, n):
    ans.append(kid[i] - kid[i-1])
ans.sort(reverse=True)

print(sum(ans[k-1:]))