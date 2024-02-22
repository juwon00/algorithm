
#  4 2 3 1 3 1
#  2 3 1 4 1 4
#  3 1 4 2 4 2
#  1 4 2 3 2 3

k = int(input())

melon = []
direction = []
length = []
for _ in range(6):
    x = []
    a, b = map(int, input().split())
    direction.append(a)
    length.append(b)
    x.append(a)
    x.append(b)
    melon.append(x)

# print(direction)
# print(length)
# print(melon)

if direction.count(1) == 2 and direction.count(3) == 2:

    main_index = direction.index(2)
    sub_index = main_index - 1 if main_index - 1 >= 0 else 5

    x_index = main_index + 2 if main_index + 2 <= 5 else main_index - 4
    y_index = main_index + 3 if main_index + 3 <= 4 else main_index - 3

    size = length[main_index] * length[sub_index] - length[x_index] * length[y_index]

    print(size * k)

elif direction.count(1) == 2 and direction.count(4) == 2:

    main_index = direction.index(3)
    sub_index = main_index - 1 if main_index - 1 >= 0 else 5

    x_index = main_index + 2 if main_index + 2 <= 5 else main_index - 4
    y_index = main_index + 3 if main_index + 3 <= 4 else main_index - 3

    size = length[main_index] * length[sub_index] - length[x_index] * length[y_index]

    print(size * k)

elif direction.count(2) == 2 and direction.count(4) == 2:

    main_index = direction.index(1)
    sub_index = main_index - 1 if main_index - 1 >= 0 else 5

    x_index = main_index + 2 if main_index + 2 <= 5 else main_index - 4
    y_index = main_index + 3 if main_index + 3 <= 4 else main_index - 3

    size = length[main_index] * length[sub_index] - length[x_index] * length[y_index]

    print(size * k)

elif direction.count(2) == 2 and direction.count(3) == 2:

    main_index = direction.index(4)
    sub_index = main_index - 1 if main_index - 1 >= 0 else 5

    x_index = main_index + 2 if main_index + 2 <= 5 else main_index - 4
    y_index = main_index + 3 if main_index + 3 <= 4 else main_index - 3

    size = length[main_index] * length[sub_index] - length[x_index] * length[y_index]

    print(size * k)


