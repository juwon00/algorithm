import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
weight = list(map(int, input().split()))

crane.sort(reverse=True)
weight.sort(reverse=True)

if crane[0] < weight[0]:
    print(-1)
    sys.exit()

result = 0
while weight:

    for c in crane:
        # print("c", c)

        for w in weight:
            # print("w", w)

            if c >= w:
                # print(c, w)
                weight.remove(w)
                break

    result += 1
    # print("w", weight)

print(result)
