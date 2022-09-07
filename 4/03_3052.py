li = list()
result_li = list()

for i in range(10):
    a = int(input())
    li.append(a%42)
    
for i in li:
    if i not in result_li:
        result_li.append(i)
        
n = len(result_li)

print(n)