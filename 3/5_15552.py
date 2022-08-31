import sys

a = int(input())

for i in range(a):
    b,c = map(int,sys.stdin.readline().split())
    b = int(b)
    c = int(c)
    
    print(b+c)