s = input()
boom = input()
boom_len = len(boom)

stack = []
for i in range(len(s)):
    stack.append(s[i])
    print(stack)
    print(''.join(stack[-boom_len:]), boom)
    if ''.join(stack[-boom_len:]) == boom:
        print("find")
        for _ in range(boom_len):
            stack.pop()
    print()

if stack:
    print(''.join(stack))
else:
    print("FRULA")