n, m = map(int, input().split())

A = list(map(int, input().split()))

for i in range(m):
    A = sorted(A)
    min_sum = A[0] + A[1]
    # print(min_sum)
    A[0] = min_sum
    A[1] = min_sum

print(sum(A))

