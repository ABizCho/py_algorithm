'''
백준 2447 (골드5)

재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 


Input : 
    첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

Output : 
    첫째 줄부터 N번째 줄까지 별을 출력한다.
    
    
# 풀이 ref : https://lucian-blog.tistory.com/57

'''

def recur_star(n) :
    if n == 3 :
        return ['***','* *','***']
    
    arr = recur_star(n//3)
    stars = []
    
    for i in arr :
        stars.append(i*3)
    for i in arr :
        stars.append(i+' '*(n//3)+i)
    for i in arr :
        stars.append(i*3)
    
    return stars


#Test Code
n = int(input())
print('\n'.join(recur_star(n)))