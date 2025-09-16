a = list(map(int,input("enter the number : ").split()))
digit = int(input())
new = []
for i in range(0,len(a)) :
    b = a[i]+digit
    new.append(b)
print(new)