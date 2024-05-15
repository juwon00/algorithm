# aaaaaaaaaabbbbbbbbbb
# 이런경우 10a10b 여서 답이 6이 된다
# (digit_length) 자릿수로 더해주는것을 생각못해서 애먹었다

def digit_length(n):
    ans = 0

    while n:
        n //= 10
        ans += 1

    return ans


def solution(s):
    answer = len(s)

    for i in range(1, len(s)):
        print(">>", i)

        j = 0
        tmp = 0
        cnt = 0
        while True:
            if j >= len(s):
                break
            if s[j + i: j + 2 * i] == "":
                tmp += len(s[j:j + i])
                break

            print(j, s[j:j + i], s[j + i: j + 2 * i])
            if s[j: j + i] == s[j + i:j + 2 * i]:
                print("same")
                cnt += 1
            else:
                if cnt > 0:
                    tmp += digit_length(cnt + 1)
                    cnt = 0
                tmp += i

            print("tmp, cnt", tmp, cnt)
            j += i

        if cnt > 0:
            tmp += digit_length(cnt + 1)

        print(tmp)
        answer = min(answer, tmp)
        print("answer", answer)
        print()

    return answer


s = "aaaaaaaaaabbbbbbbbbb"
answer = solution(s)
print("answer:", answer)
