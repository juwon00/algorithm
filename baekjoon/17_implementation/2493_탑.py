n = int(input())
top = list(map(int, input().split()))
result = [0] * n

stack = []
stack.append((0, 0))

for i, t in enumerate(top):
    print(t, i + 1)
    print(stack[-1])
    while True:
        if len(stack) > 0 and stack[-1][0] < t:
            stack.pop()
        else:
            print(stack)
            if len(stack) > 0:
                result[i] = stack[-1][1]
            stack.append((t, i + 1))
            break
    print(stack)
    print()
print(result)