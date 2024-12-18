import sys

input = sys.stdin.readline

m = int(input())
bit = 0
for _ in range(m):
    tmp = input().rstrip().split(" ")
    if tmp[0] == 'all':
        print("all")
        bit = (1 << 21) - 1
        print(bin(bit))
    elif tmp[0] == "empty":
        print("empty")
        bit = 0
        print(bin(bit))
    else:
        num = int(tmp[1])

        if tmp[0] == "add":
            print("add")
            print(num)
            bit = bit | (1 << num)
            print(bin(bit))
        elif tmp[0] == "remove":
            print("remove")
            print(num)
            bit = bit & ~(1 << num)
            print(bin(bit))
        elif tmp[0] == "check":
            print("check")
            print(num)
            print(bin(bit))
            print(bin(bit & (1 << num)))
            if bit & (1 << num):
                print(">> 1")
            else:
                print(">> 0")
        elif tmp[0] == "toggle":
            print("toggle")
            print(num)
            bit = bit ^ (1 << num)
            print(bin(bit))

    print()
