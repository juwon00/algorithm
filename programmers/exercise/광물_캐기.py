def solution(picks, minerals):
    answer = 0
    pick_cnt = sum(picks)
    minerals = minerals[:5 * pick_cnt]
    print(minerals)

    mineral_num = []
    tmp = {"d": 0, "i": 0, "s": 0}
    for i, mineral in enumerate(minerals):
        if mineral == "diamond":
            tmp["d"] += 1
        elif mineral == "iron":
            tmp["i"] += 1
        elif mineral == "stone":
            tmp["s"] += 1
        if i % 5 == 4 and i != 0:
            mineral_num.append(tmp)
            tmp = {"d": 0, "i": 0, "s": 0}
    if tmp != {"d": 0, "i": 0, "s": 0}:
        mineral_num.append(tmp)

    mineral_num.sort(key=lambda x: (x["d"], x["i"], x["s"]), reverse=True)
    print(mineral_num)

    for i in range(len(mineral_num)):
        print(mineral_num[i])
        if picks[0] > 0:
            answer += mineral_num[i]["d"] * 1 + mineral_num[i]["i"] * 1 + mineral_num[i]["s"] * 1
            picks[0] -= 1
        elif picks[1] > 0:
            answer += mineral_num[i]["d"] * 5 + mineral_num[i]["i"] * 1 + mineral_num[i]["s"] * 1
            picks[1] -= 1
        elif picks[2] > 0:
            answer += mineral_num[i]["d"] * 25 + mineral_num[i]["i"] * 5 + mineral_num[i]["s"] * 1
        print(answer)
        print()

    return answer


picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
answer = solution(picks, minerals)
print("answer:", answer)
