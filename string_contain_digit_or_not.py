n=input()
c=0
for j in n:
    if j.isdigit():
        c+=1
if c>0:
    print("Contains {} digit".format(c))
else:
    print("Doesn't contain digit")