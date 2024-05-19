from collections import deque


def solution(board):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    lenb = len(board)

    # 외벽
    nboard = [[1] * (lenb + 2) for _ in range(lenb + 2)]
    for i in range(lenb):
        for j in range(lenb):
            nboard[i + 1][j + 1] = board[i][j]

    q = deque()
    q.append([(1, 1), (1, 2), 0])
    ch_set = set([((1, 1), (1, 2))])

    while q:
        s1, s2, dist = q.popleft()
        print(">>", s1, s2, dist)

        if s1 == (lenb, lenb) or s2 == (lenb, lenb):
            return dist

        tmp = []

        # 상하좌우
        for i in range(4):
            s1_i = s1[0] + dx[i]
            s1_j = s1[1] + dy[i]
            s2_i = s2[0] + dx[i]
            s2_j = s2[1] + dy[i]
            if nboard[s1_i][s1_j] == 0 and nboard[s2_i][s2_j] == 0:
                tmp.append(((s1_i, s1_j), (s2_i, s2_j)))

        # 가로 -> 세로
        if s1[0] == s2[0]:
            # 위로 회전, 아래로 회전
            for i in [1, -1]:
                if nboard[s1[0] + i][s1[1]] == 0 and nboard[s2[0] + i][s2[1]] == 0:
                    tmp.append((s1, (s1[0] + i, s1[1])))
                    tmp.append((s2, (s2[0] + i, s2[1])))
        # 세로 -> 가로
        else:
            # 오른쪽으로 회전, 왼쪽으로 회전
            for i in [-1, 1]:
                if nboard[s1[0]][s1[1] + i] == 0 and nboard[s2[0]][s2[1] + i] == 0:
                    tmp.append(((s1[0], s1[1] + i), s1))
                    tmp.append(((s2[0], s2[1] + i), s2))

        # ch_set에 해당 좌표가 없으면 q에 추가
        for pset in tmp:
            if pset not in ch_set:
                q.append((*pset, dist + 1))
                ch_set.add(pset)


board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
answer = solution(board)
print("answer:", answer)
