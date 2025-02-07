# li = []
# for i in range(1, 6):
#     print(i)
#     nPr = list(permutations(alphabet, i))
#     print(nPr)
#     for words in nPr:
#         print(words)
#         tmp = ""
#         for word in words:
#             print(word)
#             tmp += word
#         li.append(tmp)
# print(li)
#
# li.sort()
# print(li)

def solution(word):
    answer = 0
    alphabet = ["A", "E", "I", "O", "U"]

    li = []
    for alpa1 in alphabet:
        li.append(alpa1)
        for alpa2 in alphabet:
            li.append(alpa1 + alpa2)
            for alpa3 in alphabet:
                li.append(alpa1 + alpa2 + alpa3)
                for alpa4 in alphabet:
                    li.append(alpa1 + alpa2 + alpa3 + alpa4)
                    for alpa5 in alphabet:
                        li.append(alpa1 + alpa2 + alpa3 + alpa4 + alpa5)
    li.sort()
    for i in range(len(li)):
        if li[i] == word:
            answer = i + 1
            break
    return answer

word = "I"
print(solution(word))