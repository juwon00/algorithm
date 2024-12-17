for t in range(int(input())):
    height = list(map(int, input().split()))
    index = height.pop(0)
    count = 0
    print(index, height)
    tmp = []
    for h in height:
        if len(tmp) == 0:
            tmp.append(h)
            continue
        insert_index = 0
        for i in range(len(tmp)):
            print(i, tmp[i])
            if tmp[i] > h:
                break
            insert_index += 1
        print("insert_index", insert_index)
        tmp.insert(insert_index, h)
        print("tmp =", tmp)
        length = len(tmp) - insert_index - 1
        print("length", length)
        count += length

    print("count", count)
    print("=============")
    print()
    print(index, count)


# 다른 사람의 풀이
# 그냥 정렬할껀데 버블 정렬로 정렬하면 몇번 정렬을 해야되니? 물어보는 문제
# P=int(input())
# for _ in range(P):
#     arr=list(map(int,input().split()))
#     total=0
#     for i in range(1,len(arr)-1):
#         for j in range(i+1,len(arr)): # i 뒤에 애들과 전부 비교해서
#             if arr[i] > arr[j]:  # i가 더 크면
#                 arr[i],arr[j] = arr[j],arr[i]  # 자리바꾸기
#                 total+=1
#     print(arr[0], total)