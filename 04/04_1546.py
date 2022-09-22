n = int(input()) # 과목 개수
li = list(map(int, input().split())) # 각 과목들의 원래 성적

li_sort = sorted(li, reverse=True) # 내림차순으로 정렬

for i in range(1,n): # 점수를 수정함
    li_sort[i] = li_sort[i] / li_sort[0] * 100 
    
li_sort[0] = 100 # 자기 점수중 최댓값은 항상 100이 된다

li_aver = sum(li_sort) / n # 보정된 평균을 구한다

print(li_aver)