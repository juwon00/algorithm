a = int(input())

for i in range(a-1,-1,-1):
    for j in range(a):
        if j >= i:
            print('*',end='')
        elif j < i:
            print(" ", end='')
    print('')
