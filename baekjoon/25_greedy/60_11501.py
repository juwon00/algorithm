test = int(input())

for _ in range(test):

    day = int(input())

    stock = list(map(int, input().split()))

    count = 0
    max_price = 0

    for i in range(len(stock) - 1, -1, -1):
        # print(i, stock[i])
        # print(max_price)
        if stock[i] > max_price:
            max_price = stock[i]
        else:
            count += max_price - stock[i]

    print(count)
