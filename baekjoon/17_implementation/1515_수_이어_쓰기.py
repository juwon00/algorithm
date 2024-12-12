num = list(input())
print(num)
n = 1
while True:

    current = list(str(n))
    print(current)
    for c in current:
        print(c)
        if len(num) == 0:
            break
        if c == num[0]:
            num.pop(0)

    if len(num) == 0:
        break
    n += 1
print(n)
