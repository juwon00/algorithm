def solution(record):
    answer = []

    nicks = {}
    situation = []
    for r in record:
        if len(r.split(" ")) == 3:
            condition, user_id, nickname = r.split(" ")
            nicks[user_id] = nickname
            if condition == "Enter":
                situation.append((user_id, condition))
        else:
            condition, user_id = r.split(" ")
            situation.append((user_id, condition))

        print(condition, user_id)
    print(nicks)
    print(situation)

    for s in situation:
        print(s)
        if s[1] == "Enter":
            answer.append(nicks[s[0]] + "님이 들어왔습니다.")
        elif s[1] == "Leave":
            answer.append(nicks[s[0]] + "님이 나갔습니다.")

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
answer = solution(record)
print("answer:", answer)
