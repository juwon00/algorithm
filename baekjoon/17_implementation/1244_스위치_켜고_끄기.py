def change_switch(index):
    if switch[index] == 1:
        switch[index] = 0
    else:
        switch[index] = 1


n = int(input())
switch = list(map(int, input().split()))
n_student = int(input())
print(switch)

for _ in range(n_student):
    gender, x = map(int, input().split())
    x = x - 1
    if gender == 1:
        print("male")
        for i in range(x, n, x + 1):
            print(i)
            change_switch(i)


    elif gender == 2:
        print("female")
        tmp = []
        s = 1
        tmp.append(x)
        while True:
            if x - s < 0 or x + s >= n:
                break
            if switch[x - s] == switch[x + s]:
                tmp.append(x - s)
                tmp.append(x + s)
            else:
                break
            s = s + 1
        print("tmp", tmp)
        for t in tmp:
            change_switch(t)

    print(switch)
    print()

print(*switch)

for index, s in enumerate(switch):
    print(s, end=" ")
    if (index + 1) % 20 == 0 and index != 0:
        print()
