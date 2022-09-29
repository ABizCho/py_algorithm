# 220701

nIn = int(input())

#역으로 접근
def fibo_recur(n) :
    if n <= 1 :     # 재귀 종료조건
        return n
    return fibo_recur(n-2) + fibo_recur(n-1)
    
print(fibo_recur(nIn))