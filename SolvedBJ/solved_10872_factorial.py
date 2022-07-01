# https://www.acmicpc.net/step/19

num = int(input())

def factorial(n):
    if n > 1 :
        return n * factorial(n-1)
    else :
        return 1


print(factorial(num))