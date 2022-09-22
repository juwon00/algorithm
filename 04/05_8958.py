#생각해볼 문제

n = int(input()) # 테스트 케이스의 개수

for i in range(n):
    ox_list = list(input()) # list에 하나씩 추가
    score = 0
    sum_score = 0 # 새로운 ox리스트를 입력받으면 점수합계를 리셋
    
    for ox in ox_list:
        if ox == 'O':
            score += 1 # 'O'가 연속되면 1점씩 커짐
            sum_score += score
        else:
            score = 0
    
    print(sum_score)
    
