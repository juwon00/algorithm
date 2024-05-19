def solution(str1, str2):
    print(ord("a"), ord("A"), ord("z"), ord("^"))

    str1_dict = {}
    for i in range(len(str1) - 1):
        print(str1[i] + str1[i + 1])
        if (str1[i] + str1[i + 1]).lower().isalpha():
            if (str1[i] + str1[i + 1]).lower() in str1_dict:
                str1_dict[(str1[i] + str1[i + 1]).lower()] += 1
            else:
                str1_dict[(str1[i] + str1[i + 1]).lower()] = 1
    print("str1_dict", str1_dict)

    str2_dict = {}
    for i in range(len(str2) - 1):
        print(str2[i] + str2[i + 1])
        if (str2[i] + str2[i + 1]).lower().isalpha():
            if (str2[i] + str2[i + 1]).lower() in str2_dict:
                str2_dict[(str2[i] + str2[i + 1]).lower()] += 1
            else:
                str2_dict[(str2[i] + str2[i + 1]).lower()] = 1
    print("str2_dict", str2_dict)

    if len(str1_dict) == 0 and len(str2_dict) == 0:
        return 65536

    min_dict = {}
    max_dict = {}
    for key in str1_dict:
        if key in str2_dict:
            min_dict[key] = min(str1_dict[key], str2_dict[key])
            max_dict[key] = max(str1_dict[key], str2_dict[key])
        else:
            max_dict[key] = str1_dict[key]

    for key in str2_dict:
        if key not in str1_dict:
            max_dict[key] = str2_dict[key]

    print(min_dict)
    print(max_dict)
    answer = int(sum(min_dict.values()) / sum(max_dict.values()) * 65536)

    return answer


str1 = "aa1+aa2"
str2 = "AAAA12"
answer = solution(str1, str2)
print("answer:", answer)

# 깔끔하게 푼 다른사람의 풀이
# set() & set(), set() | set() 사용이 멋짐
# import re
# import math
#
# def solution(str1, str2):
#     str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
#     str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]
#     print(str1)
#     print(str2)
#
#     gyo = set(str1) & set(str2)
#     hap = set(str1) | set(str2)
#     print(gyo)
#     print(hap)
#
#     if len(hap) == 0 :
#         return 65536
#
#     gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
#     hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])
#     print(gyo_sum)
#     print(hap_sum)
#
#     return math.floor((gyo_sum/hap_sum)*65536)
