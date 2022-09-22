a = int(input())

for i in range(1,a+1):
    b,c = input().split()
    b = int(b)
    c = int(c)
    
    sum = b + c
    
    print(f"Case #{i}: {b} + {c} = {sum}")