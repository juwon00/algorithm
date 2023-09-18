N, L = map(int, input().split())
hole = list(map(int, input().split()))

hole = sorted(hole)

start = hole[0]
count = 1

for location in hole[1:]:
    if location in range(start, start+L):
        continue
    else:
        start = location
        count += 1

print(count)
