# 계수정렬( Counting sort )
  # 비교기반의 정렬기법이 아님
  # O(n + k) 의 시간/공간 복잡도
  # 빈도수를 Counting할 추가 메모리공간을 할당하는데, 이는 0~최댓값(k)의 범위를 모두 포함시키므로 범위가 유한한 대상으로만 수행 가능
  
  # 중간이 빈 양극단에만 값이 몰린 경우, 메모리 할당의 극단적 비효율 초래
  # 계수정렬은 동일값의 빈도수가 많은 경우 counting의 의미가 크므로 효율적이다.

arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0]*(max(arr)+1)

for i in range(len(arr)):
   count[arr[i]] += 1

for i in range(len(count)) :
   for j in range(count[i]):
       print(i, end=' ')
