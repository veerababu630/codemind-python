n=int(input())
sum=0
product=1
n1=n
while(n>0):
    d=n%10
    sum=sum+d
    product=product*d
    n=n//10
if (sum==product):
    print("Spy Number".format(n1))
else:
    print("Not Spy Number".format(n1))