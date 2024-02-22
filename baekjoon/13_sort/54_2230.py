n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

a.sort()

start = 0
end = 1
result = int(2e9)

while start <= end < n:  # start <= end 조건을 처음에 생각 못해서 런타임에러 발생 !

    if a[end] - a[start] >= m:
        # print("1 : start, end", start, end, result)
        result = min(result, a[end]-a[start])
        start += 1

    else:
        # print("2 : start, end", start, end, result)
        end += 1
    # print()

print(result)
