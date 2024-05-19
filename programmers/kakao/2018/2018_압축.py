def solution(msg):
    answer = []
    msg_size = len(msg)
    print(msg, msg_size)
    lzw = ["0"]
    for i in range(65, 91):
        lzw.append(chr(i))
    print(lzw)

    i = 0
    while True:
        if i >= msg_size:
            break
        print(i)

        tmp = msg[i]
        while True:

            if i >= msg_size - 1:
                break

            print(i, tmp)
            if tmp + msg[i + 1] in lzw:
                print("long")
                tmp += msg[i + 1]
                i += 1
            else:
                print("append", tmp + msg[i + 1])
                lzw.append(tmp + msg[i + 1])
                break

        print(lzw.index(tmp))
        answer.append(lzw.index(tmp))
        print()
        i += 1

    return answer


msg = "TOBEORNOTTOBEORTOBEORNOT"
answer = solution(msg)
print("answer:", answer)
