'''
< 수행시간 비교 >

선택 정렬 알고리즘 ( 열세 )
vs
파이썬 기본 정렬 라이브러리 ( 우세 ) 
'''

from random import randint
import time

'''
선택정렬
'''
# 배열에 10,000개의 정수 삽입 ( randint를 이용한 무작위 할당 )
array = []
for _ in range(10000):
    array.append(randint(1, 100)) # 1 ~ 100 사이의 무작위 정수 할당

# (1) 선택 정렬 프로그램 성능 측정
start_time = time.time()        # 측정시작

    # 메인 소스코드 : 선택정렬 알고리즘
for i in range(len(array)):     # array의 크기만큼 인덱스를 만들어 반복을 수행 
    min_index = i # 가장 작은 인덱스(= 첫번째 인덱스 번호부터 차례로) : i === 스왑기준위치 (1)
    for j in range(i + 1, len(array)):  # i 직후 인덱스 ~ 끝까지 반복 : j === i의 스왑 비교대상(2)
        if array[min_index] > array[j]:     ## 현재 러닝타임 인덱스 상태의 i와 j 값을 비교하여 / 스왑대상이 스왑기준위치의 값보다 작다면 최소변수에 j인덱스 할당 
            min_index = j
    array[i], array[min_index] = array[min_index],array[i] #두 원소의 위치 스왑 수행 후 다음 스왑기준위치 비교실시 (반복)

end_time = time.time()          # 측정종료
print('선택정렬 수행시간 :',end_time - start_time)   #수행시간 출력


'''
파이썬 정렬 라이브러리
'''
# 배열에 10,000개의 정수 삽입 ( randint를 이용한 무작위 할당 )
array = []
for _ in range(10000):
    array.append(randint(1, 100)) # 1 ~ 100 사이의 무작위 정수 할당
    
# 기본 정렬 라이브러리 성능 측정
start_time = time.time()    #측정시작

    #기본 정렬 라이브러리 사용하여 정렬 수행
array.sort()

end_time = time.time()      #측정종료
print('기본정렬 수행시간 :', end_time - start_time) #수행시간 출력

