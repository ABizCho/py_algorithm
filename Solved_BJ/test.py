n = int(input())
arr = []
while n != 0 :
    arr.append(int(input()))
    n -= 1


for i in range(len(arr)-1,0,-1):
    b_changed = False
    for j in range(i):
        if arr[j] > arr[j+1] :
            arr[j+1],arr[j] = arr[j], arr[j+1]
            b_changed=True
    if b_changed == False :
        break
for i in range(len(arr)):
    print(arr[i])