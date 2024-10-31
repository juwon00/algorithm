n = int(input())
height = [0] * 1001
highest = 0
h_idx = 0
end_idx = 0

for _ in range(n):
    l, h = map(int, input().split())
    height[l] = h
    if highest < h:
        highest = h
        h_idx = l
    end_idx = max(end_idx, l)

print(highest, h_idx)
print(end_idx)
print()

result = 0
stack = []
for i in range(h_idx + 1):
    print(i)
    if not stack:
        stack.append(height[i])
    else:
        if stack[-1] < height[i]:
            stack.pop()
            stack.append(height[i])
    result += stack[-1]
    print(stack)
    print(result)
    print()

stack = []
for j in range(end_idx, h_idx, -1):
    print(j)
    if not stack:
        stack.append(height[j])
    else:
        if stack[-1] < height[j]:
            stack.pop()
            stack.append(height[j])
    result += stack[-1]
    print(stack)
    print(result)
    print()
print(result)
