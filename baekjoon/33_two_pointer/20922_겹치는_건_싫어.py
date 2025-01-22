from collections import defaultdict

n, k = map(int, input().split())
sequence = list(map(int, input().split()))
dic = defaultdict(int)
dic[sequence[0]] += 1
left, right = 0, 0
max_count = 1
max_length = 0
while True:
    if right == n - 1:
        break
    print(left, right)
    if max_count <= k:
        print("right")
        right += 1
        dic[sequence[right]] += 1
        max_count = max(max_count, dic[sequence[right]])
        if max_count > k:
            length = right - left
            max_index = sequence[right]
        else:
            length = right - left + 1
        max_length = max(max_length, length)
    else:
        print("left")
        dic[sequence[left]] -= 1
        if sequence[left] == max_index:
            max_count -= 1
        left += 1
    print(dic)
    print(max_count)
    print(max_length)
    print()
print(max_length)
