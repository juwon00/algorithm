from itertools import combinations


# 처음 생각한 조합으로 푸는 방법 - 시간초과
# def solution(number, k):
#     max_num = 0
#     for i in list(combinations(list(number), len(number) - k)):
#         x = int(''.join(i))
#         max_num = max(max_num, x)
#     answer = str(max_num)
#
#     return answer

def solution(number, k):
    answer = []

    for num in number:
        print(k, num)
        if not answer:
            answer.append(num)
            print("first", answer)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)
        print(k, answer)

    print(answer, answer[:-k])
    answer = answer[:-k] if k > 0 else answer

    return ''.join(answer)


number = "1924"
k = 2
solution(number, k)
