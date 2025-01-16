from collections import defaultdict

for _ in range(int(input())):
    W = input()
    k = int(input())

    count_dic = defaultdict(int)
    for w in W:
        count_dic[w] += 1

    index_dic = defaultdict(list)
    for i in range(len(W)):
        if count_dic[W[i]] >= k:
            index_dic[W[i]].append(i)
    print(index_dic)

    if not index_dic:
        print(-1)
        continue

    result = []
    for key, value in index_dic.items():
        print(key, value)
        for i in range(len(value) - k + 1):
            print(i, i + k - 1)
            tmp = value[i + k - 1] - value[i] + 1
            result.append(tmp)
    print(result)
    result.sort()
    print(result[0], result[-1])
