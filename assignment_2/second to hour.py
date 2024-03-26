sec = int(input("enter second:"))
h=0
m=0
s=0

h=sec//3600
m=((sec%3600)//60)
s=((sec%3600)%60)
print(h, ":", m, ":", s)