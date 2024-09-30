from collections import defaultdict
import math


def make_num(time):
    time = time.split(":")
    h, m = time[0], time[1]
    return int(h) * 60 + int(m)


def solution(fees, records):
    answer = []
    basic_time, basic_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]

    in_dict = defaultdict(int)
    result_dict = defaultdict(int)

    for record in records:
        record = record.split(" ")
        time, car_num, io = make_num(record[0]), record[1], record[2]
        # print(time, car_num, io)
        if io == "IN":
            in_dict[car_num] = time
        elif io == "OUT":
            result_dict[car_num] += time - in_dict[car_num]
            del in_dict[car_num]
    # print(in_dict)
    # print(result_dict)
    # print()

    max_time = make_num("23:59")
    for car_num, time in in_dict.items():
        result_dict[car_num] += max_time - time

    # print(in_dict)
    # print(result_dict)

    for _, total_time in sorted(result_dict.items()):
        # print(total_time)
        if total_time < basic_time:
            answer.append(basic_fee)
        else:
            answer.append(basic_fee + math.ceil((total_time - basic_time) / unit_time) * unit_fee)

    return answer