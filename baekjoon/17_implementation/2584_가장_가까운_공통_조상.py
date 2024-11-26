for t in range(int(input())):
    n = int(input())
    p_list = [0 for _ in range(n + 1)]
    for _ in range(n - 1):
        p, c = map(int, input().split())
        p_list[c] = p
    print(p_list)
    a, b = map(int, input().split())
    print(a, b)
    a_parent = [a]
    b_parent = [b]

    while p_list[a]:
        a_parent.append(p_list[a])
        a = p_list[a]

    while p_list[b]:
        b_parent.append(p_list[b])
        b = p_list[b]

    print(a_parent)
    print(b_parent)

    a_level = len(a_parent) - 1
    b_level = len(b_parent) - 1
    print(a_level)
    print(b_level)

    answer = -1
    while a_parent[a_level] == b_parent[b_level]:
        answer = a_parent[a_level]
        a_level -= 1
        b_level -= 1
    print(answer)
    print()
