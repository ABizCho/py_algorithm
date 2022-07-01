# 220701
arr = []

n = int(input())
for i in range(n):
    arr.append(int(input()))

    '''s1. 선택정렬 사용 : O(N^2)'''
# for i in range(len(arr)):
#     min_idx = i
    
#     for j in range(i+1,len(arr)):
#         if arr[min_idx] > arr[j] :
#             min_idx = j
#     arr[i],arr[min_idx] = arr[min_idx],arr[i]


    '''s2. 삽입정렬 사용 : O(N^2) ~ O(N):부분 정렬된 배열을 대상으로 할 경우'''
for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]: # 정렬된 리스트 범위 (현재 스텝에서 i가 편입되어 j로 여겨짐-> 정렬된 배열 내 j의 적절한 위치로 비교-교환 반복)
            arr[j],arr[j-1] = arr[j-1],arr[j]
        
        
    '''s3. 버블정렬 사용 : O(N^2) ~ O(N):부분 정렬된 배열을 대상으로 할 경우'''
# def bubble_sort(arr):
#     for i in range(len(arr)-1, 0, -1):
#         changed = False
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j+1], arr[j] = arr[j], arr[j+1]
#                 changed = True
#         if changed == False:
#             break
# bubble_sort(arr)

###최종결과 출력
for i in arr:
    print(i)
        
