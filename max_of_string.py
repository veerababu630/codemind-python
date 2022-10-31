n=input()
t=0
for i in n:
    if t<ord(i):
        t=ord(i)
print(chr(t))        