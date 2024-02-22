n = int(input())
left_tall = list(map(int, input().split()))

for x in range(len(left_tall)):
    tmp = list()
    tmp.append(x + 1)
    tmp.append(left_tall[x])
    left_tall[x] = tmp

result = [0] * n

for i in range(n):
    # print("i", i)
    pass_zero = left_tall[i][1]
    # print(pass_zero)
    for j in range(n):
        # print("j", j)
        if pass_zero > 0:
            if result[j] == 0:
                # print("--")
                pass_zero -= 1
                continue
        else:
            if result[j] == 0:
                result[j] = i + 1
                break

# print(result)
print(' '.join(map(str, result)))
