def check_3_line(char):
    # 가로
    if (game[0] == char and game[1] == char and game[2] == char) or (
            game[3] == char and game[4] == char and game[5] == char) or (
            game[6] == char and game[7] == char and game[8] == char):
        return True
    # 세로
    if (game[0] == char and game[3] == char and game[6] == char) or (
            game[1] == char and game[4] == char and game[7] == char) or (
            game[2] == char and game[5] == char and game[8] == char):
        return True
    # 대각선
    if (game[0] == char and game[4] == char and game[8] == char) or (
            game[2] == char and game[4] == char and game[6] == char):
        return True
    return False


while True:
    print()
    game = input()
    if game == "end":
        break
    game = list(game)
    print(game)
    x_cnt = game.count('X')
    o_cnt = game.count('O')
    x_3_line = check_3_line('X')
    o_3_line = check_3_line('O')
    print('x_cnt', x_cnt)
    print('o_cnt', o_cnt)
    print('x_3_line', x_3_line)
    print('o_3_line', o_3_line)

    if x_cnt < o_cnt or x_cnt - o_cnt > 1:
        print("invalid")
        continue

    if x_cnt - o_cnt == 1 and o_3_line:
        print("invalid")
        continue

    if "." in game and not x_3_line and not o_3_line:
        print("invalid")
        continue

    if x_3_line and o_3_line:
        print("invalid")
        continue

    if (x_3_line and x_cnt - o_cnt != 1) or (o_3_line and x_cnt - o_cnt != 0):
        print("invalid")
        continue

    print("valid")