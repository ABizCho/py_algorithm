# 220705: 2751번 수 정렬2 : 
    #  O(NlogN)의 정렬 : Merge-Sort, 퀵, 이중피벗 퀵, Radix

'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''
n = int(input())
arr = []

while n > 0 :
    arr.append(int(input()))
    n -= 1    

#1 병합 정렬 ( 분할-정복 원리 / (1x2)의 2중루프 / stack 순환 )

#2 퀵 정렬 (피벗 개념 / 순환 stack / case1,2)
def quick_sort(arr, start, end) :
    if start > end :
        return
    
    pivot = start
    left = start + 1
    right = end
    
    while left <= right : 
        while left <= end  and arr[left] <= arr[pivot] :
            left += 1
        while right > start and arr[right] >= arr[pivot] :
            right -= 1
            
        # case1
        if left > right :
            arr[right],arr[pivot] = arr[pivot],arr[right]
        # case2
        else :
            arr[left],arr[right] = arr[right],arr[left]
            
    quick_sort(arr,start,right-1)
    quick_sort(arr,left+1,end)

#3. 이중 피벗 퀵 정렬

#4. Radix sort 기수 정렬
#==========출력============
quick_sort(arr,0,len(arr)-1)

for i in range(len(arr)):
    print(arr[i])
