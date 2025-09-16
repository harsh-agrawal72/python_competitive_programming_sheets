a = list(map(int,input("enter the number : ").split()))
for i in a:
    if (i%2==0):
        print(i,end=" ")
    print()
for i in a:
    if(i%2!=0):
        print(i,end=" ")