import sys

input = sys.stdin.readline

data = input()
q = int(input())

prefix_str = [[0] * 26 for _ in range(len(data))]

for i in range(len(data)):
    for j in range(26):
        if ord(data[i]) - 97 == j:  # 한번 나왔으니 누적합 +1
            prefix_str[i][j] = prefix_str[i - 1][j] + 1
        else:  # 안나왔으니 그대로
            prefix_str[i][j] = prefix_str[i - 1][j]

for _ in range(q):
    a, b, c = input().split()
    if int(b) == 0:  # 0~c 까지 ->  [c]
        print(prefix_str[int(c)][ord(a) - 97])
    else:  # b~c 까지 ->  [c] - [b-1]
        print(prefix_str[int(c)][ord(a) - 97] - prefix_str[int(b) - 1][ord(a) - 97])

# data = input().rstrip()
# prefix_str = [""]
# sum_value = ""
# for i in range(len(data)):
#     sum_value += data[i]
#     prefix_str.append(sum_value)
# print(prefix_str)
#
# q = int(input())
# for _ in range(q):
#     a, b, c = input().split()
#     b = int(b)
#     c = int(c)
#     print(data, a, b, c)
#     print(prefix_str[c + 1], prefix_str[b])
#     word = prefix_str[c + 1].lstrip(prefix_str[b])
#     print(word)
#     print(word.count(a))
