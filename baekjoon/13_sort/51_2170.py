# import sys
#
# n = int(sys.stdin.readline())
#
# line = []
# for i in range(n):
#     line.append(list(map(int, sys.stdin.readline().split())))
#
# line.sort(key=lambda x: (x[0], x[1]))
#
# result = 0
# for i in range(n):
#
#     if i < n-1:
#         if line[i][1] > line[i+1][0]: # 튀어나오거나 밖에있을때
#             line[i+1][0] = line[i][1]
#
#     if i > 0:
#         if line[i][0] > line[i-1][0] and line[i][1] < line[i-1][1]: # 안에 속할때
#             line[i][0], line[i][1] = line[i-1][0], line[i-1][1]
#
#             if i < n-1:
#                 if line[i][1] > line[i + 1][0]:
#                     line[i + 1][0] = line[i][1]
#
#             continue
#
#     result += line[i][1] - line[i][0]
#
# # for k in range(n):
# #     print(line[k])
# # print()
# print(result)

# 위의 내가 푼 코드
# 어디가 틀린지 모르겠어서 다른 블로그 참고해서 다시 풀었다..


import sys
input = sys.stdin.readline

N = int(input())
lines = []
for i in range(N):
    lines.append(list(map(int, input().split())))

lines.sort()  # 정렬

# 맨 처음 꺼 기준으로
start = lines[0][0]
end = lines[0][1]

ans = 0
for k in range(1, N):  # 나머지 선들 보자
    now_start, now_end = lines[k][0], lines[k][1]

    # 겹치는 경우 => 시작점은 무조건 원래 있던 게 더 앞섬. 도착점은 비교해서 정하기.
    if end > now_start:
        end = max(end, now_end)

    # 안 겹치는 경우
    else:
        # 기존 것을 ans에 더하기
        ans += (end - start)
        # 새로운 걸로 업데이트
        start, end = now_start, now_end

ans += (end - start)
print(ans)
