t = int(input())
for test in range(t):
    n = int(input())
    graph = list(map(int, input().split()))
    pos, weight = graph[:n], graph[n:]
    print(pos)
    print(weight)

    result = []
    for i in range(1, n):
        print(i)
        low, high = pos[i - 1], pos[i]

        while high - low > 1 / (10 ** 12):
            print("low, high", low, high)
            mid = (low + high) / 2
            print(mid)
            left, right = 0, 0
            for k in range(n):
                force = weight[k] / (mid - pos[k]) ** 2
                print("force", force)
                # 왼쪽에서 잡아당기는 인력인 경우
                if pos[k] < mid:
                    left += force
                else:
                    right += force

            print("left, right", left, right)
            # 왼쪽에서 잡아당기는 인력이 더 크면
            if left > right:
                low = mid
            # 오른쪽에서 잡아당기는 인력이 더 크면
            else:
                high = mid
            print()
        result.append(mid)
    print(result)
    print("#" + str(test + 1), end=" ")
    for i in range(len(result)):
        print(f"{result[i]:.10f}", end=" ")
