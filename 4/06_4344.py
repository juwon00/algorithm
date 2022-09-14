c = int(input()) # 테스트 케이스의 개수

for i in range(c):
    li = list(map(int, input().split()))
    
    li_aver = (sum(li) - li[0]) / li[0] # 리스트의 평균
    
    stud = 0 # 평균을 넘는 학생의 수를 구하기
    for j in range(1,li[0]+1): # for j in li[1:] 로 표현 가능
        if li[j] > li_aver:
            stud += 1
    
    rate = stud / li[0] * 100 # 평균을 넘는 학생의 비율
    
    print(f'{rate:.3f}%')