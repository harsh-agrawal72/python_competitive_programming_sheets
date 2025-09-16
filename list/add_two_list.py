a = list(map(int,input("enter the number : ").split()))
b = list(map(int,input("enter the number : ").split()))
c = []
for i in a:
    c.append(a[i]+b[i])
print(c)
