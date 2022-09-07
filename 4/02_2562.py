li = list()
max = -1

for i in range(9):
    a = int(input())
    li.append(a)

for i in range(9):
    if max < li[i]:
        max = li[i]
        how_many = i + 1
        
print(max)
print(how_many)