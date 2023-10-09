# n = int(input())
#
# serial = []
# for i in range(n):
#     serial.append(input())
#
# # print(serial)
#
# serial_ascii = []
# for i in range(n):
#     tmp = []
#     for j in serial[i]:
#         tmp.append(ord(j))
#     serial_ascii.append(tmp)
#
# # print(serial_ascii)
# serial_ascii.sort(key=len)
# # print(serial_ascii)
#
# for i in range(n):
#     for j in range(i+1, n):
#         # print(i, j)
#         if len(serial_ascii[i]) == len(serial_ascii[j]):
#             # print("same")
#             i_sum = 0
#             j_sum = 0
#             for ii in serial_ascii[i]:
#                 if 48 <= ii <= 57:
#                     i_sum += ii
#             for jj in serial_ascii[j]:
#                 if 48 <= jj <= 57:
#                     j_sum += jj
#
#             if i_sum > j_sum:
#                 serial_ascii[i], serial_ascii[j] = serial_ascii[j], serial_ascii[i]
#
#             if i_sum == j_sum:
#                 # print(serial_ascii[i], serial_ascii[j], "same !")
#                 for k in range(len(serial_ascii[i])):
#                     if serial_ascii[i][k] == serial_ascii[j][k]:
#                         continue
#                     elif serial_ascii[i][k] < serial_ascii[j][k]:
#                         break
#                     elif serial_ascii[i][k] > serial_ascii[j][k]:
#                         serial_ascii[i], serial_ascii[j] = serial_ascii[j], serial_ascii[i]
#                         break
#     # print()
#
#
# # print(serial_ascii)
#
# for index, ascii_list in enumerate(serial_ascii):
#     # print(ascii_list)
#     for char in ascii_list:
#         print(chr(char), end="")
#     if index == n - 1:
#         continue
#     else:
#         print()
#     # print(index)

# 위의 내가짠 코드는 어디가 틀렸는지 모르겠다 ..

n = int(input())


def sum_num(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result += int(i)
    return result


arr = []
for i in range(n):
    arr.append(input())

arr.sort(key=lambda x: (len(x), sum_num(x), x))
for i in arr:
    print(i)
