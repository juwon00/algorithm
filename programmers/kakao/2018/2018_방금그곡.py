def solution(m, musicinfos):
    answer = ''
    answers = []

    for index, music in enumerate(musicinfos):
        ms = music.split(",")
        start, end, title, melody = ms[0].split(":"), ms[1].split(":"), ms[2], ms[3]
        start = int(start[0]) * 60 + int(start[1])
        end = int(end[0]) * 60 + int(end[1])
        print(start, end, end - start, title, melody)

        melodys = []
        for i in range(len(melody)):
            if melody[i] == '#':
                continue
            if i == len(melody) - 1:
                melodys.append(melody[i])
            elif melody[i + 1] == '#':
                melodys.append(melody[i] + melody[i + 1])
            else:
                melodys.append(melody[i])
        print(melodys)

        while True:
            if len(melodys) >= end - start:
                break
            melodys.extend(melodys)
        melodys = melodys[:end - start]
        print(melodys)

        ms = []
        for i in range(len(m)):
            if m[i] == '#':
                continue
            if i == len(m) - 1:
                ms.append(m[i])
            elif m[i + 1] == '#':
                ms.append(m[i] + m[i + 1])
            else:
                ms.append(m[i])
        print(ms)

        for i in range(len(melodys) - len(ms) + 1):
            if ms == melodys[i:i + len(ms)]:
                print("yes", i)
                answers.append([int(end - start), index, title])
                break

    print(answers)
    answers.sort(key=lambda x: (-x[0], x[1]))
    print(answers)

    if len(answers) == 0:
        answer += "(None)"
    else:
        answer += answers[0][2]
    return answer


m = "ABC"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:14,WORLD,ABCDEF"]
answer = solution(m, musicinfos)
print("answer:", answer)
