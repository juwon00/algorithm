from collections import defaultdict

n = int(input())
l = [(input(), i) for i in range(n)]
l.sort()
print(l)
prefix_dict = defaultdict(set)
prefix_list = []
max_cnt = 0

for i in range(n - 1):
    w1, w2 = l[i][0], l[i + 1][0]
    print(w1, w2)
    prefix = ""
    cnt = 0
    for j in range(min(len(w1), len(w2))):
        print(j, w1[j], w2[j])
        if w1[j] != w2[j]:
            prefix = w1[:j]
            break
        cnt += 1
        prefix = w1[:j]
    print("prefix:", prefix)
    print("cnt:", cnt)

    if cnt < max_cnt:
        continue

    if cnt > max_cnt:
        prefix_list = []
        max_cnt = cnt

    prefix_list.append(prefix)
    prefix_dict[prefix].add((l[i][1], w1))
    prefix_dict[prefix].add((l[i + 1][1], w2))
    print()

print(prefix_dict)
print(prefix_list)
print()

ans_len = n
ans = ""
for prefix in prefix_list:
    print(prefix)
    word1, word2 = sorted(prefix_dict[prefix])[:2]
    print(word1, word2)
    if ans_len > word1[0]:
        ans_len = word1[0]
        ans = (word1[1], word2[1])
    print()
print(ans[0])
print(ans[1])

# 6
# bc
# aa
# ab
# ba
# bd
# bb

# 처음 풀이 - 위의 반례가 존재함

# from collections import defaultdict
#
# n = int(input())
# input_word = [[input(), i] for i in range(n)]
# word_dict = defaultdict(list)
# word = sorted(input_word)
#
# max_cnt = 0
# for i in range(n - 1):
#     w1, w2 = word[i][0], word[i + 1][0]
#     x, y = 0, 0
#     length = min(len(w1), len(w2))
#     cnt = 0
#     for _ in range(length):
#         if w1[x] != w2[y]:
#             break
#         x += 1
#         y += 1
#         cnt += 1
#     if cnt >= max_cnt:
#         max_cnt = cnt
#         word_dict[max_cnt].append(sorted([word[i][1], word[i + 1][1]]))
#
# max_list = word_dict[max(word_dict.keys())]
# max_list.sort()
# i1, i2 = max_list[0][0], max_list[0][1]
# print(input_word[i1][0])
# print(input_word[i2][0])
