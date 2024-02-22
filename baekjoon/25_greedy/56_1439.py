S = input()
count = 0

for x in range(0, len(S) - 1):
    if S[x] != S[x+1]:
        count += 1

if count % 2 == 0:
    count = int(count / 2)
else:
    count = int((count+1) / 2)

print(count)
