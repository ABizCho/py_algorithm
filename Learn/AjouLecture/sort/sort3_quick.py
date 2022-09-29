'''
퀵 정렬 

# 시간복잡도
    O(NlogN) : 분할 횟수는 logN임. 순환 파티셔닝을 이용해, N개의 데이터에 대해 logN의 분할 횟수를 가질 수 있음
    ~ O(N^2) : 피벗 기준점이 적절하지 않아 파티션된 배열이 불균형 => 최대 N 번의 분할횟수 요구

        => logN회의 비교라면 데이터 개수 N의 1000개 값에 대해, 10번의 비교(2의 10승은 대략 1000)로 해결된다는 뜻
            => 따라서 데이터 1000개의 경우 1000*10 = 대략 10000의 연산으로 해결 가능

# 아이디어
    순환 이용 : 순환 1회당 파티셔닝 1번
    
    pivot을 기준으로 left와 right 선택변수 이용
        left = 정방향 탐색으로 pivot보다 큰 값 선택
        right = 역방향 탐색으로 pivot보다 작은 값 선택
        
    파티셔닝 케이스
        케이스1: left 진행방향과 right 진행방향 상 인덱스가 교차됨
            => right와 pivot 교환
        
        케이스2: 교차되지 않은 정상 케이스
            => left와 right 교환 
        
'''

arr = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr, start, end) :   # L,R에 대한 순환 구조를 위해 start, end를 매개변수로 갱신해줘야함
    if start >= end :   #순환 종료조건 : 배열 원소가 1개일 때
        return
    
    pivot = start
    left = start +1
    right = end
    
    while left <= right :
        while left <= end and arr[left] <= arr[pivot] :
            left += 1
        
        while right > start and arr[right] >= arr[pivot] :
            right -= 1
    
        if left > right :
            arr[right],arr[pivot] = arr[pivot],arr[right]
        
        else : 
            arr[left],arr[right] = arr[right],arr[left]
    
    quick_sort(arr, start, left-1)
    quick_sort(arr, right+1, end)


# TEST CODE=======
quick_sort(arr, 0, len(arr)-1)
print(arr)