a,b=map(int,input().split())
if a-1==b or b-1==a or a-b==9 or b-a==9:
    print("Yes")
else:
    print("No")