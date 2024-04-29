def solution(n, arr1, arr2):
    map1 = []
    map2 = []

    for a1 in arr1:
        print(a1)
        binary = format(a1, 'b')
        print(binary)
        while len(binary) < n:
            binary = "0" + binary
        map1.append(binary)
        print(binary)
        print()

    for a2 in arr2:
        print(a2)
        binary = format(a2, 'b')
        print(binary)
        while len(binary) < n:
            binary = "0" + binary
        map2.append(binary)
        print(binary)
        print()

    print(map1)
    print(map2)

    answer = [] * n
    print(answer)

    for i in range(n):
        tmp = ""
        for j in range(n):
            if map1[i][j] == '1' or map2[i][j] == '1':
                tmp += "#"
            else:
                tmp += " "
        print(tmp)
        answer.append(tmp)

    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
answer = solution(n, arr1, arr2)
print("answer:", answer)
