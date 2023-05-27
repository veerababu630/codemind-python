a=input()
b=a.split(":")
c=((int(b[-2])*60)+int(b[-1]))*0.5
d=int(b[-1])*6
if abs(c-d)>180:
    print(360-abs(c-d))
else:
    print(abs(c-d))
    