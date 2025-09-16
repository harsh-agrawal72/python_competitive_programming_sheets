a = list(map(int,input("enter the number : ").split()))
start = 0
end = len(a)-1
for i in range(len(a)):
    if (start<end):
        a[start],a[end]=a[end],a[start]
        start+=1
        end-=1
print(a)