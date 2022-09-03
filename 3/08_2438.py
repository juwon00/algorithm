a = int(input())

for i in range(a):
    for j in range(a):
        if j <= i:
            print("*",end='')
    print('')
    
    
# 다른분 플이    
# for i in range(1,a+1):
#     print("*" * i)
