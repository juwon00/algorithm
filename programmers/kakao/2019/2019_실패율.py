def solution(N, stages):
    answer = []
    print(N, stages)

    max_clear = N + 2
    counter = {}
    for i in range(1, max_clear):
        counter[i] = 0
    for stage in stages:
        counter[stage] += 1
    print(counter)

    prefix_sum = [0] * (max_clear + 1)
    for i in range(max_clear - 1, 0, -1):
        prefix_sum[i] = prefix_sum[i + 1] + counter[i]
    print(prefix_sum)

    result = []
    for i in range(1, N + 1):
        if prefix_sum[i] != 0:
            result.append([counter[i] / prefix_sum[i], i])
        else:
            result.append([0, i])
    print(result)
    result.sort(key=lambda x: (-x[0], x[1]))
    print(result)

    for i in range(len(result)):
        answer.append(result[i][1])

    return answer


N = 10
stages = [1, 2]
answer = solution(N, stages)
print("answer:", answer)
