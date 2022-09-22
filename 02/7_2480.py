a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

li = list()
li.append(a)
li.append(b)
li.append(c)
li.sort(reverse=True)

if li[0] == li[1] and li[1] == li[2]:
    print(10000 + li[0] * 1000 )
elif li[0] == li[1]:
    print(1000 + li[0] * 100)
elif li[0] == li[2]:
    print(1000 + li[0] * 100)    
elif li[1] == li[2]:
    print(1000 + li[1] * 100)
else:
    print(li[0] * 100)