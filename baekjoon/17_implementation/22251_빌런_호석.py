import sys

input = sys.stdin.readline


# zfill() 함수라는 것도 있음
# x = str(x).zfill(k)  ->  x=5, k=4 -> 0005
def make_str(num):
    if num < 10 ** (k - 1):
        num = str(num)
        while len(num) < k:
            num = "0" + num
    else:
        num = str(num)
    return num


nums = {
    "0": [1, 1, 1, 0, 1, 1, 1],
    "1": [0, 0, 1, 0, 0, 1, 0],
    "2": [1, 0, 1, 1, 1, 0, 1],
    "3": [1, 0, 1, 1, 0, 1, 1],
    "4": [0, 1, 1, 1, 0, 1, 0],
    "5": [1, 1, 0, 1, 0, 1, 1],
    "6": [1, 1, 0, 1, 1, 1, 1],
    "7": [1, 0, 1, 0, 0, 1, 0],
    "8": [1, 1, 1, 1, 1, 1, 1],
    "9": [1, 1, 1, 1, 0, 1, 1]
}
n, k, p, x = map(int, input().split())
x = make_str(x)
x_list = []
for i in range(len(x)):
    x_list.append(nums[x[i]])
print(type(x), x)
print()
result = 0
for i in range(1, n + 1):
    ii = make_str(i)
    if ii == x:
        continue
    print(ii, x)
    tmp = []
    for j in range(len(ii)):
        tmp.append(nums[ii[j]])
    print(x_list)
    print(tmp)

    cnt = 0
    for a in range(len(ii)):
        for b in range(7):
            if x_list[a][b] != tmp[a][b]:
                cnt += 1
    print(cnt)
    if cnt <= p:
        result += 1
    print()
print(result)
