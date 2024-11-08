dic = {"0001101": "0", "0011001": "1", "0010011": "2", "0111101": "3", "0100011": "4", "0110001": "5", "0101111": "6",
       "0111011": "7", "0110111": "8", "0001011": "9"}

T = int(input())
for i in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [input() for _ in range(n)]

    one_height = 0
    one_index = 0
    for x in range(n):
        for y in range(m):
            print(graph[x][y], end=' ')
            if graph[x][y] == "1":
                one_index = y
        print()
        if one_index != 0:
            one_height = x
            break
    left = one_index - 56 + 1
    right = one_index + 1
    print(one_height, left, right)
    code = graph[one_height][left:right]
    print(code)

    code_str = ""
    for j in range(0, 56, 7):
        print(j, j + 7)
        print(code[j:j + 7])
        code_str += dic[code[j:j + 7]]
    print(code_str)
    odd = 0
    even = 0
    sum_result = 0
    for k in range(8):
        if k % 2 == 0:
            odd += int(code_str[k])
            sum_result += int(code_str[k])
        else:
            even += int(code_str[k])
            sum_result += int(code_str[k])
    print(odd, even)
    print(odd * 3 + even)
    if (odd * 3 + even) % 10 == 0:
        print(f"#{i} {sum_result}")
    else:
        print(f"#{i} {0}")
