def factorial(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
t=int(input())
for i in range(t):
    num=int(input())
    print(factorial(num))
    