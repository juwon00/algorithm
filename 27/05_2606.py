n = int(input())
pair_num = int(input())

pair_li = list()

for i in range(pair_num):
    pair = list(map(int, input().split()))
    pair_li.append(pair)


print(pair_li)