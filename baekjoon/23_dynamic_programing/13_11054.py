n = int(input())
a = list(map(int, input().split()))
reverseA = a[::-1]
print(a)
print(reverseA)

inc_dp = [1] * n
dec_dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            inc_dp[i] = max(inc_dp[i], inc_dp[j] + 1)
        if reverseA[i] > reverseA[j]:
            dec_dp[i] = max(dec_dp[i], dec_dp[j] + 1)

    print(inc_dp)
    print(dec_dp)
    print()

dec_dp = dec_dp[::-1]
print(inc_dp)
print(dec_dp)

result = []
for i in range(n):
    result.append(inc_dp[i] + dec_dp[i])
print(result)
print(max(result) - 1)
