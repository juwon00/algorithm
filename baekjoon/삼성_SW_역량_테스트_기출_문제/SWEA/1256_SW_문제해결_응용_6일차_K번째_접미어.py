for t in range(int(input())):
    k = int(input())
    string = input()
    if len(string) < k:
        print(f"#{t + 1} none")
        continue
    strings = []
    for i in range(len(string)):
        strings.append(string[i:])
    strings.sort()
    # print(strings)
    # print("k", k)
    print(f"#{t + 1} {strings[k - 1]}")
