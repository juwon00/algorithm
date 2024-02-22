n = int(input())
m = int(input())
armor = list(map(int, input().split()))
armor.sort()
print(armor)

left, right = 0, n - 1
count = 0

while True:
    print(left, right)

    if left >= right:
        break
    elif armor[left] + armor[right] == m:
        print("count")
        count += 1
        left += 1
        right -= 1
    elif armor[left] + armor[right] < m:
        left += 1
    else:
        right -= 1

print(count)
