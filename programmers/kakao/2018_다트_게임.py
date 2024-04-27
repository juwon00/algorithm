def solution(dartResult):
    answer = 0
    tmp1 = 0
    tmp2 = 0
    flag = False

    for i in range(len(dartResult)):
        print(dartResult[i])
        print(tmp1, tmp2)

        if flag:
            flag = False
            continue

        if dartResult[i].isdigit() and dartResult[i + 1].isdigit():
            tmp2 = tmp1
            answer += tmp1
            tmp1 = int(dartResult[i:i + 2])
            flag = True

        elif dartResult[i].isdigit():
            tmp2 = tmp1
            answer += tmp1
            tmp1 = int(dartResult[i])

        elif dartResult[i] == "D":
            tmp1 = tmp1 * tmp1

        elif dartResult[i] == "T":
            tmp1 = tmp1 * tmp1 * tmp1

        elif dartResult[i] == "*":
            print("*")
            tmp1 = tmp1 * 2
            answer -= tmp2
            answer += tmp2 * 2

        elif dartResult[i] == "#":
            print("#")
            tmp1 = -tmp1
        print("answer", answer)
        print()
    answer += tmp1
    return answer


dartResult = "1S2D*3T"
answer = solution(dartResult)
print("answer", answer)
