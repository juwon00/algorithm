def change_to_hh_mm(time):
    hour = time // 60
    minute = time % 60
    answer = ''
    if hour < 10:
        answer += "0" + str(hour)
    else:
        answer += str(hour)
    answer += ":"

    if minute < 10:
        answer += "0" + str(minute)
    else:
        answer += str(minute)
    print(answer)

    return answer


def solution(n, t, m, timetable):
    print(9 * 60)

    crews = [int(time.split(":")[0]) * 60 + int(time.split(":")[1]) for time in timetable]
    crews.sort()
    print("crews", crews)

    busstop = [540 + x * t for x in range(n)]
    print("bus  ", busstop)

    index = 0  # crews에서 누가 탈 순서인지
    for i in range(len(busstop)):
        print(i, busstop[i])
        cnt = 0  # 버스에 몇명 탔는지
        while index < len(crews) and cnt < m and busstop[i] >= crews[index]:
            cnt += 1
            index += 1
            print(cnt, index)

        print("index", index, cnt)
        if i == len(busstop) - 1:  # 마지막 버스
            print("last")
            if cnt == m:  # 자리가 없으면 마지막 crew보다 1분 빨리 온다
                print("full")
                print(crews[index - 1] - 1)
                return change_to_hh_mm(crews[index - 1] - 1)
            else:  # 자리가 남으면 버스 시간에 맞춰서 온다
                print("ok")
                print(busstop[i])
                return change_to_hh_mm(busstop[i])


n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]
answer = solution(n, t, m, timetable)
print("answer:", answer)
