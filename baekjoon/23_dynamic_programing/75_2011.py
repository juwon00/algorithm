code = [9] + list(map(int, input()))
print(code)
length = len(code)

remove_zero = []
for j in range(1, length):
    if code[j] == 0 and (code[j - 1] > 2 or code[j - 1] == 0):
        print(0)
        exit()
    elif code[j] == 0:
        print("zero", j)
        remove_zero.append(j)
remove_zero.sort(reverse=True)
print(remove_zero)

for r in remove_zero:
    code[r] = 0
    code.pop(r - 1)

length = len(code)
print(code, length)
dp = [0] * length
dp[0], dp[1] = 1, 1
print(dp)
pass_i = []
for i in range(2, length):
    print(i, pass_i)

    if i in pass_i:
        print("pass")
        continue

    if code[i] == 0:
        if length - 1 > i:
            dp[i] = dp[i - 1]
            dp[i + 1] = dp[i]
            pass_i.append(i + 1)
        else:
            dp[i] = dp[i - 1]
    elif 0 < code[i - 1] <= 2:
        x = code[i - 1] * 10 + code[i]
        print(x)
        if x < 27:
            dp[i] = dp[i - 1] + dp[i - 2]
        else:
            dp[i] = dp[i - 1] + dp[i - 2] - 1
    else:
        dp[i] = dp[i - 1]  # + dp[i - 2] - 1  <- 마지막까지 생각 못한 부분  반례)121074110
print(dp)
print(dp[length - 1] % 1000000)

#
# 다른분 블로그에서 본 간단한 코드
#
# code = [0]
# code += list(input())
#
# if code[1] == '0':
#     print(0)
#     exit(0)
#
# length = len(code)
# dp = [0] * length
# dp[0] = dp[1] = 1
#
# for i in range(2, length):
#     first = int(code[i])
#     tenth = int(code[i - 1]) * 10 + int(code[i])
#     if first > 0:
#         dp[i] += dp[i - 1]
#     if 10 <= tenth <= 26:
#         dp[i] += dp[i - 2]
#
# print(dp[length - 1] % 1000000)
