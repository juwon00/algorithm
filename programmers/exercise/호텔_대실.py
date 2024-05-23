from collections import deque


def solution(book_time):
    answer = 0

    book_times = []
    for time in book_time:
        tmp = []
        print(time)
        start = time[0].split(":")
        tmp.append(int(start[0]) * 60 + int(start[1]))
        end = time[1].split(":")
        tmp.append(int(end[0]) * 60 + int(end[1]) + 10)
        book_times.append(tmp)
        print(book_times)
    book_times.sort(key=lambda x: (x[1], x[0]))
    print(book_times)
    print()

    q = deque(book_times)
    print(q)

    while q:

        now = q.popleft()
        print("now", now)

        nt = now[1]
        for i in range(len(q)):
            next_time = q.popleft()
            print("next", next_time, nt)
            if nt > next_time[0]:
                print("append", next_time)
                q.append(next_time)
                print()
            else:
                nt = next_time[1]

        print("finish", q)
        print()
        answer += 1
    return answer


book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
# book_time = [["00:05", "00:06"], ["00:16", "00:17"], ["00:16", "00:18"]]
answer = solution(book_time)
print("answer", answer)
