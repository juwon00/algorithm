def solution(answers):
    result = []

    a1 = [1, 2, 3, 4, 5] * 2000
    a2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    print(answers)
    a1_correct, a2_correct, a3_correct = 0, 0, 0

    for i in range(len(answers)):
        if answers[i] == a1[i]:
            a1_correct += 1
        if answers[i] == a2[i]:
            a2_correct += 1
        if answers[i] == a3[i]:
            a3_correct += 1

    print(a1_correct, a2_correct, a3_correct)

    max_correct = max(a1_correct, a2_correct, a3_correct)

    if max_correct == a1_correct:
        result.append(1)
    if max_correct == a2_correct:
        result.append(2)
    if max_correct == a3_correct:
        result.append(3)
    return result


answers = [1, 3, 2, 4, 2]
solution(answers)
