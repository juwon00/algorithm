sum = int(input())
total_number = int(input())

cal = 0
for i in range(total_number):
    price,number = input().split()
    price = int(price)
    number = int(number)
    
    cal = cal + (price * number)
    
if sum == cal:
    print('Yes')
else:
    print('No')