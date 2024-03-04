n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
print(arr)

word = {}
for w in arr:
    print(word)
    length = len(w) - 1
    print(w, length)
    for i in w:
        print(i)
        if i in word:
            word[i] += 10 ** length
        else:
            word[i] = 10 ** length
        length -= 1
print(word)

word = sorted(word.values(), reverse=True)
print(word)
result = 0
num = 9
for w in word:
    result += w * num
    num -= 1
print(result)
