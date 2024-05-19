def solution(survey, choices):
    answer = ''

    dic = {"1": [0, 0], "2": [0, 0], "3": [0, 0], "4": [0, 0]}
    plus = [0, 3, 2, 1]

    print(survey)
    print(choices)
    print(dic)

    for i in range(len(survey)):
        if survey[i] == "RT":
            print("RT")
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                dic["1"][0] += plus[choices[i]]
            else:
                dic["1"][1] += choices[i] - 4

        elif survey[i] == "TR":
            print("TR")
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                dic["1"][1] += plus[choices[i]]
            else:
                dic["1"][0] += choices[i] - 4

        elif survey[i] == "CF":
            print("CF")
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                dic["2"][0] += plus[choices[i]]
            else:
                dic["2"][1] += choices[i] - 4

        elif survey[i] == "FC":
            print("FC")
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                dic["2"][1] += plus[choices[i]]
            else:
                dic["2"][0] += choices[i] - 4

        elif survey[i] == "JM":
            print("JM")
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                dic["3"][0] += plus[choices[i]]
            else:
                dic["3"][1] += choices[i] - 4

        elif survey[i] == "MJ":
            print("MJ")
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                dic["3"][1] += plus[choices[i]]
            else:
                dic["3"][0] += choices[i] - 4

        elif survey[i] == "AN":
            print("AN")
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                dic["4"][0] += plus[choices[i]]
            else:
                dic["4"][1] += choices[i] - 4

        elif survey[i] == "NA":
            print("NA")
            if choices[i] == 4:
                continue
            elif choices[i] < 4:
                dic["4"][1] += plus[choices[i]]
            else:
                dic["4"][0] += choices[i] - 4

        print(dic)

    char = [[], ["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    for i in range(1, 5):
        print(dic.get(str(i)))
        print(char[i])
        if dic.get(str(i))[0] >= dic.get(str(i))[1]:
            answer += char[i][0]
        else:
            answer += char[i][1]

    return answer


survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]
answer = solution(survey, choices)
print("answer:", answer)
