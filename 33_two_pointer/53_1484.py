g = int(input())
left, right = 1, 1
weight = []

while True:
    print(left, right)

    if right - left == 1 and right ** 2 - left ** 2 > g:
        break

    if right ** 2 - left ** 2 == g:
        print("weight")
        weight.append(right)
        left += 1
        right += 1
    elif right ** 2 - left ** 2 > g:
        left += 1
    else:
        right += 1

if len(weight) > 0:
    for w in weight:
        print(w)
else:
    print(-1)
