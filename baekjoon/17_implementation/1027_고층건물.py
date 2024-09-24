n = int(input())
building = list(map(int, input().split()))
print(n)
print(building)
result = 0

for x1, y1 in enumerate(building):

    count = 0
    right_gradient = 0
    left_gradient = 0
    print(x1, y1)
    print("=====")
    left_list = []

    for x2, y2 in enumerate(building):
        if x1 == x2:
            continue
        print(x2, y2)

        if x1 < x2:
            print("right")
            if x2 - x1 == 1:
                print("find")
                right_gradient = y2 - y1
                count += 1
            else:
                tmp = (y2 - y1) / (x2 - x1)
                if tmp > right_gradient:
                    print("find")
                    right_gradient = tmp
                    count += 1

        elif x1 > x2:
            print("left")
            left_list.append((x2, y2))


    print(left_list)
    for i in range(len(left_list) - 1, -1, -1):
        x2, y2 = left_list[i]
        print(x2, y2, left_gradient)
        if x1 - x2 == 1:
            print("find 1")
            left_gradient = y1 - y2
            count += 1
        else:
            tmp = (y1 - y2) / (x1 - x2)
            print("tmp", tmp)
            if tmp < left_gradient:
                print("find 2")
                left_gradient = tmp
                count += 1

    print("count", count)
    print()

    result = max(result, count)

print("result", result)