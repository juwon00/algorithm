def solution(new_id):
    answer = ''

    # 1
    new_id1 = new_id.lower()
    print("new_id1", new_id1)

    # 2
    new_id2 = ""
    for id in new_id1:
        if (48 <= ord(id) <= 57) or (97 <= ord(id) <= 122) or id in ["-", "_", "."]:
            new_id2 += id
    print("new_id2", new_id2)

    # 3
    new_id3 = ""
    for i in range(len(new_id2)):
        print(new_id2[i])
        if new_id2[i] == "." and len(new_id3) == 0:
            new_id3 += new_id2[i]
        elif new_id2[i] == "." and new_id3[-1] == ".":
            continue
        else:
            new_id3 += new_id2[i]
    print("new_id3", new_id3)

    # 4
    if len(new_id3) > 0:
        if new_id3[0] == ".":
            new_id4 = new_id3[1:]
        elif new_id3[-1] == ".":
            new_id4 = new_id3[:-1]
        elif new_id3[0] == "." and new_id3[-1] == ".":
            new_id4 = new_id3[1:-1]
        else:
            new_id4 = new_id3
    else:
        new_id4 = new_id3
    print("new_id4", new_id4)

    # 5
    if new_id4 == "":
        new_id5 = "a"
    else:
        new_id5 = new_id4
    print("new_id5", new_id5)

    # 6
    if len(new_id5) > 15:
        new_id6 = new_id5[:15]
    else:
        new_id6 = new_id5
    if new_id6[-1] == ".":
        new_id6 = new_id6[:-1]
    print("new_id6", new_id6)

    # 7
    if len(new_id6) == 2:
        new_id7 = new_id6 + new_id6[1]
    elif len(new_id6) == 1:
        new_id7 = new_id6 * 3
    else:
        new_id7 = new_id6
    print("new_id7", new_id7)

    answer = new_id7
    return answer


new_id = "...!@BaT#*..y.abcdefghijklm"
answer = solution(new_id)
print("answer:", answer)
