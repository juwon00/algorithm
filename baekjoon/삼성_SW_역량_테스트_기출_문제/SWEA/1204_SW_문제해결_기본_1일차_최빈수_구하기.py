from collections import Counter

T = int(input())
for i in range(1, T + 1):
    _ = int(input())
    sample = list(map(int, input().split()))
    counter = Counter(sample)
    max_count = max(counter.values())
    result = max([key for key, count in counter.items() if count == max_count])
    print(f"#{i} {result}")