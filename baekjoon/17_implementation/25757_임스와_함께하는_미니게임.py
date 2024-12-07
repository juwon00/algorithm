n, game = input().split(" ")
n = int(n)
print(n, game)
nickname = set(input() for _ in range(n))
print(nickname)
if game == "Y":
    print(len(nickname))
elif game == "F":
    print(len(nickname) // 2)
elif game == "O":
    print(len(nickname) // 3)
