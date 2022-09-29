# 20220706 / 10989 수 정렬하기 3 : O(n+k)
    # 수의 범위가 작다면 카운팅 정렬을 사용하여 더욱 빠르게 정렬할 수 있습니다. : 메모리 제한 케이스 = 카운팅 정렬
    
''' 
카운팅 정렬 : 
    정렬할 대상 값의 양극단 범위까지를 모두 포함하는 순차적 인덱스를 구성하여, 모든 값을 count한 빈도를 배열에 저장함 그리고 순차적 값을 빈도수만큼 차례로 출력하여 정렬을 실시함.
    O(n+k)의 시간 복잡도를 가지며, 추가적인 배열을 사용하므로 O(n+k)의 공간복잡도도 요구받음. 대상 도메인에 따라 메모리 사용량이 극단적으로 늘어날 수 있으므로 상황에 따라 적절한 사용이 요구됨.
'''
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

count = [0]*(max(arr)+1)

# 카운팅 정렬
for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)) :
    for j in range(count[i]) :
        print(i, )
        
