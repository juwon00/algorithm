def solution(tickets):
    answer = []

    tickets.sort(key=lambda x: (x[0], x[1]))
    visited = [False] * len(tickets)
    print(tickets)

    def dfs(start, path):
        print(start, path)
        if len(path) == len(tickets) + 1:
            print("find")
            print()
            answer.append(path)
            return path

        for j in range(len(tickets)):
            if tickets[j][0] == start and not visited[j]:
                print(tickets[j], j)
                visited[j] = True
                dfs(tickets[j][1], path + [tickets[j][1]])
                visited[j] = False

    dfs("ICN", ["ICN"])

    # 중복을 생각하지 못해서 처음 bfs로 푼 풀이 - dfs로 수정
    #
    # q = deque()
    # q.append("ICN")
    # while q:
    #     now = q.popleft()
    #     print(now, tickets)
    #     for i in range(len(tickets)):
    #         if now == tickets[i][0]:
    #             print("go")
    #             answer.append(tickets[i][1])
    #             q.append(tickets[i][1])
    #             tickets.pop(i)
    #             break

    print(answer[0])
    return answer[0]


tickets = [["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"],
           ["BBB", "AAA"]]
solution(tickets)
