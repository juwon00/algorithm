import sys
input = sys.stdin.readline

n = int(input())
waters = list(map(int, input().split()))

result = float("inf")
result_left = 0
result_right = n - 1


# 입력받은 데이터를 한번에 이분탐색 하는것이 아닌,
# 각각의 데이터 하나를 기준으로
# 나머지 데이터를 이분탐색을 통해 적절한 값을 탖는것
for i in range(n-1):

    water = waters[i]

    left = i + 1
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        tmp = waters[mid] + waters[i]

        if abs(tmp) < result:
            result_left = i
            result_right = mid
            result = abs(tmp)

        if tmp == 0:
            break
        elif tmp < 0:
            left = mid + 1
        else:
            right = mid - 1

print(waters[result_left], waters[result_right])
