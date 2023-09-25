from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    important = deque(list(map(int, input().split())))

    result = 0

    while important:
        # print()
        # print("start")
        # print(important, M)

        left = important.popleft()
        # print("left :", left)

        if important.__len__() == 0:
            result += 1
            if M == 0:
                break

        if left >= max(important):
            # print("M :", M)
            result += 1
            if M == 0:
                break
            M -= 1

        else:
            # print("M :", M)
            important.append(left)
            if M == 0:
                M = important.__len__() - 1
            else:
                M -= 1
            # print(important, M)

    print(result)
