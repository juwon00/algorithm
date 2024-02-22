N = int(input())

house = list(map(int, input().split()))

house = sorted(house)

print(house[ (N-1) // 2])

