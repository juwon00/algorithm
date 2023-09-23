N = int(input())
K = int(input())
sensor = sorted(list(map(int, input().split())))

if K >= N:
    print(0)
    exit()

sensor_sub = [0] * (N - 1)
for i in range(N - 1):
    sensor_sub[i] = sensor[i + 1] - sensor[i]

sensor_sub = sorted(sensor_sub, reverse=True)

for j in range(K-1):
    sensor_sub.pop(0)

print(sum(sensor_sub))
