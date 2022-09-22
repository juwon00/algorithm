n = int(input())
store = n
count = 1

while True:
        
    left = int(store / 10)
    right = int(store % 10)

    second_left = right
    second_right = int((left + right) % 10)
    
    new_num = second_left * 10 + second_right
    
    if new_num != n:
        count = count + 1
        store = new_num
        continue
    else:
        break

print(count)