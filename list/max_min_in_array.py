a = list(map(int,input("enter the number : ").split()))
max = a[0]
for i in a:
    if i>max:
        max=i
print(max)

min = a[0]
for i in a:
    if i<min:
        min=i
print(min)