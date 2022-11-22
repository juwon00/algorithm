import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(input())

k = K
stack = list()

#! 아래 주석은 내 코드 시간초과가 난다 왜??
# for i in num:

#     if not stack:
#         stack.append(i)
#         continue
    
#     for j in reversed(stack):
#         if j < i and k > 0:
#             k -= 1
#             stack.pop()

#     stack.append(i)

for i in range(N):
    while k > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        k -= 1
    stack.append(num[i])
    
        
print(''.join(stack[:N-K]))