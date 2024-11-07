import sys
from collections import defaultdict

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
graph = [int(input()) for _ in range(n)]
graph.extend(graph)
result = 0
left, right = 0, 0
window = defaultdict(int)
window[c] += 1

for i in range(k):
    window[graph[i]] += 1
    right += 1
print(left, right)
print(window)
print()

for _ in range(n):
    print(window)
    result = max(result, len(window))
    print(result)
    window[graph[right]] += 1
    window[graph[left]] -= 1
    if window[graph[left]] == 0:
        del window[graph[left]]
    right += 1
    left += 1

print(result)
