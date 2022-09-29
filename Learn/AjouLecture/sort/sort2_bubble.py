'''
버블 정렬 : bubble sort 
: O(N^2) ~ O(N)

    # 아이디어
    2중 루프 반복을 이용해 
    인접한 2개의 items를 비교,교환 하며 순서대로 전체에 수행(스캔)
        - 한번의 스캔이 완료되면 리스트의 오른쪽 끝에 가장 큰 레코드가 위치하게 된다.
        - 한번의 스캔이 완료되면, 끝으로 이동한 레코드들을 제외하고 다시 스캔 반복.
    
    # 주의 : 특정 스캔에서 교환이 일어나지 않았을 시, 정렬 종료
    
    # 성능
        비교 횟수 :
            최선/평균/최악 케이스 모두 일정한 비교횟수
        이동 횟수 
            -최악 : 역순으로 정렬된 배열인 경우 = 3 X 비교횟수
            -최선 : 이미 정렬된 배열인 경우 = 0번의 이동횟수
            -(평균) : O(N^2)
        
        (특징): 비교연산보다 이동연산에 더 많은 시간이 소요된다.(레코드 이동 과다)
'''

def bubble_sort(arr):
    for i in range( len(arr)-1, 0, -1 ):
        b_changed= False
        for j in range(i):
            if arr[j] > arr[j+1] :
                arr[j],arr[j+1] = arr[j+1],arr[j]
                b_changed= True
            
        if b_changed == False  :
            break
        
#Test Code
arr = [5,2,3,4,1]
bubble_sort(arr)
print(arr)
            
            
        