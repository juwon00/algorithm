def dfs(visited, num, number, first):
    print(number, first)
    for x in num[number]:
        print(x)
        if x == first:
            print("find")
            return True
        if not visited[x]:
            visited[x] = True
            if dfs(visited, num, x, first):
                return True
    return False

n = int(input())
num = {i: [] for i in range(1, n + 1)}

for i in range(n):
    tmp = int(input())
    num[tmp].append(i + 1)
print(num)

result = []
for number in num.keys():
    print("====", number)
    visited = [False] * (n + 1)
    if dfs(visited, num, number, number):
        result.append(number)

print()
print(len(result))
for r in result:
    print(r)
