N, K = map(int, input().split())

burger_people = input()

eat_burgur = [False] * N  # 햄버거 찾았을 때 기록할 리스트
count = 0

for i in range(N):
    if burger_people[i] == 'P':

        for x in range(i-K, i+K+1):
            if 0 <= x < N:  # burger_people 범위 지키기 위해
                if burger_people[x] == 'H' and eat_burgur[x] != True:  # 햄버거가 있는데 아직 안먹은 햄버거이면
                    eat_burgur[x] = True
                    count += 1
                    break

print(count)
