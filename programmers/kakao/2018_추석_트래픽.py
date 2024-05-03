def solution(lines):
    answer = 0

    time_line = []

    for line in lines:
        T = line.split(" ")[2]
        T = T[:len(T) - 1]
        print(T)
        et = line.split(" ")[1].split(":")
        print(et[0], et[1], et[2])
        end_time = float(et[0]) * 60 * 60 + float(et[1]) * 60 + float(et[2])
        print(end_time)
        start_time = round(end_time - float(T) + float(0.001), 3)  # 부동수소점? 때문에 round( , 3) 해줘야 됨
        print(start_time)                                          # 다음부터는 소수점으로 계산하지 말고 1000곱해서 하면 편할듯
        print()
        tmp = [start_time, end_time]
        time_line.append(tmp)
    time_line.sort(key=lambda x: x[1])
    print(time_line)

    for i in range(len(time_line)):
        cnt = 1
        print("i =", i)
        for j in range(i + 1, len(time_line)):
            print(i, j)
            if -1 < round(time_line[i][1] - time_line[j][0], 3): # 부동수소점? 때문에 round( , 3) 해줘야 됨
                print(time_line[i][1], time_line[j][0], round(time_line[i][1] - time_line[j][0], 3))
                cnt += 1
        answer = max(answer, cnt)
        print(cnt)
        print()

    return answer


lines = [
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]
answer = solution(lines)
print("answer:", answer)
