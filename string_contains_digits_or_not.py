t=int(input())
for i in range(t):
    n=input()
    c=0
    for j in n:
        if j.isdigit():
            c+=1
    if c==0:
        print("No")
    else:
        print("Yes")