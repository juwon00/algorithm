def is_zero(s):
    print("===============>= ", s)
    if eval(s.replace(" ", "")) == 0:
        return True
    else:
        return False


def back_tracking(x, target, s):
    print(x, s)
    if x == target:
        if is_zero(s):
            result.append(s)
        return
    for sign in [" ", "+", "-"]:
        back_tracking(x + 1, target, s + sign + str(x + 1))


for _ in range(int(input())):
    n = int(input())
    print(n)
    result = []
    back_tracking(1, n, "1")
    for r in result:
        print(r)

    print()
