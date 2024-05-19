def solution(s):
    answer = ""
    print(s)

    num = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
           "eight": "8", "nine": "9"}
    print(num)

    tmp = ""
    for char in s:
        print(char)
        if char.isdigit():
            tmp = ""
            print("pass")
            answer += char
        else:
            tmp += char
            print(tmp)
            if tmp in num:
                print("find")
                get = num.get(tmp)
                print("get", get)
                answer += get
                tmp = ""

    return int(answer)


s = "23four5six7"
answer = solution(s)
print("answer", answer)
