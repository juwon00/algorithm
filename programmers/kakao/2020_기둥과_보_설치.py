def check_build(answer):
    for x, y, a in answer:

        if a == 0:
            if y != 0 and [x, y - 1, 0] not in answer and [x - 1, y, 1] not in answer and [x, y, 1] not in answer:
                print("기둥 False")
                return False
        elif a == 1:
            if ([x, y - 1, 0] not in answer and [x + 1, y - 1, 0] not in answer and (
                    [x - 1, y, 1] not in answer or [x + 1, y, 1] not in answer)):
                print("보 False")
                return False

    return True


def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:

        if b == 0:
            print("삭제")
            answer.remove([x, y, a])
            if not check_build(answer):
                answer.append([x, y, a])
        elif b == 1:
            print("설치")
            answer.append([x, y, a])
            if not check_build(answer):
                answer.remove([x, y, a])
        print()

    # 처음 풀었던 런타임에러 나오는 코드
    # 왜 ??
    # for x, y, a, b in build_frame:
    #     print(x, y, a, b)
    #     if a == 0:
    #         print("기둥")
    #         if b == 0:
    #             print("삭제")
    #             answer.remove([x, y, a])
    #             if not check_build(answer):
    #                 answer.append([x, y, a])
    #
    #         elif b == 1:
    #             print("설치")
    #             if y == 0:
    #                 print("바닥")
    #                 answer.append([x, y, a])
    #             elif [x, y - 1, 0] in answer:
    #                 print("다른 기둥 위")
    #                 answer.append([x, y, a])
    #             elif ([x - 1, y, 1] not in answer and [x, y, 1] in answer) or (
    #                     [x - 1, y, 1] in answer and [x, y, 1] not in answer):
    #                 print("보 끝부분")
    #                 answer.append([x, y, a])
    #
    #     elif a == 1:
    #         print("보")
    #         if b == 0:
    #             print("삭제")
    #             answer.remove([x, y, a])
    #             if not check_build(answer):
    #                 answer.append([x, y, a])
    #
    #         elif b == 1:
    #             print("설치")
    #             if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer:
    #                 print("한쪽 끝 기둥")
    #                 answer.append([x, y, a])
    #             elif [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
    #                 print("양쪽 끝 보")
    #                 answer.append([x, y, a])
    #     print(answer)
    #     print()

    answer.sort()
    return answer


n = 5
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
               [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
answer = solution(n, build_frame)
print("answer:", answer)
