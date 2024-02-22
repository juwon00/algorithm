import math

n = int(input())
if n == 1:
    print(0)
    exit()

array = [True] * (n + 1)
array[0], array[1] = False, False

for i in range(2, int(math.sqrt(n)) + 1):
    print(i)
    if array[i]:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
print(array)

prime_number = []
for i in range(n + 1):
    if array[i]:
        prime_number.append(i)
print(prime_number)

start, end = 0, 0
sum = 2  # start, end가 0,0으로 시작해서 처음 소수인 2부터 시작
cnt = 0
while True:
    print("start, end", start, end, sum)
    if start == n:
        print(1)
        break
    elif sum > n:
        print(2)
        sum -= prime_number[start]
        start += 1
    elif sum == n:
        print("3, found")
        cnt += 1
        if start == len(prime_number) - 1 and end == len(prime_number) - 1:
            break
        sum -= prime_number[start]
        start += 1
    else:
        print(4)
        if start == len(prime_number) - 1 and end == len(prime_number) - 1:
            break
        end += 1
        sum += prime_number[end]

print("cnt", cnt)
