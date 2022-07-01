n = int(input())
li = []

idx = 0
for i in range(n):
    v, w = map(int, input().split())
    li.append([v,w,i+1])
    
li = sorted(li, key= lambda x: x[:][:], reverse=True)

sum = 0
d = []
for l in li :
    if l[0] not in d:
        d.append(l[0])
        sum+= l[2]
        
print(sum)