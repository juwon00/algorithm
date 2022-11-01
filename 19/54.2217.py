
# n = int(input())

# rope_list = list()

# for _ in range(n):
#     rope = int(input())
#     rope_list.append(rope)

# rope_list.sort()

# i = 0
# while True:
#     if rope_list[i] * n < rope_list[i+1] * (n - 1):
#         i += 1
#         n -= 1
#     else:
#         result = rope_list[i] * n
#         break
    
# print(result)

#Todo 위의 코드로 했는데 오류가 나서 아래 코드로 바꿨다


n = int(input())

rope_list = list()

for _ in range(n):
    rope = int(input())
    rope_list.append(rope)

rope_list.sort(reverse=True) # 내림차순으로 정렬후

for i in range(n): # list의 i번째 수와 i+1을 곱한 리스트로 만든 후 
    rope_list[i] = rope_list[i] * (i+1)

print(max(rope_list)) # 그 중 가장 큰 값을 출력하면 된다

