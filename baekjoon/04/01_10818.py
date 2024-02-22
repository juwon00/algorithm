n = int(input())
li = list(map(int, input().split()))

top = None
bottom = None

for i in range(n):
    if top == None or top < li[i]:
        top = li[i]
    if bottom == None or bottom > li[i]:
        bottom = li[i]
        
print(bottom, top)
