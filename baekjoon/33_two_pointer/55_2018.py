n = int(input())

left, right = 0, 0
sum = 0
count = 0

while True:
    print("left, right", left, right, sum, count)

    if right == n and left == n:
        break

    if sum == n:
        count += 1
        left += 1
        sum -= left

    elif sum < n:
        right += 1
        sum += right
    else:
        left += 1
        sum -= left

print(count)
