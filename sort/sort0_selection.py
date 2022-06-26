# 선택정렬: selection-sort : O(N^2)

array = [2,5,3,6,1,7,4,8,9,0]

for i in range(len(array)):
    min_index = i
    
    for j in range(i+1,len(array)):
        if array[min_index] > array[j] :
            min_index = j
    array[i],array[min_index] = array[min_index], array[i]
            
print(array)

